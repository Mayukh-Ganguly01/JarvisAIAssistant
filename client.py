from openai import OpenAI
client = OpenAI(
    api_key="API_KEY" ,
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a virtual assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": ""}
  ]
)

print(completion.choices[0].message.content)

