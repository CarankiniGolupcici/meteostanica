class senzor:
    def getHumidityAndTemp(self):
        import Adafruit_DHT
        sensor = Adafruit_DHT.AM2302
        pin= 14
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        if humidity is not None and temperature is not None:
            return humidity, temperature
        else:
            return 0,0

class senzor1:
    def getTemp(self):
        import Adafruit_BMP.BMP085 as BMP085
        sensor = BMP085.BMP085()
        return sensor.read_temperature()

    def getPressure(self):
        import Adafruit_BMP.BMP085 as BMP085
        sensor = BMP085.BMP085()
        return sensor.read_pressure()
