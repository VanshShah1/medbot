from txtai.embeddings import Embeddings
embeddings=Embeddings()
data = ["string data"]
while True:
        query=input("prompt: ")
        uid=embeddings.similarity(query=query, data=data)[0][0]
        res=data[uid]
        print(res)
        print("-" * 50)