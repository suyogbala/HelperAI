import openai


openai.api_key = 'API_key'

response = openai.Completion.create(
    model="gpt-3.5-turbo-instruct",
    prompt="",
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

print(response)