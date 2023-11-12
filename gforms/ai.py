import os
import time

import openai
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

load_dotenv(find_dotenv())

GPT_MODEL = os.getenv("GPT_MODEL")
ASSISTANT_ID = os.getenv("ASSISTANT_ID")

openai.api_key = os.getenv("OPENAI_API_TOKEN")

client = OpenAI(api_key=os.getenv("OPENAI_API_TOKEN"))

print(f"GPT model: {GPT_MODEL}, assistant id: {ASSISTANT_ID}")


def generate_blueprint(user_data: str) -> str:
    thread = client.beta.threads.create()
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=user_data
    )
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=ASSISTANT_ID
    )

    while True:
        time.sleep(1)
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )
        if run.status == "completed":
            break
        else:
            pass

    response_message = client.beta.threads.messages.retrieve(
        thread_id=thread.id,
        message_id=message.id
    )

    return response_message.content[0].text.value
