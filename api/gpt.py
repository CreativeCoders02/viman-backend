from openai import OpenAI
from os import environ as env
client = OpenAI(api_key=env.get('OPENAI_API_KEY'))


def getResponse(messages):
    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=messages,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response


def getUserMessage(name):

    messages = [
        {
            "role": "system",
            "content": "You just give a warm welcome to newly registered users in creative coders website.  User will give their name , you just need to respond to it. Just flatter the user"
        },
        {
            "role": "user",
            "content": f"I'm {name}."
        }
    ]
    response = getResponse(messages)
    content = response.choices[0].message.content
    return content
