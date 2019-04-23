from flask import Flask
from flask import render_template
import Adafruit_DHT
app = Flask(__name__)
@app.route('/')
def kurton():
    humidity, temperature =penis()
    return render_template('sajt.html', temperatura=temperature, vazduh=humidity, pritisak=35)
def penis():
    sensor = Adafruit_DHT.AM2302
    pin= 1
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        return humidity, temperature
    else:
        return 0,0
