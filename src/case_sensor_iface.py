import lib16inpind
import psycopg2
import time
import threading
from datetime import datetime

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
            if not self.prev_sensor_state and current_sensor_state:
                self.sensor_action()  # Call sensor_action if sensor state changes from False to True
            self.prev_sensor_state = current_sensor_state


    def sensor_action(self):
        with self.lock:
            date = datetime.now().strftime("%Y-%m-%d")
            con = psycopg2.connect(
                dbname="database_name",
                user="database user_name",
                password="database password",
                host="database ip",
                port="database port_number"
            )

            cur = con.cursor()

            cur.execute("""CREATE TABLE IF NOT EXISTS case_count(
                date TEXT PRIMARY KEY,
                count INTEGER)""")

            # Checks if current date exists.
            cur.execute("""SELECT count FROM case_count WHERE date = %s""",(date,))
            row = cur.fetchone()

            if row:
                # If the row exists, update the count
                cur.execute("UPDATE case_count SET count = count + 1 WHERE date = %s", (date,))
            else:
                # If the row does not exist, insert a new row with count = 1
                cur.execute("INSERT INTO case_count (date, count) VALUES (%s, 1)", (date,))
            
            con.commit()
            cur.execute("SELECT * FROM case_count WHERE data = %s",(date,))
            print(cur.fetchone())
            con.close()
            
        

    def get_sensor_state(self):
        return lib16inpind.readCh(self.stack, self.channel_number) == 1
        
        
#Sensor('case',0,1)
#con= sqlite3.connect('production.db')
#cur= con.cursor()
#print(cur.execute("""SELECT * FROM case_count""").fetchall())
