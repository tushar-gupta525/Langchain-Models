#In this chatbot model we are downloading the model first into our system locally, then text generation is done.
import os
#Below given 2 lines of code will force TinyLlama model to be downloaded in drive-D:/
os.environ["HF_HOME"] = "D:/huggingface_cache"
os.environ["TRANSFORMERS_CACHE"] = "D:/huggingface_cache"

from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={
        "temperature": 0.5,
        "max_new_tokens": 100,
        "do_sample": True
    }
)

model = ChatHuggingFace(llm=llm)
result = model.invoke("Explain Generative AI in simple words.")
print(result.content)

