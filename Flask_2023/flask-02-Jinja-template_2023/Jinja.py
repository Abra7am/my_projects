from flask import Flask, render_template    

app= Flask(__name__)


@app.route('/')
def head():
    return render_template('index.html', number1 = 10, number2 = 50)


@app.route('/mult')
def number():
    var1, var2 = 20, 30
    return render_template ('body.html', num1=var1, num2=var2, multiplication= var1*var2)
# here page multiplies! (http://127.0.0.1:3000/mult)



if __name__ == '__main__':
    app.run(debug=True, port=3000)