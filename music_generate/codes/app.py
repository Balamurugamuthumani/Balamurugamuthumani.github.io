# -*- coding: utf-8 -*-

from flask import Flask,render_template,request
import melodygenerator as mgg

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        print("POST RECIEVED!!!!")
    
    return render_template("index.html",)

@app.route("/predict",methods=["GET","POST"])
def predict():
    mg = mgg.MelodyGenerator()
    #seed ="67 _ 65 _ _ _ 60 _ _ _ _ _ 62 _ 64"
    if request.method == 'POST':
        seed = request.form['seed']
        melody = mg.generate_melody(seed, 500, mgg.SEQUENCE_LENGTH,0.8)
        mg.save_melody(melody)
        
    return render_template('index.html', prediction_text='Your composition is ready {}!'.format(melody))


if __name__=="__main__":
    
    app.run(debug="True",threaded="True",port=4455)       