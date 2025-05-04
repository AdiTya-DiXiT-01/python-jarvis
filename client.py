from openai import OpenAI

def ai_response(text):
    client = OpenAI(api_key='***********************api_key_here************************')

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {'role': 'system', 'content': 'You are a helpful voice assistant.'},
            {'role': 'user', 'content': text}
        ]
    )

    return response.choices[0].message.content
