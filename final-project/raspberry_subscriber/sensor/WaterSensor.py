import spidev, time

class WaterSensor:
    def __init__(self, channel):

        self.spi = spidev.SpiDev()
        self.spi.open(0, 0)
        self.spi.max_speed_hz = 976000
        self.channel = channel

    def analog_read(self):
        r = self.spi.xfer2([1, (8 + self.channel) << 4, 0])
        adc_out = ((r[1] & 3) << 8) + r[2]

        return adc_out


    def getData(self):
        reading = self.analog_read()
        voltage = reading * 3.3 / 1024
        print("Water_Sensor Reading=%d\tVoltage=%f" % (reading, voltage))

        return reading


    def clear(self):
        self.spi.close()