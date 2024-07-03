import numpy as np
from langchain_community.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings()


class VectorStore():

    def __init__(self, embedding_model):
        self.embeds = {}
        self.embedding_model = embedding_model
    
    def get(self, text):
        return self.embeds[text]
    
    def add(self, texts):
        embeds = self.embedding_model.embed_documents(texts)
        for i, text in enumerate(texts):
            self.embeds[text] = embeds[i]

    def query(self,texts, num_results=10):
        query_embed = self.embedding_model.embed_query(texts)

        results = []
        print("asdasd")
        print(self.embeds.items())
        for vector_id, vector in self.embeds.items():
            similarity = np.dot(query_embed, vector)/(np.linalg.norm(query_embed) * np.linalg.norm(vector))
            results.append((vector_id, similarity))
       
        results.sort(key=lambda x: x[1], reverse = True)
        print(results)
        return results[:num_results]
    
file = open(r"C:\Users\devxm\Documents\AI Stuff\LLMincontextlearning\context.txt",'r',encoding="utf8")
context = file.read()
file.close()

text = "This is a test document."



vector_store = VectorStore(embedding_model=embeddings)
vector_store.add(context)

print(vector_store.query('memory'))
# while True:
#     q = input("Ask a query: ")
#     print(vector_store.query(q))

#     if q.lower() == "exit":
#         break
        