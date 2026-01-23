# This LLMs code is not going to execute because of no api key is mentioned in .env file because this is paid api key 
# This is code of LLM using openai api key in ChatModels we see chatmodel using this openai api key but they have diffrenece 
# one is LLM and another is chatmodel

from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct')

result = llm.invoke("What is the capital of India")

print(result)
