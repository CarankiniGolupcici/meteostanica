import os

from flask import Flask, render_template
from user_pass_host import procitajIstoriju
import mysql.connector
# import senzori
# sensor_helper = senzori.senzori()
import senzori_test

sensor_helper = senzori_test.senzori()

app = Flask(__name__, root_path=os.path.join(os.path.dirname(__file__), "html"))





@app.route("/istorija.html")
def jaje():
    entries = procitajIstoriju()
    return render_template('istorija.html', entries=entries)

@app.route('/sajt.html')
@app.route('/')
def kurton():
    humidity, temperature = sensor_helper.getHumidityAndTemp()
    pressure = sensor_helper.getPressure()
    return render_template('sajt.html', temperatura=temperature, vazduh=humidity, pritisak=pressure)


if __name__ == '__main__':
    app.debug = True
    app.run()
