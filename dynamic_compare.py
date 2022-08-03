from scipy.spatial import distance
from sentence_transformers import SentenceTransformer


model = SentenceTransformer('distilbert-base-nli-mean-tokens')

def get_similarity(st1,st2):
    sentence1_embeddings = model.encode(st1)
    sentence2_embeddings = model.encode(st2)
    return (1 - distance.cosine(sentence1_embeddings, sentence2_embeddings))
