import openai
import numpy as np

openai.api_key = st.secrets["OPENAI_API_KEY"]  # Replace with env variable for security

def get_embedding(text, model="text-embedding-ada-002"):
    text = text.replace("\n", " ")
    result = openai.Embedding.create(input=[text], model=model)
    return result['data'][0]['embedding']

def cosine_similarity(vec1, vec2):
    a = np.array(vec1)
    b = np.array(vec2)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
