# openai_helper
A helper module for moderation, content filtering, and GPT-3 endpoints using OpenAI's Python library

First, create a file named .env in the directory of this script, and put the following:

OPENAI_KEY = "key"
  
Replacing key with your OpenAI API key generated in your account. The only function that charges your OpenAI account is the get_gpt_response. The others are free. Some additional information about fields can be found in the script's comments. You can find the API docs here: https://platform.openai.com/docs/

If you have feedback regarding the script only, send it to contact@symbionetwork.com. Otherwise, contact OpenAI support.

Function Descriptions:

get_moderation_response - Query moderation model and return either True or False for flagged field - useful for OpenAI content policy enforcement. If it's flagged, you should not send it to OpenAI using get_gpt_response. See https://platform.openai.com/docs/guides/moderation/overview for more information and what the response data actually looks like.

get_filter_response - Content filter model. This returns either a 0, 1, or 2. A 0 or 1 signifies clean or "potentially harmful" content and should be accepted without scrutiny. A 2, however, signifies harmful content, but can be checked to ensure that the AI model got it right. See https://platform.openai.com/docs/models/content-filter for more information.

get_gpt_response - Queries GPT-3's Davinci model. The cost is $0.02 per 1000 tokens. You can also use different models. See https://platform.openai.com/docs/models/overview for more information and use cases.

get_img_response - Queries DALL-E models for image creation. The cost is $0.02 per image by default. Smaller images are cheaper. This returns a temporary URL of the image.