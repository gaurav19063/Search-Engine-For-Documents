import os
from nltk.corpus import stopwords

from nltk import word_tokenize


def jaccard():
    path="/home/gaurav/Desktop/IIITD/IR/Assignments/assignment2/mod_stories/"
    n=0

    print("----Enter Query--------")
    query=input()
    query_words=list(set(word_tokenize(query.lower())))
    dict1 = {}
    for x in os.listdir(path):

        # print(path+x)
        f = open(path+x, encoding='ISO-8859-1')
        # print(f.read())
        n=n+1
        print(n)
        stop_words = set(stopwords.words('english'))
        doc_words=list(set(word_tokenize(f.read().lower())))
        for s in query_words:
            if s in stop_words:
                query_words.remove(s)
        for s in doc_words:
            if s in stop_words:
                doc_words.remove(s)
        query_words=set(query_words)
        doc_words = set(doc_words)

        # query_words=query_words-(query_words & set(stopwords))
        # doc_words=doc_words-(doc_words & set(stopwords))
        nom=len(query_words & doc_words)
        denom=len(query_words | doc_words)



        dict1[x]=nom/denom
        # docs.append(dict1)
    # print("Give value of k")
    print (dict1)
    dict1 = sorted(dict1, key=dict1.get, reverse=True)
    # dict1 = sorted(dict1.items(), key=lambda kv: (kv[1], kv[0]))
    print("Give value of k")
    k=int(input())
    print(dict1[0:k])





# ---------------------------------------

jaccard()


