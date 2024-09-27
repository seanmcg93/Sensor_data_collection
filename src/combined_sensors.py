import bin_sensor_iface
import case_sensor_iface
import up_down_time

sensor_cases = case_sensor_iface.Sensor("Cases", 0, 1)
sensor_bins = bin_sensor_iface.Sensor("Bins", 0, 2, delay=45)
sensor_up_down_time = up_down_time.Sensor("Up_Down", 0, 4)
