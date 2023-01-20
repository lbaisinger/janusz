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



# current color pallete : https://coolors.co/242320-fcf7f8-bf4342-76877d-f77f00