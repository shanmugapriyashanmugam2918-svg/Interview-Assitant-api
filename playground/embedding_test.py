from sentence_transformers import SentenceTransformer

model=SentenceTransformer("all-MiniLm-L6-v2")

embedding=model.encode("I love Plants and me")

print(type(embedding))
print(len(embedding))
print(embedding[:10])