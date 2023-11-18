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


def init_assistant_context(user_context: str) -> str:
    thread = client.beta.threads.create()  # new thread for new customer
    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=user_context
    )

    return thread.id


def get_day_blueprint(day_data: str, thread_id: str) -> str:
    client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=day_data
    )

    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=ASSISTANT_ID
    )

    print(run)

    while True:
        time.sleep(1)
        run = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run.id
        )
        if run.status == "completed":
            break
        elif run.status == 'failed':
            raise Exception('Failed attempt to communicate with OpenAI')
        else:
            pass

    messages = client.beta.threads.messages.list(
        thread_id=thread_id
    )

    print(messages.data[0].content[0].text.value)

    return messages.data[0].content[0].text.value


def get_blueprint(data: dict[str, str]) -> str:
    thread = init_assistant_context(data["context"])
    print("Thread: " + thread)
    monday = get_day_blueprint(data["monday"], thread)
    print(monday)
    tuesday = get_day_blueprint(data["tuesday"], thread)
    wednesday = get_day_blueprint(data["wednesday"], thread)
    thursday = get_day_blueprint(data["thursday"], thread)
    friday = get_day_blueprint(data["friday"], thread)
    saturday = get_day_blueprint(data["saturday"], thread)
    sunday = get_day_blueprint(data["sunday"], thread)
    return f"[{monday},{tuesday},{wednesday},{thursday},{friday},{saturday},{sunday}]"
