from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/curriculum')
def cv():
    return "belum ada"

if __name__ == "__main__":
    app.run(debug=1)

