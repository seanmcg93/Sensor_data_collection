import lib16inpind
import psycopg2
from psycopg2 import OperationalError
import time
import threading
from datetime import datetime
import db_conf

class Sensor:
    def __init__(self, field_name, stack, channel_number, delay=0):
        self.field_name = field_name
        self.stack = stack
        self.channel_number = channel_number
        self.delay = delay
        self.prev_sensor_state = self.get_sensor_state()
        self.lock = threading.Lock()  # Create a lock
        self.thread = threading.Thread(target=self.monitor_event_detect)
        self.thread.start()  # Start the monitoring thread

    def monitor_event_detect(self):
        while True:
            current_sensor_state = self.get_sensor_state()
            pack_running = lib16inpind.readCh(0, 3)
            if not self.prev_sensor_state and current_sensor_state and pack_running == 0:
                self.sensor_action()  # Call sensor_action if sensor state changes from False to True
            self.prev_sensor_state = current_sensor_state

    def connect_to_database(self):
        """Attempt to connect to the database with retry logic."""
        while True:
            try:
                return psycopg2.connect(
                    dbname=db_conf.db_name,
                    user=db_conf.db_user,
                    password=db_conf.db_pass,
                    host=db_conf.db_host,
                    port=db_conf.db_port
                )
            except OperationalError as e:
                print(f"Database connection failed: {e}. Retrying in 30 seconds...")
                time.sleep(25)

    def sensor_action(self):
        with self.lock:
            date = datetime.now().strftime("%Y-%m-%d")
            current_time = datetime.now().strftime("%H:%M:%S")

            con = self.connect_to_database()  # Use retry logic to establish connection

            try:
                cur = con.cursor()

                cur.execute("""CREATE TABLE IF NOT EXISTS bin_dump_count(
                    id SERIAL PRIMARY KEY,
                    date DATE,
                    time TIME,
                    count INTEGER,
                    Time_Difference INTERVAL
                )""")

                # Check if there is already an entry for the current date
                cur.execute("SELECT count FROM bin_dump_count WHERE date = %s ORDER BY id DESC LIMIT 1", (date,))
                row = cur.fetchone()

                if row:
                    # If there is an entry for today, continue counting
                    last_count = row[0]
                else:
                    # If no entry for today, start counting from 0
                    last_count = 0

                # Insert a new row with incremented count
                new_count = last_count + 1
                cur.execute("INSERT INTO bin_dump_count (date, time, count) VALUES (%s, %s, %s)",
                            (date, current_time, new_count))

                con.commit()
                # Print the data that was just inserted
                print(f"Inserted data - Date: {date}, Time: {current_time}, Count: {new_count}")
            except Exception as e:
                print(f"An error occurred during the database operation: {e}")
            finally:
                con.close()

            if self.delay > 0:
                time.sleep(self.delay)  # Delay to avoid double counting

    def get_sensor_state(self):
        return lib16inpind.readCh(self.stack, self.channel_number) == 1
