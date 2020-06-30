import nltk, os, spacy, csv
from nltk import *
from nltk.corpus import stopwords

nlp = spacy.load("en_core_web_sm")
nlp.max_length = 1500000

def bigrams_with_ner_to_csv(path):
    tkinter.messagebox.showwarning(title='Warning', message='This takes some time(This process last about 2.5 minutes with a 1.2 Mb txt file), Please be patient!\nOnce it is finished, It will give you a notification!')
    file_ = open(path + '/' + 'no_emptyline.txt', 'rt')
    doc = nlp(file_.read())

    #Exclude Entity type PERSON, GPE, LOC
    ents = [e.text for e in doc.ents if e.label_ == "PERSON" or e.label_ == "GPE" or e.label_ == "LOC"]
    line = ''
    for i in ents:
        line += i + ' '
    ents_i = word_tokenize(line)
    ents_i = list(set(ents_i))

    tokens = []
    List_ = []
    #Lemmatization
    for item in doc:
        tokens.append(item.lemma_)
    #loop through every two tokens to create raw Bigrams
    token_pair = [tokens[i:i + 2] for i in range(0, len(tokens), 1)]

    for ii in token_pair:
        stop_words = set(stopwords.words('english'))
        i = [i for i in ii if i not in stop_words and i not in ents_i and i.isalpha()]
        if len(i) > 1:
            List_.append(i)
    file_.close()

    #convert strings into lower case
    List_lower = []
    for l in List_:
        x = [s.lower() for s in l]
        List_lower.append(x)

    count_times = []
    for i in List_lower:
        count_times.append(List_lower.count(i))
        m = max(count_times)
        n = count_times.index(m)

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

    with open(path + '/' + 'database.csv', 'w', newline='') as f:
        f_csv = csv.DictWriter(f, headers)
        f_csv.writeheader()
        f_csv.writerows(rows)

    tkinter.messagebox.showinfo(title='Thanks', message='File Created!')
