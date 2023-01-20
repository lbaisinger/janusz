from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/base')
def base():
    return render_template('base.html')


@app.route('/')
def bootstrap():
    return render_template('bootstrap.html')


if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'),
            port=int(os.getenv('PORT', 5000)))

