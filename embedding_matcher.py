import streamlit as st
from openai import OpenAI
import os
import numpy as np

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    project=os.getenv("OPENAI_PROJECT")
)

def get_embedding(text, model="text-embedding-ada-002"):
    text = text.replace("\n", " ")
    result = client.embeddings.create(input=text, model=model)
    return result.data[0].embedding

def cosine_similarity(vec1, vec2):
    a = np.array(vec1)
    b = np.array(vec2)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
