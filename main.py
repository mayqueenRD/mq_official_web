#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, session
import sqlite3
import sys
import subprocess

app = Flask(__name__)
app.config['SECRET_KEY'] = 'F34TF$($e34D';
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

@app.route("/",methods=['GET' , 'POST'])
def main():
    return render_template('mayqueen_web/index.html')

@app.route("/team")
def team():
    return render_template('mayqueen_web/team.html')

@app.route("/support")
def support():

    item=6

    if  session['thelang']== '繁體中文':
        lang='t_chinese'
    elif session['thelang'] == 'English':
        lang='eng'
    elif session['thelang'] == '简体中文':
        lang='s_chinese'
    else:
        lang='t_chinese'

    titles=["" for x in range(item)]
    conn = sqlite3.connect('menu.db') # or use :memory: to put it in RAM
    cursor=conn.cursor()
    for idx in range(0, item, 1):
        cmd='select ' + lang +' from menu where idx='+ str(idx)
        a = cursor.execute(cmd)
        titles[idx]=str(cursor.fetchone()[0])

    conn.close

    templateData = {
        'home' : titles[0],
        'about_us' : titles[1],
        'product' : titles[2],
        'support' : titles[3],
        'news' : titles[4],
        'contact' : titles[5],
    }
    return render_template('mayqueen_web/support.html',**templateData)


@app.route("/contact")
def contact():
    return render_template('mayqueen_web/contact1.html')


@app.route("/minipc")
def minipc():
    return render_template('mayqueen_web/minipc.html')

@app.route("/dashcam")
def dashcam():
    return render_template('mayqueen_web/dashcam.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
