from flask import Flask, render_template

app = Flask(__name__)

@app.route('/teste')
def teste():
    pass

@app.route('/')
def home():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True, host='192.168.1.16', port=8501)