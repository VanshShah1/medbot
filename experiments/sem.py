from txtai.embeddings import Embeddings
embeddings=Embeddings()
<<<<<<< HEAD
data = ["string data"]
=======
data = ["string dataset"]
>>>>>>> 79c297d846bb9c8f506962c94c1222d76633018e
while True:
        query=input("prompt: ")
        uid=embeddings.similarity(query=query, data=data)[0][0]
        res=data[uid]
        print(res)
        print("-" * 50)
