from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

documents = [
    "Library provide access to knowledge and resources.",
    "Machine Learning improves data analysis.",
    "Natural Language processing helps computers understand text.",
    "Childer enjoy interactive storytelling and books."
]

doc_embeddings = model.encode(documents, convert_to_tensor=True)

query = "AI understanding language"
query_embedding = model.encode(query, convert_to_tensor=True)

scores = util.cos_sim(query_embedding, doc_embeddings)

best_idx = scores.argmax()
print("Query:", query)
print("\nBest Match:")
print(documents[best_idx])
print("\nScore:", scores[0][best_idx])