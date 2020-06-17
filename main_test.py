#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from urllib import request
from nltk import *
from bigram_generator import BigramGenerator
target_directory = {}

# Local Text Submission
def local_submission():
    def selectPath():
        path_ = filedialog.askdirectory()
        path.set(path_)
        target_directory[0]=path.get()
        print(target_directory[0])
    def opentxt():
        file = filedialog.askopenfilename(initialdir="/", title="Select file",
                                              filetypes=(("txt files", "*.txt"), ("all files", "*.*")))

        file_ = open(file, 'r')
        txtfile = file_.read()
        filename.set(file)
        cleantext(path, txtfile)
        tkinter.messagebox.showinfo('Tipps', 'File Created!')
        window_local.destroy()

    def cleantext(path, file):
        file_to_open = os.path.join(path.get(), "no_emptyline.txt")
        fnew = open(file_to_open, 'w')
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


    # TopLevel Window
    window_local = tk.Toplevel(root)
    window_local.geometry('550x200')
    window_local.title('Local File')

    path = StringVar()  # give the link to the string value
    filename = StringVar()

    Label(window_local, text="Target Directory to store the file:").place(x=20, y=50)
    Entry(window_local, textvariable=path).place(x=230, y=50)
    Button(window_local, text="Select your Directory", command=selectPath).place(x=400, y=50)

    Label(window_local, text="Select your txt file:").place(x=20, y=120)
    Entry(window_local, textvariable=filename).place(x=230, y=120)
    Button(window_local, text="Select and Submit", command=opentxt).place(x=400, y=120)



# URL Link Submission
def url_submisson():
    def selectPath():
        path_ = filedialog.askdirectory()
        path.set(path_)
        target_directory[0]=path.get()
        print(target_directory[0])
    def confirm_submission():
        url_link = url.get()
        response = request.urlopen(url_link)
        file = response.read().decode('utf8')

        tkinter.messagebox.showinfo(title='Thanks', message='Your URL Link is received!')
        cleantext(path,file)
        # Close toplevel window
        window_link.destroy()

    def cleantext(path, file):
        file_to_open = os.path.join(path.get(), "no_emptyline.txt")
        fnew = open(file_to_open, 'w')
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

    # TopLevel Window
    window_link = tk.Toplevel(root)
    window_link.geometry('650x200')
    window_link.title('URL Link')

    path = StringVar()
    url = tk.StringVar()  # give the link to the string value
    url.set('http://www.gutenberg.org/files/2554/2554-0.txt')

    Label(window_link, text="Target Directory to store the file:").place(x=10, y=50)
    Entry(window_link, textvariable=path).place(x=230, y=50)
    Button(window_link, text="Select your Directory", command=selectPath).place(x=500, y=50)

    Label(window_link, text='URL Link: ').place(x=10, y=130)
    Entry(window_link, textvariable=url, width=40).place(x=230, y=130)
    Button(window_link, text="Submit", command=confirm_submission).place(x=550, y=130)









# object the window
root = tk.Tk()

root.title('BigramCrawler')

# diameter of the window
root.geometry('600x550')




# wellcome image
canvas = tk.Canvas(root, width=600, height=300, bg='green')
image_file = tk.PhotoImage(file='bigram.png')
image = canvas.create_image(200, 0, anchor='n', image=image_file)
canvas.pack(side='top')
tk.Label(root,
         text='Hi！This is the Bigram Crawler. \nWe can extract bigrams from English texts.\n You can either select a '
              'txt file from local,\n or give us URL link to a txt file.',
         font=('Arial', 16)).pack()



# object the buttons
Label(root, text="Choose your way to provide the text:",
         font=('Arial', 12)).place(x=20, y=420)
local_txt = tk.Button(root, text='Local File', command=local_submission)
local_txt.place(x=330, y=418)
url_link = tk.Button(root, text='URL Link', command=url_submisson)
url_link.place(x=430, y=418)

'''Label(root, text="Bigram Crawling and Storing:",
         font=('Arial', 12)).place(x=20, y=450)
bigram_crawl = tk.Button(root, text='Crawl Bigrams', command=BigramGenerator(set(target_directory[0])))
bigram_crawl.place(x=330, y=448)'''

# Mainloop of the window
root.mainloop()
