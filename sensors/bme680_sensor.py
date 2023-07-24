import bme680
import sys

args = sys.argv

class BME680:
	sensor = None
	
	def __init__(self):
		try:
			self.sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
		except (RuntimeError, IOError):
			self.sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)

		self.sensor.set_humidity_oversample(bme680.OS_2X)
		self.sensor.set_pressure_oversample(bme680.OS_4X)
		self.sensor.set_temperature_oversample(bme680.OS_8X)
		self.sensor.set_filter(bme680.FILTER_SIZE_3)
		self.sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)

		# Initial values for heater
		self.sensor.set_gas_heater_temperature(320)
		self.sensor.set_gas_heater_duration(150)
		self.sensor.select_gas_heater_profile(0)

		self.sensor.set_power_mode(1)

		print("[EXTERN][BME680] BME680 is initialized")

	def get_temp(self):
		if self.sensor.get_sensor_data():
			return self.sensor.data.temperature

	def get_pressure(self):
		if self.sensor.get_sensor_data():
			return self.sensor.data.pressure

	def get_humidity(self):
		if self.sensor.get_sensor_data():
			return self.sensor.data.humidity
