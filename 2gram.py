# -*- coding: utf-8 -*-
import re, nltk, pprint, random, sys, os
from urllib import request
from nltk import *
from text_cleaner import *
from bigram_generator import BigramGenerator

# raw text from online
#url = "http://www.gutenberg.org/files/2554/2554-0.txt"
#path = '/Users/Lingzhi/Documents'

# raw text from local
#path = nltk.data.find('/Users/Lingzhi/Documents/gutenberg_short.txt')

# choose between online and local text, 1 for online, 2 for local

loc_web = input("Do you want to give a text from Local or from the Web? \n1 for a local file. \n2 for a file from the Web.\n3 for Abortion.\n")
while loc_web != 1 or 2 or 3:
    if loc_web == "1":
        dir = input("Please provide me the directory of the raw text file\n(For Example: \nC:/Users/ncllz/Documents/project/ with WIN OS\n/Users/Lingzhi/Documents/ with MAC OS):")
        filename = input("Please provide me the file name of the raw text(For Example: gutenberg_short.txt):")
        filepath = os.path.join(dir, filename)
        No_EmptyLine_Local(filepath)
        BigramGenerator(filepath)
        break

    elif loc_web == "2":
        url = input("Please provide me the URL link to the raw text(with an extra space before you press ENTER)\n Example URL: http://www.gutenberg.org/files/2554/2554-0.txt :")
        filepath = input("Please provide me the path you want to store the cleaned file:\n(For Example: \nC:/Users/ncllz/Documents/project/ with WIN OS\n/Users/Lingzhi/Documents/ with MAC OS):")
        No_EmptyLine_Web(url,filepath)
        BigramGenerator(filepath)

        break
    elif loc_web == "3":
        break

    else:
        print("The information you provide is invalid! Please have a check and give it agian.\n")
        loc_web = input("Do you want to give a text from Local or from the Web? \n1 for a local file. \n2 for a file from the Web.\n3 for Abortion.\n")
        if loc_web == "1":
            dir = input("Please provide me the directory of the raw text file\n(For Example: \nC:/Users/ncllz/Documents/project/ with WIN OS\n/Users/Lingzhi/Documents/ with MAC OS):")
            filename = input("Please provide me the file name of the raw text(For Example: gutenberg_short.txt):")
            filepath = os.path.join(dir, filename)
            No_EmptyLine_Local(filepath)
            BigramGenerator(filepath)

            break

        elif loc_web == "2":
            url = input("Please provide me the URL link to the raw text(with an extra space before you press ENTER)\n Example URL: http://www.gutenberg.org/files/2554/2554-0.txt :")
            filepath = input("Please provide me the path you want to store the cleaned file:\n(For Example: \nC:/Users/ncllz/Documents/project/ with WIN OS\n/Users/Lingzhi/Documents/ with MAC OS):")
            BigramGenerator(filepath)
            break

        elif loc_web == "3":
            break