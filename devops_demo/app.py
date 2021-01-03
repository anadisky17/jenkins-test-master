from flask import Flask, render_template, request
from calculator.cal import add

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index_view():
    x, y = 5, 6
    if request.method == 'POST':
        x = request.form['x']
        y = request.form['y']
    res = add(int(x), int(y))
    return render_template('index.html', x=x, y=y, res=res)


app.run(debug=True)
