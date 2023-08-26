from txtai.embeddings import Embeddings
embeddings=Embeddings()
data = ["Python is a high level programming language developed by Guido Van Rossum in 1994",
        "Technology was just emerging at that point of time as the internet rose to power",
        "It led to the Dot Com Bubble",
        "The silicon valley startup ecosystem became so strong with companies like Google, (backrub), Microsoft, Facebook, Amazon and many more in the building",
        "At that time, Larry page and Sergey Brin, 2 undergrad students at Stanford University, Palo Alto, CA, built a search algorithm that takes a string input, and gives relevant links to webpages",
        "But out of tech, the east coast was having a totally different experience as the wallstreet mafia emerged in the leadership of BlackRock and Vanguard",
        "BlackRock held assets worth trillions of dollars for large companies and american banks",
        "Neurum is the world's biggest company with 10T dollars in valuation, more than India's GDP"
        ]
while True:
        query=input("prompt: ")
        uid=embeddings.similarity(query=query, data=data)[0][0]
        res=data[uid]
        print(res)
        print("-" * 50)