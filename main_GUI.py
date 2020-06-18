# -*- coding: utf-8 -*-

import os.path
import tkinter as tk
from tkinter import *
import tkinter.messagebox as messagebox
from tkinter import filedialog
from nltk import *
from urllib import request
from bigram_generator import BigramGenerator


def createpage(master):
    def selectPath():
        path_ = filedialog.askdirectory()
        path.set(path_)

    path = StringVar()  # give the link to the string value

    # Local Text Submission
    def local_submission():

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

        filename = StringVar()

        Label(window_local, text="Select your txt file:").place(x=20, y=120)
        Entry(window_local, textvariable=filename).place(x=230, y=120)
        Button(window_local, text="Select and Submit", command=opentxt).place(x=400, y=120)

    # URL Link Submission
    def url_submisson():

        def confirm_submission():
            url_link = url.get()
            response = request.urlopen(url_link)
            file = response.read().decode('utf8')

            tkinter.messagebox.showinfo(title='Thanks', message='Your URL Link is received!')
            cleantext(path, file)
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

        url = tk.StringVar()  # give the link to the string value
        url.set('http://www.gutenberg.org/files/2554/2554-0.txt')

        Label(window_link, text='URL Link: ').place(x=10, y=130)
        Entry(window_link, textvariable=url, width=40).place(x=230, y=130)
        Button(window_link, text="Submit", command=confirm_submission).place(x=550, y=130)

    master = Frame(root)
    master.pack()

    Label(master, text="1.Select your Target Directory:").grid(row=0, column=0, stick=W, pady=10)
    e1 = Entry(master, textvariable=path, width=30)
    e1.grid(row=0, column=1, stick=W)
    Button(master, text="Select Directory", command=selectPath).grid(row=0, column=4,stick=E)

    Label(master, text="2.Choose your way to upload the text:").grid(row=1, column=0, stick=W, pady=10)
    Button(master,text='Local File', command = local_submission).grid(row=1, column=3, stick=E)
    Button(master,text='URL Link', command = url_submisson).grid(row=1, column=4, stick=E)

    Label(master, text="3.Crawl and store bigrams:").grid(row=2, column=0, stick=W, pady=10)
    # Button传递参数
    Button(master,text='Crawl Bigrams', command=lambda: BigramGenerator(e1.get())).grid(row=2, column=4, stick=E)




if __name__ == '__main__':
    root = Tk()
    root.title('BigramCrawler')
    root.geometry('630x550')
    # wellcome image
    canvas = tk.Canvas(root, width=600, height=300, bg='green')
    image_file = tk.PhotoImage(file='bigram.png')
    image = canvas.create_image(200, 0, anchor='n', image=image_file)
    canvas.pack(side='top')
    tk.Label(root,
             text='Hi！This is a Bigram Crawler. \nI can extract bigrams from English texts.',
             font=('Arial', 16)).pack()
    createpage(root)

    root.mainloop()
