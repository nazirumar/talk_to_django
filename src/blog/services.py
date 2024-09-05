
from transformers import BertTokenizer, BertModel
from pgvector.django import CosineDistance
from django.db.models import F, FloatField
from django.apps import apps

from decouple import config
import requests
import json

# Configuration
HUGGINGFACE_API_KEY = config("HUGGINGFACE_API_KEY")
LLM_MODEL = config("LLM_MODEL", default='gpt2')
EMBEDDING_MODEL = config("EMBEDDING_MODEL", default='sentence-transformers/all-MiniLM-L6-v2')
EMBEDDING_LENGTH = 384  # Adjust this based on the embedding model used


# Set the headers for the Hugging Face API
headers = {
    "Authorization": f"Bearer {HUGGINGFACE_API_KEY}"
}

# Function to generate text using the Hugging Face API
def generate_text(prompt, model=LLM_MODEL):
    api_url = f"https://api-inference.huggingface.co/models/{model}"
    payload = {
        "inputs": prompt,
        "options": {"wait_for_model": True}
    }
    response = requests.post(api_url, headers=headers, json=payload)
    return response.json()

# Function to get embeddings using the Hugging Face API
def get_embedding(text, model=EMBEDDING_MODEL):
    api_url = f"https://api-inference.huggingface.co/models/{model}"
    payload = {
        "inputs": text,
        "options": {"wait_for_model": True}
    }
    response = requests.post(api_url, headers=headers, json=payload)
    return response.json()[0]['embedding']

def get_query_embedding(text):
    # get_or_created EMbedding
    return get_embedding(text)


def search_posts(query, limit=5):
    BlogPost = apps.get_model(app_label='blog', model_name='BlogPost')
    query_embedding = get_query_embedding(query)
    qs = BlogPost.objects.annotate(
    distance=CosineDistance('embedding',query_embedding),
    similarity=1 - F("distance")
    ).order_by('distance')[:limit]
    return qs
