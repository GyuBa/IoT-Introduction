import spidev, time

class ForceSensor:
    def __init__(self):
        self.spi = spidev.SpiDev()
        self.spi.open(0, 0)
        self.spi.max_speed_hz = 976000


    def analog_read(self, channel):
        r = self.spi.xfer2([1, (8 + channel) << 4, 0])
        adc_out = ((r[1] & 3) << 8) + r[2]

        return adc_out

    def getData(self):
        reading = self.analog_read(1)
        voltage = reading * 3.3 / 1024
        print("Force_Sensor Reading=%d\tVoltage=%f" % (reading, voltage))

        return reading


    def clear(self):
        self.spi.close()