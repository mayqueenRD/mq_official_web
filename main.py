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

    ip=request.remote_addr
    proc = subprocess.Popen(["date >> record ", ""], stdout=subprocess.PIPE, shell=True)
    proc.communicate()
    proc = subprocess.Popen(["echo '%s' >> record " % ip, ""], stdout=subprocess.PIPE, shell=True)
    proc.communicate()

    return render_template('mayqueen_web/index.html')

@app.route("/products")
def products():

    return render_template('mayqueen_web/products.html')

@app.route("/about")
def about():

    return render_template('mayqueen_web/about.html')


@app.route("/product_info")
def product_info():

    total=17

    titles=["" for x in range(total)]
    spec=["" for x in range(total)]

    conn = sqlite3.connect('products.db') # or use :memory: to put it in RAM
    cursor=conn.cursor()
    for idx in range(0, total, 1):
        detail_idx = str(request.args)[22] + str(request.args)[23] + str(request.args)[24] + str(request.args)[25] + str(request.args)[26]

        cmd='select ' + detail_idx +' from products where idx='+ str(idx)
        b = cursor.execute(cmd)
        spec[idx]=str(cursor.fetchone()[0])

    conn.close

    templateData = {
        'part_number' : spec[0],
        'technology' : spec[1],
        'processor' : spec[2],
        'gpu' : spec[3],
        'storage' : spec[4],
        'network' : spec[5],
        'bluetooth' : spec[6],
        'display' : spec[7],
        'audio' : spec[8],
        'usb' : spec[9],
        'uart' : spec[10],
        'spi' : spec[11],
        'gpio' : spec[12],
        'i2c' : spec[13],
        'case' : spec[14],
        'dimensions' : spec[15],
        'memory' : spec[16]
    }
    return render_template('mayqueen_web/product_info.html',**templateData)

@app.route("/download_minipc")
def download_minipc():

    return render_template('mayqueen_web/download_minipc.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
