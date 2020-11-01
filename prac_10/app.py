from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello World :) </h1>'

@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=''):
    return 'hello {}'.format(name)

@app.route('/f')
@app.route('/f/<input_value>')
def f(input_value=0):
    celsius = float(input_value)
    result = celsius * 9.0 / 5 + 32
    return '{}'.format(result)


if __name__ == '__main__':
    app.run()
