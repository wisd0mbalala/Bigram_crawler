# -*- coding: utf-8 -*-
import nltk, os
from urllib import request
from nltk import *


def cleantext(path, file):
    fnew = open(path + '/' + 'no_emptyline.txt', 'w+')
    fnew.truncate()  # clear the content of new file
    raw = file.replace('\n', ' ')
    #text = raw.lower()
    sentences = sent_tokenize(raw)
    for sentence in sentences:
        lines = re.split('\n+', sentence)  # exclude extra empty lines
        for line in lines:
            newline = ' '.join(line.split())  # exclude extra spaces
            fnew.write(newline)
            fnew.write('\n')
    fnew.close()


def No_EmptyLine_Local(filepath):
    file = open(filepath, 'r')
    fnew = open(filepath + '_no_emptyline.txt', 'w+')
    fnew.truncate()  # clear the content of new file
    raw2 = file.read()
    raw = raw2.replace('\n', ' ')
    file.close()
    text = raw.lower()
    sentences = sent_tokenize(text)

    for sentence in sentences:
        lines = re.split('\n+', sentence)  # exclude extra empty lines
        for line in lines:
            newline = ' '.join(line.split())  # exclude extra spaces
            fnew.write(newline)
            fnew.write('\n')
    fnew.close()


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print
        u"file path is required, please check your path!"
    else:
        No_EmptyLine_Local(sys.argv[1])


def No_EmptyLine_Web(url, path):
    response = request.urlopen(url)
    file = response.read().decode('utf8')
    fnew = open(path + '/' + '_no_emptyline.txt', 'w+')
    fnew.truncate()  # clear the content of new file

    raw = file.replace('\n', ' ')

    text = raw.lower()
    sentences = sent_tokenize(text)

    for sentence in sentences:
        lines = re.split('\n+', sentence)  # exclude extra empty lines
        for line in lines:
            newline = ' '.join(line.split())  # exclude extra spaces
            fnew.write(newline)
            fnew.write('\n')
    fnew.close()


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print
        u"file path is required, please check your path!"
    else:
        No_EmptyLine_Local(sys.argv[2])
