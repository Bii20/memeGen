from flask import Flask


app = Flask(__name__)

@app.route('/')
def Home():
    return'hello joker'


@app.route('/home')
def home():
    return'hello homie'

@app.route('/home/v1')
def home():
    return'hello to me'



if __name__ == '__main__':

    app.run(host='0.0.0',port=5001,debug=True)    