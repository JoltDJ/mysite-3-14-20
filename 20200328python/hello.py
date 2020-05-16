from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    title = 'My Flask Website'
    subtitle = 'The Best Website Ever'
    return render_template('hello.html', mytitle=title, subtitle=subtitle)