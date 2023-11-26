from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

SERVICE_ACCOUNT_FILE = 'docs_key.json'

SCOPES = ['https://www.googleapis.com/auth/documents.readonly']

CREDENTIALS = Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('docs', 'v1', credentials=CREDENTIALS)

document = service.documents().get(documentId='1_AfLgFoSSsdXSP6RidQnBHVNNw4zOEte_GQ6Ji3eG1w').execute()


def __read_paragraph_element(element):
    """Recursively reads a paragraph element to extract text."""
    text = ''
    if 'textRun' in element:
        text = element['textRun']['content']
    elif 'inlineObjectElement' in element:
        # Handle Inline objects (like images)
        text = '<InlineObject>'
    return text


def __read_structural_elements(elements):
    """Processes an array of structural elements to extract text."""
    text = ''
    for element in elements:
        if 'paragraph' in element:
            for para_element in element['paragraph']['elements']:
                text += __read_paragraph_element(para_element)
        elif 'table' in element:
            # Handle Table elements
            for row in element['table']['tableRows']:
                for cell in row['tableCells']:
                    text += __read_structural_elements(cell['content'])
        elif 'tableOfContents' in element:
            # Handle Table of Contents
            text += __read_structural_elements(element['tableOfContents']['content'])
    return text


def retrieve_prompt() -> str:
    return __read_structural_elements(document.get('body').get('content', []))
