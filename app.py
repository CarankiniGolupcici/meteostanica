import os

from flask import Flask, url_for, render_template
import 
app = Flask(__name__, root_path=os.path.join(os.path.dirname(__file__),"html"))
@app.route('/')
def kurton():
    humidity, temperature =penis()
    return render_template('sajt.html', temperatura=temperature, vazduh=humidity, pritisak=35)
def penis():
    sensor = 3 #Adafruit_DHT.AM2302
    pin= 1
    #humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    humidity, temperature = 50, 3
    print(url_for('static', filename='background.png'))
    if humidity is not None and temperature is not None:
        return humidity, temperature
    else:
        return 0,0


if __name__ == '__main__':
    app.run()
