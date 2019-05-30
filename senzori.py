class senzori:
    def getHumidityAndTemp(self):
        import Adafruit_DHT
        sensor = Adafruit_DHT.AM2302
        pin= 1
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        if humidity is not None and temperature is not None:
            return humidity, temperature
        else:
            return 0,0
    def getPressure(self):
        if pressure is not None:
            return pressure
        else:
            return 0
