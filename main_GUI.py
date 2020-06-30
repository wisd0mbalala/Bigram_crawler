# -*- coding: utf-8 -*-

import os.path
import tkinter as tk
from tkinter import *
import tkinter.messagebox as messagebox
from tkinter import filedialog
from nltk import *
from urllib import request
from bigram_generator import BigramGenerator
from bigram_crawler import bigrams_to_csv
from bigram_crawler_with_NER import bigrams_with_ner_to_csv
from tkinter import ttk
from freqCal import sortFreq


def createpage(master):
    def selectPath():
        path_ = filedialog.askdirectory()
        path.set(path_)

    path = StringVar()  # give the link to the string value

    # Local Text Submission subwindow
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
            #raw = raw.lower()
            sentences = sent_tokenize(raw)
            for sentence in sentences:
                lines = re.split('\n+', sentence)  # exclude extra empty lines
                for line in lines:
                    newline = ' '.join(line.split())  # exclude extra spaces
                    fnew.write(newline)
                    fnew.write('\n')
            fnew.close()

        # TopLevel Window
        window_local = tk.Toplevel(root)
        window_local.geometry('500x50')
        window_local.title('Local File')

        filename = StringVar()

        Label(window_local, text="Select your txt file:").grid(row=0, column=0, stick=W)
        Entry(window_local, textvariable=filename).grid(row=0, column=1, stick=W)
        ttk.Button(window_local, text="Select and Submit", command=opentxt).grid(row=0, column=3, stick=E)

    # URL Link Submission subwindow
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
            #raw = raw.lower()
            sentences = sent_tokenize(raw)
            for sentence in sentences:
                lines = re.split('\n+', sentence)  # exclude extra empty lines
                for line in lines:
                    newline = ' '.join(line.split())  # exclude extra spaces
                    fnew.write(newline)
                    fnew.write('\n')
            fnew.close()

        # TopLevel Window
        window_link = tk.Toplevel(root)
        window_link.geometry('600x50')
        window_link.title('URL Link')

        url = tk.StringVar()  # give the link to the string value
        url.set('http://www.gutenberg.org/files/2554/2554-0.txt')

        Label(window_link, text='URL Link: ').grid(row=0, column=0, stick=W)
        Entry(window_link, textvariable=url, width=40).grid(row=0, column=1, stick=W)
        ttk.Button(window_link, text="Submit", command=confirm_submission).grid(row=0, column=3, stick=E)

    def POS_Freq():

        def freqpresent():
            s = sortFreq(e1.get())
            for key,value in s.items():
                lstbox1.insert(lstbox1.size(), key, value)

        def clear():
            lstbox1.delete(0, END)

        # TopLevel Window
        window_freq = tk.Toplevel(root)
        window_freq.geometry('300x250')
        window_freq.title('POS Tag Frequency')

        frame1 = Frame(window_freq, relief=RAISED)
        frame1.place(relx=0.0)
        frame2 = Frame(window_freq, relief=GROOVE)
        frame2.place(relx=0.5)
        lstbox1 = Listbox(frame1)
        lstbox1.pack()
        btn1 = Button(frame2, text="Calculate", command=freqpresent)
        btn1.pack(fill=X)
        btn2 = Button(frame2, text="Clear", command=clear)
        btn2.pack(fill=X)

    master = Frame(root)
    master.pack()

    Label(master, text="1.Select your Target Directory:").grid(row=0, column=0, stick=W, pady=10)
    e1 = Entry(master, textvariable=path, width=30)
    e1.grid(row=0, column=1, stick=W)
    ttk.Button(master, text="Select Directory", command=selectPath).grid(row=0, column=2, stick=E)

    Label(master, text="2.Choose your way to upload the text:").grid(row=1, column=0, stick=W, pady=10)
    ttk.Button(master, text='Local File', command=local_submission).grid(row=1, column=1, stick=E)
    ttk.Button(master, text='URL Link', command=url_submisson).grid(row=1, column=2, stick=E)

    Label(master, text="3.Crawl and store bigrams with or without Named Entities Recognition:").grid(row=2, column=0, stick=W, pady=10)
    # Button传递参数
    ttk.Button(master, text='Crawl Bigrams without NER', command=lambda: bigrams_to_csv(e1.get())).grid(row=2, column=1, stick=E)
    ttk.Button(master, text='Crawl Bigrams with NER', command=lambda: bigrams_with_ner_to_csv(e1.get())).grid(row=2, column=2, stick=E)

    Label(master, text="4.Present Frequencies of the Each POS Tag:").grid(row=3, column=0, stick=W, pady=10)
    ttk.Button(master, text='Present Frequency', command=POS_Freq).grid(row=3, column=2, stick=E)


if __name__ == '__main__':
    root = Tk()
    root.title('BigramCrawler')
    root.geometry('800x550')
    # wellcome image
    canvas = tk.Canvas(root, width=800, height=300, bg='green')
    image_file = tk.PhotoImage(file='bigram.gif')
    image = canvas.create_image(400, 0, anchor='n', image=image_file)
    canvas.pack(side='top')
    tk.Label(root,
             text='Hi！This is a Bigram Crawler. \n Remember to Select Your Target Directory First!!!',
             font=('Arial', 16)).pack()
    createpage(root)

    root.mainloop()
