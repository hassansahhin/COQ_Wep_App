import pickle
from flask import Flask , render_template , url_for
from flask_ngrok import run_with_ngrok



#load the dictionary
with open('data.pickle', 'rb') as handle:
  data = pickle.load(handle)


#intialize the App
app=Flask(__name__,template_folder='templates' ,static_folder='static')
run_with_ngrok(app)


#routs
@app.route("/")
@app.route("/home")
def home():
  return render_template("home.html" ,title = "home" ,data =data)

@app.route("/BSC")
def BSC():
  return render_template("BSC.html" , title = "BSC" , data =data)

@app.route("/quality")
def quality():
  return render_template("quality.html" , title = "quality" , data =data)

@app.route("/faisal")
def faisal():
  return render_template("faisal.html" , title = "faisal" ,  data =data)

@app.route("/nbe")
def nbe():
  return render_template("nbe.html" , title = "nbe" ,  data =data)

@app.route("/qnb")
def qnb():
  return render_template("qnb.html" , title = "qnb" ,  data =data)

@app.route("/japan")
def japan():
  return render_template("japan.html" , title = "japan" , data =data)


@app.route("/ld07")
def ld07():
  return render_template("ld07.html" , title = "ld07" , data =data)

@app.route("/ld04")
def ld04():
  return render_template("ld04.html" , title = "ld04" ,  data =data)

@app.route("/cbd")
def cbd():
  return render_template("cbd.html" , title = "cbd" ,  data =data)
  
if __name__ == "__main__":
  app.run()

