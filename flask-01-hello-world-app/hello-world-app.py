from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World from Flask"

@app.route('/second')
def second():
    return "Hello World that's the second"

@app.route('/third/subthird')
def third():
    return "Hello World that's the sub_page of the third page"


@app.route('/forth/<string:id>')
def forth(id):
    return f'Id number of this page is : {id}'



if __name__ == '__main__':
    app.run(debug=True, port=3000)
