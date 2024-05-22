from flask import Flask


app = Flask(__name__)

@app.route('/')
def Home():
    return'hello joker'


@app.route('/home')
def home():
    return'hello homie'



if __name__ == '__main__':

    app.run(host='0.0.0',port=5001,debug=True)    