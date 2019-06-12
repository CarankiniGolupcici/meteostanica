import os

from flask import Flask, render_template
from user_pass_host import procitajIstoriju
import mysql.connector
import senzori
import threading
from senzor_to_mysql import zapisujPodatke

sensor_helper = senzori.senzor()
sensor_helper1 = senzori.senzor1()

app = Flask(__name__, root_path=os.path.join(os.path.dirname(__file__), "html"))





@app.route("/istorija.html")
def jaje():
    entries = procitajIstoriju()
    return render_template('istorija.html', entries=entries)

@app.route('/sajt.html')
@app.route('/')
def kurton():
    humidity, temperature = sensor_helper.getHumidityAndTemp()
    pressure = sensor_helper1.getPressure()
    temperature2 = sensor_helper1.getTemp()
    return render_template('sajt.html', temperatura='{0:0.2f}'.format((temperature+temperature2)/2), vazduh='{0:0.2f}'.format(humidity), pritisak='{0:0.2f}'.format(pressure/100))


def ucitajVrednosti(sc):
    humidity, temperature = sensor_helper.getHumidityAndTemp()
    pressure = sensor_helper1.getPressure()
    temperature2 = sensor_helper1.getTemp()
    zapisujPodatke(temperature,temperature2,pressure,humidity)
    print("zapisujem")
    if not sc.is_set():
        threading.Timer(1800,ucitajVrednosti,[sc]).start()
sc = threading.Event()
ucitajVrednosti(sc)


if __name__ == '__main__':
    #app.debug = True
    app.run(host='0.0.0.0', port=5000)
