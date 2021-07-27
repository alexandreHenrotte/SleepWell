from flask import Flask, render_template, request
from services.process import calculate

app = Flask(__name__, template_folder="templates",
            static_folder='static')
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['get'])
def process():
    mode = request.args.get('mode')
    hour = request.args.get('hour')
    minutes = request.args.get('minutes')

    timesAdviced = calculate(mode, hour, minutes)
    print(timesAdviced)
    return render_template("result.html", mode=mode, timesAdviced=timesAdviced)


if __name__ == '__main__':
    app.run()
