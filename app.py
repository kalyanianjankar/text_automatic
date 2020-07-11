from flask import Flask, Response, render_template,request,url_for
import json

import sys
sys.path.append('//C://Users//ASHISH//Example//example1//virtual//Lib//site-packages//flask_wtf')
from flask_wtf import Form

from wtforms import TextField, BooleanField


app=Flask(__name__)

class SearchForm(Form):
	autocomp =TextField('Insert City',id='city_autocomplete')
import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/_autocomplete',methods=['GET'])
def autocomplete():
	cities=["Spain","Aachen","Germany","Aalborg","Denmark","Abbotabad","Calangute",	"Calicut",	"Campirganj",	"Canacona", "Chaba",	"Chabbewal",
	"Dabani","	Dabhadi",	"Dabhoi","Jabal",	"Jabalpur","K.Paramathi",	"Kaas Plateau","Zadkala",	"Zaheerabad"]
	print(cities)
	return Response(json.dumps(cities),mimetype='application/json')

@app.route('/',methods=['GET','POST'])	

def index():
	form = SearchForm(request.form)
	return render_template("index.html",form=form)

if __name__ == '__main__':
	app.run(debug=True)