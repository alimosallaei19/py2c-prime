import bme680
import sys

args = sys.argv

def init():
	try:
		sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
	except (RuntimeError, IOError):
		sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)

	sensor.set_humidity_oversample(bme680.OS_2X)
	sensor.set_pressure_oversample(bme680.OS_4X)
	sensor.set_temperature_oversample(bme680.OS_8X)
	sensor.set_filter(bme680.FILTER_SIZE_3)
	sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)

	# Initial values for heater
	sensor.set_gas_heater_temperature(320)
	sensor.set_gas_heater_duration(150)
	sensor.select_gas_heater_profile(0)

	sensor.set_power_mode(1)

	print("[EXTERN][BME680] BME680 is initialized")

def get_temp():
	if sensor.get_sensor_data():
		return sensor.data.temperature

def get_pressure():
	if sensor.get_sensor_data():
		return sensor.data.pressure

def get_humidity():
	if sensor.get_sensor_data():
		return sensor.data.humidity

# first arg should always be the function that is being executed.
if args[1] == 'init':
	init()
elif args[1] == 'temp':
	get_temp()
elif args[1] == 'pressure':
	get_pressure()
elif args[1] == 'humidity':
	get_humidity()
