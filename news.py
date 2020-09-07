# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 00:25:02 2020

@author: Minoru Otsuka
"""

import feedparser
import tkinter
import webbrowser

#------------------------------------------------
#RSSメイン処理関数
#------------------------------------------------
def rss_main():
    global news_text, f1
    global d, index, news_site, news_site_index, scroll_index, news_title, line_width
    
    if (scroll_index == 0):    
        if (index < 0):
            #初回のみの処理
            index = 0
        else:
            #2回目以降の処理
            index = index + 1
            if (index == len(d.entries)):
                index = 0
        
        if (index == 0):  
            d = feedparser.parse(news_site[news_site_index])
            news_site_index += 1
            if (news_site_index == len(news_site)):
                news_site_index = 0
            
        news_title = "◇" + d["feed"]["title"] + "◇" + d.entries[index].title + "　"*int(line_width/2)

    news_text.set(news_title[0:scroll_index+1])

    scroll_index += 1
    if (scroll_index == len(news_title)):
        scroll_index = 0
        
    f1.after(500, rss_main)

#------------------------------------------------
#クリック時の処理
#------------------------------------------------
def open_news(ev):
    global d, index

    webbrowser.open(d.entries[index].link)    
    
#------------------------------------------------
#メイン関数
#------------------------------------------------
def main():
    global news_text, f1
    global index, news_site, news_site_index, scroll_index, line_width
    
    #RSS URLの読み込み
    f = open("site_list.txt","r")
    news_site = f.readlines()
    f.close()
    
    #変数初期化
    index = -1
    news_site_index = 0
    scroll_index = 0
    
    line_width = 24 #表示文字数(半角)
    
    #ウィンドウ作成
    w = tkinter.Tk()
    w.title("新幹線ニュース")
    
    news_text = tkinter.StringVar()
    
    f1 = tkinter.Frame(w)
    
    img = tkinter.PhotoImage(file="back.png")
    bg = tkinter.Label(f1, image=img)
    bg.pack()
   
    screen = tkinter.Label(f1, textvariable=news_text, anchor="e", width=line_width, fg="yellow", bg="black", font=("ＭＳ ゴシック",20))
    screen.bind("<Button-1>", open_news)
    screen.place(relx=0.203, rely=0.212)

    f1.pack()

    f1.after(0, rss_main)
    f1.mainloop()

main()
