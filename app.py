from flask import Flask, render_template
from main import crawler

app = Flask(__name__)


@app.route('/')
def hello():
    data = crawler()
    print(data)
    return render_template('index.html', user='jjanmo', data={'a': 10, 'b': 100})


if __name__ == '__main__':
    app.run(debug=True)
