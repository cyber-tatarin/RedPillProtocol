from datetime import datetime, timedelta

import pygsheets

key_json = 'gsheets_key.json'


def find_row_number(ad_link, worksheet):
    try:
        # Authenticate using service account credentials
        # gc = pygsheets.authorize(service_file=key_json)
        
        # Open the Google Sheet by name
        # sheet = gc.open('FERC telegram bot overview')
        # worksheet = sheet[0]
        
        cells_list_of_lists = worksheet.find(str(ad_link), matchEntireCell=True)  # [[]]
        print(cells_list_of_lists)
        if cells_list_of_lists:  # empty list object considered as false
            return cells_list_of_lists[0].row
        else:
            return None
    except Exception as x:
        print(x)


def insert_base_items(list_of_lists_of_item_rows):
    try:
        # Authenticate using service account credentials
        gc = pygsheets.authorize(service_file=key_json)
        # Convert the list of links into a single column
        
        # Open the Google Sheet by name
        sheet = gc.open('RedPillProtocol')
        # Select the first worksheet in the Google Sheet

        worksheet = sheet.worksheet_by_title('main')
        
        worksheet.insert_rows(row=1, values=list_of_lists_of_item_rows)
    
    except Exception as x:
        print(x)
    