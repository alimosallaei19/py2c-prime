import sensors.rm3100

class RM3100:
    sensor = None
    def __init__(self):
        self.sensor = sensors.rm3100.PniRm3100()
        self.sensor.assign_device_addr(input_addr=0x21)
        self.sensor.assign_cmm_byte()
        self.sensor.write_cmm()
    
    def get_x(self):
        return self.sensor.read_meas_x()

    def get_y(self):
        return self.sensor.read_meas_y()
    
    def get_z(self):
        return self.sensor.read_meas_z()
