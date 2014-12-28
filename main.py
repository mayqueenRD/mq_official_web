#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('mayqueen_web/index.html')

@app.route("/team")
def mobile():
    return render_template('mayqueen_web/team.html')

@app.route("/news")
def news():
    return render_template('mayqueen_web/news.html')

@app.route("/contact")
def contact():
    return render_template('mayqueen_web/contact1.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
