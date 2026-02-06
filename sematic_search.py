from sentence_transformers import SentenceTransformer, util
import matplotlib.pyplot as plt

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

scores = util.cos_sim(query_embedding, doc_embeddings)[0]

scores_list = scores.cpu().tolist()

ranked = sorted(
    enumerate(scores_list),
    key =lambda x: x[1],
    reverse= True
)
print(f"Query: {query}\n")
print("Ranked results (hoghest similarity first):")
for idx,score in ranked:
    print(f"- score={score:.4f} | doc[[idx]] = {documents[idx]}")

labels = [f"doc {i}" for i in range(len(documents))]
plt.figure()
plt.title("Sematic similarity scores vs query")
plt.xlabel("Documents")
plt.ylabel("Cosine similarity")
plt.bar(labels, scores_list)
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()