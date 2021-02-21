from flask import Flask, render_template, request
from process import calculate

app = Flask(__name__, template_folder="../templates",
            static_folder='../static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api', methods=['get', 'post'])
def process():
    mode = request.args.get('mode')
    hour = request.args.get('hour')
    minutes = request.args.get('minutes')
    return calculate(mode, hour, minutes)


if __name__ == '__main__':
    app.run()
