from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_embedding(text, model="text-embedding-ada-002"):
    text = text.replace("\n", " ")
    result = client.embeddings.create(input=text, model=model)
    return result.data[0].embedding
