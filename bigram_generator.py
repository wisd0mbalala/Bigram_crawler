# -*- coding: utf-8 -*-
import nltk, os
from urllib import request
from nltk import *
from nltk.corpus import stopwords
from collections import Counter
import tkinter.messagebox as messagebox


def BigramGenerator(filepath):
	# tkinter.messagebox.showwarning(title='Warning', message='This takes some time, Please be patient! Once it is finished, It will give you a notification!')

	file = open(filepath + '/' + 'no_emptyline.txt', 'rt')
	# file_rawBigrams = open(filepath + '_raw_bigrams.txt', 'w+')
	# file_rawBigrams.truncate()
	file_Bigrams = open(filepath + '/' + 'bigrams.txt', 'w+')
	file_Bigrams.truncate()
	text = file.readlines()
	file.close()

	list_a = []

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
				list_a.append(i)
				file_Bigrams.write(str(i))
				file_Bigrams.write('\n')

	file_Bigrams.close()
	# tkinter.messagebox.showinfo(title='Thanks', message='File Created!')

	# print(list_a)
	# print(len(list_a))

	List = list_a
	# file_rawBigrams.close()

	count_times = []
	for i in List:
		count_times.append(List.count(i))
		m = max(count_times)
		n = count_times.index(m)
	# print(count_times)
	# print(len(count_times))

	'''Dict = {}
	Dict = dict(zip(List,count_times))
	print(Dict)'''

	# L = len(List) - len(count_times)
	# print(L)

	index = 0
	D = {}

	no_dupDict = {}
	no_dup = []
	newList = []

	for ii in List:
		l = []
		for i in ii:
			l.append(i)
		D[l[0] + '-' + l[1]] = count_times[index]
		index = index + 1

	D = sorted(D.items(), key=lambda item: item[1], reverse=True)
	print(D)
	print(len(D))

	L = []
	ind = 0
	for ii in List:
		l = []
		for i in ii:
			l.append(i)
		x = l[0] + ',' + l[1] + ',' + str(count_times[ind])
		if x not in L:
			L.append(x)
		ind += 1

	print(L)
	print(len(L))

	return L , D
