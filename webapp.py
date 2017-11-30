from flask import Flask, url_for, render_template, request, Markup, flash
import os, json, random
app = Flask(__name__)

with open('skyscrapers.json') as skyscrapers_data:
       buildings = json.load(skyscrapers_data)




@app.route("/")
def render_main():
    return render_template('info.html')

@app.route("/data")
def render_second():
    state = request.args["city"]
    return render_template('DataBySkyscraper.html', options = get_city_options(),response = your_interesting_function(state))       
    

@app.route("/amount")
def render_third():
    return render_template('AmountOfSkyscrapers.html')
    
def get_city_options():
        
    options = ""
    city = ""
    for c in skyscrapers:
        if not c["location"]["city"] == city:
            options += Markup("<option value=\"" + c["location"]["city"] + "\">" + c["location"]["city"] + "</option>")
            city = c["location"]["city"]
    
    return options

def your_interesting_function(stateName):
    count = 0
    while not counties[count]["location"]["city"] == stateName:
        count += 1
           
    city = counties[count]["location"]["city"]
    skyscraper = counties[count]["name"]
    word = "is made out of:"
    material = counties[count]["material"]
    return city + ": " + str(skyscraper) + ": " + word + str(material)
if __name__=="__main__":
    app.run(debug=True)
