from flask import Flask, url_for, render_template, request, Markup, flash
import os, json, random
app = Flask(__name__)

with open('skyscrapers.json') as skyscrapers_data:
       buildings = json.load(skyscrapers_data)
        
@app.route("/home")
def render_main():
    return render_template('info.html')

@app.route("/data")
def render_second():
    return render_template('DataBySkyscraper.html')

@app.route("/amount")
def render_third():
    return render_template('AmountOfSkyscrapers.html')
    
if __name__=="__main__":
    app.run(debug=True, port=54321)
