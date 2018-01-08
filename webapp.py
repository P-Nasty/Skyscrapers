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
    try:
        name = request.args["name"]
        return render_template('DataBySkyscraper.html', options = get_name_options(),response = your_interesting_function(name))       
    except:
        return render_template('DataBySkyscraper.html', options = get_name_options())     
 

@app.route("/amount")
def render_third():
    try:
        name = request.args["city"]
        return render_template('AmountOfSkyscrapers.html', options1 = get_city_options(),response1 = your_interesting_function1(name))       
    except:
        return render_template('AmountOfSkyscrapers.html', options1 = get_city_options())   

def get_name_options():
        
    options = ""
    name = ""
    for c in buildings:
        if not c["name"] == name:
            options += Markup("<option value=\"" + c["name"] + "\">" + c["name"] + "</option>")
            name = c["name"]
    return options

def your_interesting_function(name):
    count = 0
    while not buildings[count]["name"] == name:
        count += 1
           
    city = buildings[count]["location"]["city"]
    skyscraper = buildings[count]["name"]
    word = "is made out of:"
    material = buildings[count]["material"]
    return city + ": " + skyscraper + ": " + word + material
    
    
def get_city_options():
        
    options = ""
    cities = []
    for c in buildings:
        if c["location"]["city"] not in cities:
            cities.append(c["location"]["city"])
            options += Markup("<option value=\"" + c["location"]["city"] + "\">" + c["location"]["city"] + "</option>")
          
    
    return options

def your_interesting_function1(name):
    counter = 0
    for a in buildings:
        if name == a["location"]["city"]:
            counter += 1
    return "there are " + str(counter) + " skyscrapers in " + name       
  
    
    
if __name__=="__main__":
    app.run(debug=True)  
