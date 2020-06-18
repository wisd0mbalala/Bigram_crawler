# -*- coding: utf-8 -*-
import nltk, os, csv
from urllib import request
from nltk import *
from nltk.corpus import stopwords
from nltk.corpus import brown
from collections import Counter
import tkinter.messagebox as messagebox

def bigrams_to_csv(filepath):
    # tkinter.messagebox.showwarning(title='Warning', message='This takes some time, Please be patient! Once it is finished, It will give you a notification!')

    file = open(filepath + '/' + 'no_emptyline.txt', 'rt')
    #file_Bigrams = open(filepath + '/' + 'bigrams.txt', 'w+')
    #file_Bigrams.truncate()
    text = file.readlines()
    file.close()

    List = []

    for x in text:
        tokens = word_tokenize(x)
        step = 2
        list = [tokens[i:i + 2] for i in
                range(0, len(tokens), 1)]  # loop through every two tokens to create raw Bigrams
        for ii in list:
            # print(ii)
            # file_rawBigrams.write(str(ii))
            # file_rawBigrams.write('\n')
            # exclude puctuations and stopwords
            stop_words = set(stopwords.words('english'))
            i = [i for i in ii if i.isalpha() and i not in stop_words]
            if len(i) > 1:
                List.append(i)
                #file_Bigrams.write(str(i))
                #file_Bigrams.write('\n')

    #file_Bigrams.close()
    # tkinter.messagebox.showinfo(title='Thanks', message='File Created!')




    count_times = []
    for i in List:
        count_times.append(List.count(i))
        m = max(count_times)
        n = count_times.index(m)



    # L = len(List) - len(count_times)
    # print(L)

    index = 0
    D_value = {}

    for ii in List:
        l = []
        for i in ii:
            l.append(i)
        D_value[l[0] + '-' + l[1]] = count_times[index]
        index = index + 1

    Value = []
    D_sort = sorted(D_value.items(), key=lambda item: item[1], reverse=True)
    for value in D_value.values():
        Value.append(value)




    L = []
    L_novalue = []

    ind = 0
    for ii in List:
        l = []
        li = []
        for i in ii:
            l.append(i)
            li.append(i)
        x = l[0] + ',' + l[1] + ',' + str(count_times[ind])
        # y = [str(l[0]) + ',' + str(l[1])]
        if x not in L:
            L.append(x)
            L_novalue.append(li)
        ind += 1


    # N-Gram Tagging
    ###############################################################

    # brown_tagged_sents = brown.tagged_sents(categories='news')
    # brown_sents = brown.sents(categories='news')
    # unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
    # unigram_tagger.tag(brown_sents[2007])
    # unigram_tagger.evaluate(brown_tagged_sents)
    #
    # size = int(len(brown_tagged_sents) * 0.9)
    # size
    # train_sents = brown_tagged_sents[:size]
    # test_sents = brown_tagged_sents[size:]
    # unigram_tagger = nltk.UnigramTagger(train_sents)
    # print(unigram_tagger.evaluate(test_sents))
    # bigram_tagger = nltk.BigramTagger(train_sents)
    # print(bigram_tagger.evaluate(test_sents))
    # t0 = nltk.DefaultTagger('NN')
    # t1 = nltk.UnigramTagger(train_sents, backoff=t0)
    # t2 = nltk.BigramTagger(train_sents, backoff=t1)
    # print(t2.evaluate(test_sents))



    Tag=[]

    # Tag set choice
    for ii in L_novalue:
        Tag.append(nltk.pos_tag(ii,tagset='universal'))
        #Tag.append(nltk.pos_tag(ii))


    #Write data into csv file
    base = open(filepath + '/' + 'database.csv', 'w', newline='')
    write = csv.writer(base)

    row_to_write = []
    num = 0

    for iiii in Tag:
        r = []
        for ii in iiii:
            for i in ii:
                r.append(i)
        r.append(str(Value[num]))
        write.writerow(r)
        num += 1
