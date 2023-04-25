from flask import Flask


app = Flask(__name__)

@app.route('/')  #This is mainpage
def hello():
    return "Hello World from Flask"

@app.route('/second')  #This is second page, 127.0.0.1:5000/second
def second():
    return "This is second page"

@app.route('/third/subthird')  
def third():
    return "This is subpage of thirdpage" #http://127.0.0.1:5000/third/subthird

@app.route('/forth/<string:id>')  #http://127.0.0.1:5000/forth/11681168
def forth(id):
    return f'Id number of this page is : {id}'


if __name__ == '__main__':  # here we define on which port it works! (debug=True, port:5000 or can be any other)
    app.run(debug=True)