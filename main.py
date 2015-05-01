#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import sqlite3
import sys

app = Flask(__name__)

reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

@app.route("/",methods=['GET' , 'POST'])
def main():

    item=20
    the_lang='t_chinese'

    if request.method == 'POST':
        the_lang=request.form['thelang']

    if the_lang == '繁體中文':
        lang='t_chinese'
    elif the_lang == 'English':
        lang='eng'
    elif the_lang == '简体中文':
        lang='s_chinese'
    else:
        lang='t_chinese'

    titles=["" for x in range(item)]
    conn = sqlite3.connect('language.db') # or use :memory: to put it in RAM
    cursor=conn.cursor()
    for idx in range(0, item, 1):
        cmd='select ' + lang +' from language where idx='+ str(idx)
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
        'creative_product' : titles[6],
        'cp_description' : titles[7],
        'perfect_service' : titles[8],
        'ps_description' : titles[9],
        'individual_platform' : titles[10],
        'ip_description' : titles[11],
        'hot_product' : titles[12],
        'last_news' : titles[13],
        'member_zone' : titles[14],
        'login_msg' : titles[15],
        'login' : titles[16],
        'register_acc' : titles[17],
        'community' : titles[18],
        'change_lang' : titles[19]
    }
    return render_template('mayqueen_web/index.html',**templateData)

@app.route("/team")
def team():

    item=6
    the_lang='t_chinese'

    if request.method == 'POST':
        the_lang=request.form['thelang']

    if the_lang == '繁體中文':
        lang='t_chinese'
    elif the_lang == 'English':
        lang='eng'
    elif the_lang == '简体中文':
        lang='s_chinese'
    else:
        lang='t_chinese'

    titles=["" for x in range(item)]
    conn = sqlite3.connect('team.db') # or use :memory: to put it in RAM
    cursor=conn.cursor()
    for idx in range(0, item, 1):
        cmd='select ' + lang +' from team where idx='+ str(idx)
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
    return render_template('mayqueen_web/team.html',**templateData)

@app.route("/support")
def support():

    item=6
    the_lang='t_chinese'

    if request.method == 'POST':
        the_lang=request.form['thelang']

    if the_lang == '繁體中文':
        lang='t_chinese'
    elif the_lang == 'English':
        lang='eng'
    elif the_lang == '简体中文':
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

@app.route("/goods")
def goods():

    item=6
    the_lang='t_chinese'

    if request.method == 'POST':
        the_lang=request.form['thelang']

    if the_lang == '繁體中文':
        lang='t_chinese'
    elif the_lang == 'English':
        lang='eng'
    elif the_lang == '简体中文':
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
    return render_template('mayqueen_web/goods.html',**templateData)

@app.route("/detail")
def goods_detail():

    item=6
    the_lang='t_chinese'

    if request.method == 'POST':
        the_lang=request.form['thelang']

    if the_lang == '繁體中文':
        lang='t_chinese'
    elif the_lang == 'English':
        lang='eng'
    elif the_lang == '简体中文':
        lang='s_chinese'
    else:
        lang='t_chinese'

    titles=["" for x in range(item)]
    conn = sqlite3.connect('goods_detail.db') # or use :memory: to put it in RAM
    cursor=conn.cursor()
    for idx in range(0, item, 1):
        cmd='select ' + lang +' from menu where idx='+ str(idx)
        a = cursor.execute(cmd)
        titles[idx]=str(cursor.fetchone()[0])

    detail_idx = str(request.args)[22]

    cmd='select img from goods_detail where idx=' + detail_idx
    a = cursor.execute(cmd)
    image=str(cursor.fetchone()[0])

    cmd='select spec from goods_detail where idx=' + detail_idx
    a = cursor.execute(cmd)
    spec=str(cursor.fetchone()[0])

    conn.close

    templateData = {
        'home' : titles[0],
        'about_us' : titles[1],
        'product' : titles[2],
        'support' : titles[3],
        'news' : titles[4],
        'contact' : titles[5],
        'image' : image,
        'spec' : spec
    }

    return render_template('mayqueen_web/goods_detail.html',**templateData)

@app.route("/news")
def news():

    item=6
    the_lang='t_chinese'

    if request.method == 'POST':
        the_lang=request.form['thelang']

    if the_lang == '繁體中文':
        lang='t_chinese'
    elif the_lang == 'English':
        lang='eng'
    elif the_lang == '简体中文':
        lang='s_chinese'
    else:
        lang='t_chinese'

    titles=["" for x in range(item)]
    conn = sqlite3.connect('team.db') # or use :memory: to put it in RAM
    cursor=conn.cursor()
    for idx in range(0, item, 1):
        cmd='select ' + lang +' from team where idx='+ str(idx)
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
    return render_template('mayqueen_web/news.html',**templateData)

@app.route("/contact")
def contact():

    item=6
    the_lang='t_chinese'

    if request.method == 'POST':
        the_lang=request.form['thelang']

    if the_lang == '繁體中文':
        lang='t_chinese'
    elif the_lang == 'English':
        lang='eng'
    elif the_lang == '简体中文':
        lang='s_chinese'
    else:
        lang='t_chinese'

    titles=["" for x in range(item)]
    conn = sqlite3.connect('team.db') # or use :memory: to put it in RAM
    cursor=conn.cursor()
    for idx in range(0, item, 1):
        cmd='select ' + lang +' from team where idx='+ str(idx)
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
    return render_template('mayqueen_web/contact1.html',**templateData)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
