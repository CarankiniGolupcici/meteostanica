import os

from flask import Flask, url_for, render_template

#import senzori
#sensor_helper = senzori.senzori()
import senzori_test
sensor_helper = senzori_test.senzori()

app = Flask(__name__, root_path=os.path.join(os.path.dirname(__file__), "html"))


@app.route('/')
def kurton():
    humidity, temperature = sensor_helper.getHumidityAndTemp()
    return render_template('sajt.html', temperatura=temperature, vazduh=humidity, pritisak=35)


if __name__ == '__main__':
    app.run()
