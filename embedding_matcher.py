import openai
import numpy as np

openai.api_key = "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"  # Replace with env variable for security

def get_embedding(text, model="text-embedding-ada-002"):
    text = text.replace("\n", " ")
    result = openai.Embedding.create(input=[text], model=model)
    return result['data'][0]['embedding']

def cosine_similarity(vec1, vec2):
    a = np.array(vec1)
    b = np.array(vec2)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
