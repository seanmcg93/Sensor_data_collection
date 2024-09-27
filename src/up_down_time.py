import psycopg2
import lib16inpind
import threading
from datetime import datetime, timedelta
import db_conf

class Sensor:
    def __init__(self, field_name, stack, channel_number):
        self.field_name = field_name
        self.stack = stack
        self.channel_number = channel_number
        self.pack_down_time = None
        self.first_activation_time = None
        self.final_deactivation_time = None
        self.total_down_time = timedelta()
        self.prev_sensor_state = self.get_sensor_state()
        self.lock = threading.Lock()
        self.comparison_duration = timedelta(hours=3)
        self.monitoring_thread = threading.Thread(target=self.monitor_event_detect)
        self.monitoring_thread.start()

    def monitor_event_detect(self):
        while True:
            current_sensor_state = self.get_sensor_state()
            now = datetime.now()

            if current_sensor_state == 1 and self.prev_sensor_state == 0:
                if self.first_activation_time is None:
                    self.first_activation_time = now
                if self.pack_down_time is not None:
                    down_duration = now - self.pack_down_time
                    self.total_down_time += down_duration
                    self.pack_down_time = None
                print(f"Sensor activated at {now}")

            elif current_sensor_state == 0 and self.prev_sensor_state == 1:
                self.pack_down_time = now
                self.final_deactivation_time = now
                print(f"Sensor deactivated at {now}")

            # Check if the sensor has been deactivated for longer than the comparison duration
            if self.pack_down_time and now - self.pack_down_time > self.comparison_duration:
                self.generate_summary()
                self.reset_totals()

            self.prev_sensor_state = current_sensor_state

    def generate_summary(self):
        today_date = datetime.now().strftime("%Y-%m-%d")
        total_down_minutes = int(self.total_down_time.total_seconds() // 60)

        # Calculate uptime based on start time, end time, and downtime
        if self.first_activation_time and self.final_deactivation_time:
            total_duration = self.final_deactivation_time - self.first_activation_time
            total_duration_minutes = int(total_duration.total_seconds() // 60)
            total_up_minutes = total_duration_minutes - total_down_minutes
        else:
            total_up_minutes = 0

        print(f"Generating summary at {datetime.now()}")
        print(f"Start Time: {self.first_activation_time}, End Time: {self.final_deactivation_time}")
        print(f"Total Down Time (minutes): {total_down_minutes}, Total Up Time (minutes): {total_up_minutes}")

        # Connect to PostgreSQL
        con = psycopg2.connect(
            dbname=db_conf.db_name,
            user=db_conf.db_user,
            password=db_conf.db_pass,
            host=db_conf.db_host,
            port=db_conf.db_port
        )
        cur = con.cursor()

        # Create table if not exists
        cur.execute('''CREATE TABLE IF NOT EXISTS up_down_time (
            date DATE,
            start_time TIME,
            end_time TIME,
            down_time_minutes INTEGER,
            up_time_minutes INTEGER)''')

        # Insert summary data
        cur.execute(
            '''INSERT INTO up_down_time (date, start_time, end_time, down_time_minutes, up_time_minutes) VALUES (%s, %s, %s, %s, %s)''',
            (today_date,
             self.first_activation_time.strftime("%H:%M:%S") if self.first_activation_time else '00:00:00',
             self.final_deactivation_time.strftime("%H:%M:%S") if self.final_deactivation_time else '23:59:59',
             total_down_minutes, total_up_minutes))

        con.commit()

    def reset_totals(self):
        self.total_down_time = timedelta()
        self.pack_down_time = None
        self.first_activation_time = None
        self.final_deactivation_time = None

    def get_sensor_state(self):
        return lib16inpind.readCh(self.stack, self.channel_number) == 1


