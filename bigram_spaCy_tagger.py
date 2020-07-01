import spacy,csv
from nltk import *
from nltk.corpus import stopwords

nlp = spacy.load("en_core_web_sm")
nlp.max_length = 1500000

# sentences = 'His parents were very hard-working and deeply religious people, but so poor that they lived with their five children in only two rooms. Writing to his brother Mihail, Dostoevsky says: “They snapped words over our heads, and they made us put on the white shirts worn by persons condemned to death.'

path = 'C:/Users/ncllz/Documents/project'
file_ = open(path + '/' + 'no_emptyline_short.txt', 'rt')
sentences = file_.read()
file_.close()

doc = nlp(sentences)


tokens_universal = []
pos_universal = []
ent = []

for sent in doc.sents:
    tokens = [token.lemma_ for token in sent]
    pos = [token.pos_ for token in sent]
    tokens_universal.extend(tokens)
    pos_universal.extend(pos)

    ents = [e.text for e in sent.ents if e.label_ == "PERSON" or e.label_ == "GPE" or e.label_ == "LOC"]
    line = ''
    for i in ents:
        # line += i + ' '
        if i not in ent:
            ent.append(i)

ent = " ".join(ent)
ents_i = word_tokenize(ent)
print(ents_i)

dict_lemma_pos = dict(zip(tokens_universal,pos_universal))
print(dict_lemma_pos)

tokens = list(dict_lemma_pos.keys())
tags = list(dict_lemma_pos.values())

pair_t1=[]
pair_t2=[]
token_pairs = [tokens[i:i + 2] for i in range(0, len(tokens), 1)]
for ii in token_pairs:
    l=[]
    for i in ii:
        l.append(i)
    if len(l)>1:
        pair_t1.append(l[0]+ ' ' + l[1])
pos_pairs = [tags[i:i + 2] for i in range(0, len(tags), 1)]
for ii in pos_pairs:
    l=[]
    for i in ii:
        l.append(i)
    if len(l)>1:
        pair_t2.append(l[0]+ ' ' + l[1])

print(pair_t1)
print(pair_t2)

stop_words = set(stopwords.words('english'))

pair_t1_tok=[]
pair_t1_new=[]
pair_t2_tok=[]
for ii in pair_t1:
    ii_tok = word_tokenize(ii)
    pair_t1_tok.append(ii_tok)
    pair_t1_new.append(ii_tok)
for ii in pair_t2:
    ii_tok = word_tokenize(ii)
    pair_t2_tok.append(ii_tok)

# for ii in list(pairs_dict.keys()):
#     ii_tok = word_tokenize(ii)
#     for i in ii_tok:
#         if i in stop_words or i in ents_i or not i.isalpha():
#             del pairs_dict[ii]
#             print(pairs_dict)

for ii in pair_t1_tok[:]:
    for x in ii:
        should_remove = False
        for i in ii:
            if not i.isalpha() or i in stop_words or i in ents_i:
                should_remove = True

    if should_remove:
        pair_t1_tok.remove(ii)

pair_t2_new=[]
for i in pair_t1_tok:
    if i in pair_t1_new:
        index = pair_t1_new.index(i)
        pair_t2_new.append(pair_t2_tok[index])


print(pair_t1_tok)
print(len(pair_t1_tok))
print(pair_t2_new)
print(len(pair_t2_new))
####################################################################
new_list=list(zip(pair_t1_tok,pair_t2_new))
print(new_list)
List_lower=[]
for l in pair_t1_tok:
    x = [s.lower() for s in l]
    List_lower.append(x)

d = {}
l = []
for x, y in zip(List_lower,pair_t2_new):
    l1=[]
    l2=[]
    for i,ii in zip(x,y):
        l1.append(i)
        l2.append(ii)
    l.append(str(l1[0]+','+l1[1])+',' +str(l2[0]+',' + l2[1]))
    d[l1[0]+','+l1[1]]=l2[0]+',' + l2[1]

print(l)
print(d)
counter = dict(Counter(d.keys()))
print(counter)
count_times=[]
for i in d.keys():
    count_times.append(list(d.keys()).count(i))

new_dict= dict(zip(l,counter.values()))
print(new_dict)
D_sort = sorted(new_dict.items(), key=lambda item: item[1], reverse=True)

print(D_sort)


#####################################################################
# Tag=[]
# Tag_final = []
# for x, y in zip(pair_t1_tok, pair_t2_new):
#     for i, ii in zip(x,y):
#         Tag.append(i+' '+ii)
#     #Tag.append(nltk.pos_tag(ii))
# Tag_tok = [Tag[i:i + 2] for i in range(0, len(Tag), 2)]
# for ii in Tag_tok:
#     Tag_temp = []
#     for i in ii:
#         ii_tok = word_tokenize(i)
#         Tag_temp.append(ii_tok)
#     Tag_final.append(Tag_temp)
###############################################################
count_times = []
for i in pair_t1_tok:
    count_times.append(pair_t1_tok.count(i))
    m = max(count_times)
    n = count_times.index(m)

index = 0
D_value = {}


for ii in pair_t1_tok:
    print(ii)
    l = []
    for i in ii:
        print(i)
        l.append(i)
    D_value[l[0] + ',' + l[1]] = count_times[index]
    index = index + 1

Value = []
D_sort = sorted(D_value.items(), key=lambda item: item[1], reverse=True)
for value in D_value.values():
    Value.append(value)
##############################################################################


List_lower=[]
for l in pair_t1_tok:
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
Tag_final = []
for x, y in zip(L_novalue, pair_t2_new):
    for i, ii in zip(x,y):
        Tag.append(i+' '+ii)
    #Tag.append(nltk.pos_tag(ii))
Tag_tok = [Tag[i:i + 2] for i in range(0, len(Tag), 2)]
for ii in Tag_tok:
    Tag_temp = []
    for i in ii:
        ii_tok = word_tokenize(i)
        Tag_temp.append(ii_tok)
    Tag_final.append(Tag_temp)

print(Tag)
#Write data into csv file
headers = ['Bigram', 'POS-Tags', 'Gram1', 'Tag1', 'Gram2', 'Tag2', 'Occurrences']
num = 0
rows = []
for iiii in Tag_final:
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
