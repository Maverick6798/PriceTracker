from flask import Flask, render_template,request
from Amazon_Tracker import Tracker

url = "https://www.amazon.in/Wings-Wireless-Bluetooth-Earphones-Controls/dp/B08T96R3XJ/ref=sr_1_2?keywords=wings+phantom&qid=1645202890&sprefix=wings+%2Caps%2C261&sr=8-2"
track=Tracker(url)
name=track.track()
print(name)
app= Flask(__name__)
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/predict")
def predict():
    print(name)
    try:
        return render_template('predict.html',name=track.track(),price=track.track())            
    except ValueError:
        return "Please check if the values are entered correctly!"



if __name__=='__main__':
    app.run()

