import openai
openai.api_key = "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"
model_engine = "text-davinci-003"
while True:
   prompt = str(input('Human :  '))
   completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
   )
   print('AI :  ' + str(completion.choices[0].text))