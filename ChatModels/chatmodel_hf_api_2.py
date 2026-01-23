from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="chat-completion",
    # instead of (repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0") we are using->
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    # because this is a model that explicitly supports chat / messages API.
    max_new_tokens=100,
    temperature=0.7
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("Explain Machine Learning in one line.")
print(result.content)



