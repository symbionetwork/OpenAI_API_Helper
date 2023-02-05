# This is necessary for the rest of the script to work. I wouldn't change anything in the following fields.
import requests
import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.environ.get("OPENAI_KEY")
moderation_endpoint_url = "https://api.openai.com/v1/moderations"

# Query moderation endpoint and return either True or False for flagged - useful for OpenAI content policy enforcement
# If it's flagged, you should not send it to OpenAI using get_gpt_response. See https://platform.openai.com/docs/guides/moderation/overview
# for more information and what the response data actually looks like.
def get_moderation_results(input):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai.api_key}"
    }
    data = {"input": f"{input}"}
    response = requests.post(moderation_endpoint_url, headers=headers, json=data)
    response_data = response.json()
    return response_data['results'][0]['flagged']

# Content filter endpoint. This returns either a 0, 1, or 2. A 0 or 1 signifies clean or "potentially harmful" content.
# A 0 or 1 should be accepted without scrutiny. A 2, however, signifies harmful content, but can be checked to ensure
# that the AI got it right. See https://platform.openai.com/docs/models/content-filter for more information.
def get_filter_results(input):
    response = openai.Completion.create(
        model="content-filter-alpha",
        prompt = f"<|endoftext|>{input}\n--\nLabel:",
        temperature=0,
        max_tokens=1,
        top_p=0,
        logprobs=10
    )

    return response.choices[0].text

# Queries GPT-3's Davinci model. The cost is $0.02 per 1000 tokens. Max_tokens can be up to 4000 tokens. You can also use
# different models. See https://platform.openai.com/docs/models/overview for more information and use cases.
def get_gpt_response(input):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=input,
    max_tokens=800,
    temperature=0.5,
    )
    return response.choices[0].text