#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from urllib import request
from nltk import *


# Local Text Submission
def opentxt():
    filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
    filepath = filename
    file = open(filepath, 'r')
    file = file.read()
    file_i = str(file)
    return file_i


# URL Link Submission
def url_submisson():
    def confirm_submission():
        url_link = url.get()
        response = request.urlopen(url_link)
        file = response.read().decode('utf8')

        tkinter.messagebox.showinfo(title='Thanks', message='Your URL Link is received!')
        # Close toplevel window
        window_link.destroy()
        print(file)
        return file

    # TopLevel Window
    window_link = tk.Toplevel(root)
    window_link.geometry('420x200')
    window_link.title('URL Link')

    url = tk.StringVar()  # give the link to the string value
    url.set('http://www.gutenberg.org/files/2554/2554-0.txt')
    tk.Label(window_link, text='URL Link: ').place(x=10, y=50)
    link = tk.Entry(window_link, textvariable=url, width=40)
    link.place(x=130, y=50)

    # comfirm_submission button
    comfirm_submission = tk.Button(window_link, text='Submit', command=confirm_submission)
    comfirm_submission.place(x=180, y=120)


def selectPath():
    path_ = filedialog.askdirectory()
    path.set(path_)


def cleantext(path, file):
    file_to_open = os.path.join(path.get(), "no_emptyline.txt")
    fnew = open(file_to_open, 'w+')
    fnew.truncate()  # clear the content of new file
    raw = file.replace('\n', ' ')
    print(raw)
    text = raw.lower()
    print(text)
    sentences = sent_tokenize(text)
    print(sentences)
    for sentence in sentences:
        lines = re.split('\n+', sentence)  # exclude extra empty lines
        print(lines)
        for line in lines:
            newline = ' '.join(line.split())  # exclude extra spaces
            print(newline)
            fnew.write(newline)
            fnew.write('\n')
    fnew.close()


# object the window
root = tk.Tk()

root.title('BigramCrawler')

# diameter of the window
root.geometry('400x400')

# wellcome image
canvas = tk.Canvas(root, width=400, height=135, bg='green')
image_file = tk.PhotoImage(file='bigram.png')
image = canvas.create_image(200, 0, anchor='n', image=image_file)
canvas.pack(side='top')
tk.Label(root,
         text='Hi！This is the Bigram Crawler. \nWe can extract bigrams from English texts.\n You can either select a txt file from local,\n or give us url link to a txt file.',
         font=('Arial', 16)).pack()

path = StringVar()
folder = StringVar()
file_i = ''

# object the buttons
local_txt = tk.Button(root, text='Local File', command=opentxt)
local_txt.place(x=70, y=300)
url_link = tk.Button(root, text='URL Link', command=url_submisson)
url_link.place(x=200, y=300)
target_path = tk.Button(root, text='Target Directory', command=selectPath)
target_path.place(x=70, y=350)
clean_file = tk.Button(root, text='Clean the Text', command=cleantext(path, file_i))
clean_file.place(x=200, y=350)

# Mainloop of the window
root.mainloop()
