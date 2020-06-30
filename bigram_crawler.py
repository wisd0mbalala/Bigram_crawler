# -*- coding: utf-8 -*-
import nltk, os, csv, spacy
from urllib import request
from nltk import *
from nltk.corpus import stopwords
from nltk.corpus import brown
from collections import Counter
import tkinter.messagebox as messagebox
nlp = spacy.load("en_core_web_sm", disable=["ner"])
nlp.max_length = 1500000

def bigrams_to_csv(filepath):
    tkinter.messagebox.showwarning(title='Warning', message='This takes some time, Please be patient!\n(This process last about 2.5 minutes with a 1.2 Mb txt file)\nOnce it is finished, It will give you a notification!')

    file = open(filepath + '/' + 'no_emptyline.txt', 'rt')
    #file_Bigrams = open(filepath + '/' + 'bigrams.txt', 'w+')
    #file_Bigrams.truncate()
    doc = nlp(file.read())
    file.close()

    List_ = []
    tokens = []

    for item in doc:
        tokens.append(item.lemma_)
    token_pair = [tokens[i:i + 2] for i in
                range(0, len(tokens), 1)]  # loop through every two tokens to create raw Bigrams
    for ii in token_pair:
        stop_words = set(stopwords.words('english'))
        i = [i for i in ii if i.isalpha() and i not in stop_words]
        if len(i) > 1:
            List_.append(i)
                #file_Bigrams.write(str(i))
                #file_Bigrams.write('\n')

    #file_Bigrams.close()

    #convert strings into lower case
    List_lower = []
    for l in List_:
        x = [s.lower() for s in l]
        List_lower.append(x)

    #Calculate Occurrences
    count_times = []
    for i in List_lower:
        count_times.append(List_lower.count(i))
        m = max(count_times)
        n = count_times.index(m)



    # L = len(List) - len(count_times)
    # print(L)

    index = 0
    D_value = {}

    for ii in List_lower:
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
    for ii in List_lower:
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
        Tag.append(nltk.pos_tag(ii, tagset='universal'))
        #Tag.append(nltk.pos_tag(ii))


    #Write data into csv file
    headers = ['Bigram', 'POS-Tags', 'Gram1', 'Tag1', 'Gram2', 'Tag2', 'Occurrences']
    num = 0
    rows = []
    for iiii in Tag:
        dict = {}
        r = []
        for ii in iiii:
            for i in ii:
                r.append(i)
        dict['Bigram'] = r[0] + '-' + r[2]
        dict['POS-Tags'] = r[1] + '-' + r[3]
        dict['Gram1'] = r[0]
        dict['Tag1'] = r[1]
        dict['Gram2'] = r[2]
        dict['Tag2'] = r[3]
        dict['Occurrences'] = Value[num]
        rows.append(dict)
        num += 1

    with open(filepath + '/' + 'database.csv', 'w', newline='') as f:
        f_csv = csv.DictWriter(f, headers)
        f_csv.writeheader()
        f_csv.writerows(rows)

    tkinter.messagebox.showinfo(title='Thanks', message='File Created!')
