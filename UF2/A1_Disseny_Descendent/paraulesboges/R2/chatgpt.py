import openai #pip install openai

#Generate API key

#API key: https://platform.openai.com/account/api-keys

openai.api_key ="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"



ENGINE= "text-davinci-003"

ANSWER_QUANTITY=1

MAX_TOKENS =2048 #How many words?



#Question 1



question = "Què és ChatGPT?"

print(f"Asking question: {question}")

completion = openai.Completion.create(engine=ENGINE, prompt=question, n=ANSWER_QUANTITY, max_tokens=MAX_TOKENS)

print(completion.choices[0].text)



#Question 2

question = "Què significa GPT de ChatGPT?"

print(f"Asking question: {question}")

completion = openai.Completion.create(engine=ENGINE, prompt= question, n=ANSWER_QUANTITY, max_tokens=MAX_TOKENS)

print(completion.choices[0].text)