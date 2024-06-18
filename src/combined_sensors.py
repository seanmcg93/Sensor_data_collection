import bin_sensor_iface
import case_sensor_iface

sensor_cases = case_sensor_iface.Sensor("Cases", 0, 1)
sensor_bins = bin_sensor_iface.Sensor("Bins", 0, 2, delay=10)