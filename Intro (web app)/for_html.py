#integrating HTML
# GET and POST

from flask import Flask, redirect, url_for, render_template


app = Flask(__name__)


@app.route('/')
def welcome():
   return render_template('index.html')  #need to make a "templates" folder


@app.route('/success/<int:score>')   #score is an integer value
def success(score):
    return "The person has passed and the marks are"  + str(score)


@app.route('/fail/<int:score>')   #score is an integer value
def fail(score):
    return "The person has failed and the marks are"  + str(score)


#------result checker-----#
@app.route('/results/<int:marks>')
def results(marks):
    result = ""
    if marks<50:
        result = "fail"
    else:
        result= "success"

    return redirect(url_for(result,score= marks))


if __name__ == "__main__":
    app.run(debug =True)