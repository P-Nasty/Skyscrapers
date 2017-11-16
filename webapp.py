from flask import Flask, url_for, render_template, request, Markup, flash
import os, json, random
app = Flask(__name__)

with open('skyscrapers.json') as skyscrapers_data:
       buildings = json.load(skyscrapers_data)
        
@app.route("/")
def render_main():
    return render_template('info.html')

if __name__=="__main__":
    app.run(debug=False, port=54321)
