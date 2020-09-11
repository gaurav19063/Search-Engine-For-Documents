import math
import os
import pickle
import re

import numpy
from nltk.tokenize import word_tokenize
from num2words import num2words

import pandas as pd
def load_titles():
    path="/home/gaurav/Desktop/IIITD/IR/Assignments/assignment2/titles/"
    dict3={}
    n = 0
    for y in os.listdir(path):

        f = open(path+y, encoding='ISO-8859-1')
        data=f.readlines()
        n = n + 1
        # print(y)

        for x in data:
            # print(x)

            if y=="index3.html" and x[0:10]=="<TR VALIGN":

                tokens=word_tokenize(x)
                # print(tokens)
                for i in range (len(tokens)):
                    if(tokens[i]=="HREF="):
                        dict3[tokens[i+2]]=tokens[i+16:][:tokens[i+16:].index("<")]



            elif(x[0:35]=="<TR VALIGN=TOP><TD VALIGN=TOP><B><A"):
                continue
            elif(x[0:10]=="<TR VALIGN"):
                ind1=x.index('>',37)

                k=x[37:ind1][1:-1]
                # print(k)
                x1=x[::-1]
                ind1 = x1.index('>')

                title=x1[:ind1][::-1][1:]
                # print(title)
                dict3[k]=word_tokenize(title)

        print("#############################################")
    # print(dict3)
    # print(len(dict3))
    return dict3
def cal_tf_idf1(dict1,x,n):
    if(n-dict1[x].count(0)==0):
        return 0
    else:
        return 1+math.log10(n/(n-dict1[x].count(0)))
def cal_tf_idf(dict1,x,n):
    if(n-dict1[x].count(0)==0):
        return 0
    else:
        return 1+math.log10(n/(n-dict1[x].count(0)))

def length_Normalize(list1):
    nor2=math.sqrt(numpy.dot(list1,numpy.transpose(list1)))
    if(nor2==0):
        nor2=1
    for i in range(len(list1)):

        list1[i]=list1[i]/nor2
    # print(list1)
    return list1




def score_cos_Sim(dict2,i,query_words2,list3,list1):

    list2=[]

    for x in query_words2:
        list2.append(dict2[x][i])
    # list2=length_Normalize(list2) #<-----------------------------------------
    sc=numpy.dot(list3,list2)
    # if sc==1:
    # print(list2,list3)

    # print(sc)
    return sc

def score_tf_idf(dict2, i, query_words2,list1):
    list2=[]
    for x in query_words2:
        # list1.append(dict2[x][-1])

        list2.append(dict2[x][i])
    return sum(list2)
def title_score(x,i,list1,dict3):
    # print(x,i,list1[0],dict3)
    # print()
    return 1  if  x in dict3[list1[i]] else 0

    # return 0
def varient1(doc_words,w,list1,i,dict3):

    sc=(1+math.log10(doc_words.count(w)+1))+(title_score(w,i,list1,dict3))*(1+math.log10(doc_words.count(w)+1))
    return sc

def varient2(doc_words,w,list1,i,dict3):
    return (doc_words.count(w))+title_score(w,i,list1,dict3)*(.5*doc_words.count(w))

def tf_idf():
    path="/home/gaurav/Desktop/IIITD/IR/Assignments/assignment2/mod_stories/"
    n=0
    dict1 = {}



    list1=[]
    for x in os.listdir(path):
        list1.append(x)
    l=len(list1)
    # dict3 = load_titles()
    # with open('dict_titles.pickle', 'wb') as handle:
    #     pickle.dump(dict3, handle, protocol=pickle.HIGHEST_PROTOCOL)
    # with open('dict_titles.pickle', 'rb') as handle:
    #     dict3 = pickle.load(handle)
    #
    # list2 = [0] * l
    # stop_words = set(stopwords.words('english'))
    #
    # for x in os.listdir(path):
    #
    #     f = open(path+x, encoding='ISO-8859-1')
    #     print(n)
    #     doc_words=word_tokenize(f.read().lower())
    #     doc_words1=doc_words.copy()
    #     terms = set(doc_words1)
    #     for w in terms:
    #         w1 = w
    #         if re.match(r'\d+',w):
    #             if w.isdigit():
    #                 w=num2words(w)
    #         if w in stop_words:
    #             continue
    #
    #         elif w in dict1.keys():
    #             dict1[w][n]=varient1(doc_words,w1,list1,n,dict3)###############################################
    #
    #
    #         else:
    #             dict1[w] = list2.copy()
    #             dict1[w][n]=varient1(doc_words,w1,list1,n,dict3)##########################################
    #     n = n + 1


    # n = len(list1)
    # # print(n,"yes")
    # for x in dict1.keys():
    #     p=cal_tf_idf(dict1,x,n)
    #     # print(p)
    #
    #     dict1[x].append(p)
    #     for i in range(n):
    #         dict1[x][i]=dict1[x][i]*dict1[x][-1]
    #

    with open('dict_words.pickle', 'rb') as handle:
        dict1 = pickle.load(handle)



##############################################################################################################
    # for i in range(l):
    #     list6 = []
    #     for x in dict1.keys():
    #         list6.append(dict1[x][i])
    #     val= numpy.sqrt(numpy.dot(list6, list6))
    #     print(i)
    #     for x in dict1.keys():
    #         dict1[x][i]=round(dict1[x][i]/val,5)
            # print(len(dict1[x]))


    # with open('dict_words_normalized', 'wb') as handle:
    #     pickle.dump(dict1, handle, protocol=pickle.HIGHEST_PROTOCOL)
    # with open('dict_words_normalized.pickle', 'rb') as handle:
    #     dict1 = pickle.load(handle)


#####################################################################################################################



    while(1):

        print("----------Enter Query----------------")
        query = input().lower()
        if(query=="-1"):
            print("-------Thank you----------------")
            break
        print("Finding Docs.........")
        query_words = word_tokenize(query)
        query_words2 = set(query_words)
        dict2 = {}
        flag = 0
        query_words3 = []
        for w in query_words2 :
            w2=w
            if re.match(r'\d+',w):
                if w.isdigit():
                     w=num2words(w)

            if w not in dict1.keys():
                continue
            query_words3.append(w)
            flag = flag + 1
            dict2[w] = (dict1[w].copy())
            dict2[w][-1] = query_words.count(w2) * dict1[w][-1]
        query_words2 = query_words3.copy()

        if flag == 0:
            print("------Enter value of k-----------")
            k = int(input())
            print(list1[:k])
            continue
        dict3 = {}
        i = 0
        list4 = []

        for x in query_words2:
            # print(x)
            # print(len(dict1[x]))
            # print(dict2[x][-1])
            list4.append(dict2[x][-1])
        # print(list4)
        list5 = length_Normalize(list4)
        for x in list1:
            # dict3[x]=score_cos_Sim(dict2,i,query_words2,list5,list1)###########################################
            dict3[x] = score_tf_idf(dict2, i, query_words2, list1)###########################################
            i = i + 1
        # print(dict3)
        dict3 = sorted(dict3, key=dict3.get, reverse=True)
        # print(list1)
        print("------Enter value of k-----------")
        k = int(input())
        print(dict3[0:k])


# ---------------------------------------

if(tf_idf()==-1):
    print("Enter a valid query")
