from flask import Flask

app = Flask(__name__)

@app.route('/')  #on hitting "/", the following function will execute
def welcome():
    return "Hello World"



if __name__ == "__main__":
    app.run(debug = True)      #no need to rerun app.py