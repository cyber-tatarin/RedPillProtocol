import os

import openai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

GPT_MODEL = os.getenv("GPT_MODEL")
openai.api_key = os.getenv("OPENAI_API_TOKEN")

print(GPT_MODEL, 'gpt_model!')


def get_blueprint(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model=GPT_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    answer = response["choices"][0]["message"]["content"]
    return answer


if __name__ == "__main__":
    print(get_blueprint("""# MISSION
You are a professional coach. Your mission is to provide the user with the exact per minute plan for their weekly routine which will help them to achieve their goal in 1 year. The goal is to form a strong habit for each activity they need to reach the goals. I'd like to start with very easy and really quick actions to start forming a habit. And increase amount of time and level of difficulty next weeks gradually

# INTERACTION SCHEMA
The user will provide you with his mandatory activities which he can not skip or replace. You should fulfill his spare time completely from the very morning to the very evening

# RESPONSE SCHEMA
Provide response in the format plain text. Text should contain only schedule WITHOUT any additional information. The response should be complete for every day of a week. Provide concrete actions, never write abstract morning routine, etc. If the action is very easy (like drink a glass of water), do not book 15 minutes for it, be very concrete with needed time

My schedule is: Mon: university(from 15:00 till 20:00), Tue: gym(from 10:00 till 13:00), Wed: university (from 16 till 19), Thu: gym(from 8 till 11), university(from 13 till 18), Fri is t
he same as Wednesday, and no mandatory plans for weekends.

My goal is to be able to dunk in a basketball game. i lack 10 cm in jump to do it"""))
