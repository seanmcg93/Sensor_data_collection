### Database Schema Documentation

#### Overview

This document describes the schema of the PostgreSQL database used for storing sensor data. The database contains two tables: `bin_dump_count` and `case_count`. Each table is designed to store specific types of data collected from sensors.

#### Tables

---

#### Table: `bin_dump_count`

**Description**: This table keeps track of the bin dumps.

| Column Name | Data Type | Constraints             | Description                                   |
|-------------|-----------|-------------------------|-----------------------------------------------|
| `id`        | `SERIAL`  | `PRIMARY KEY`           | Auto-incrementing unique identifier for each entry. |
| `date`      | `TEXT`    | `NOT NULL`              | The date when the bin dump was recorded.      |
| `time`      | `TEXT`    | `NOT NULL`              | The time when the bin dump was recorded.      |
| `count`     | `INTEGER` | `NOT NULL`              | The count of bin dumps recorded.              |

**Table Creation SQL**:
```sql
CREATE TABLE IF NOT EXISTS bin_dump_count (
    id SERIAL PRIMARY KEY,
    date TEXT NOT NULL,
    time TEXT NOT NULL,
    count INTEGER NOT NULL
);
```

---

#### Table: `case_count`

**Description**: This table keeps track of the case counts per day.

| Column Name | Data Type | Constraints             | Description                                   |
|-------------|-----------|-------------------------|-----------------------------------------------|
| `date`      | `TEXT`    | `PRIMARY KEY`           | The date when the case count was recorded.    |
| `count`     | `INTEGER` | `NOT NULL`              | The count of cases recorded for the day.      |

**Table Creation SQL**:
```sql
CREATE TABLE IF NOT EXISTS case_count (
    date TEXT PRIMARY KEY,
    count INTEGER NOT NULL
);
```

---

#### Detailed Explanation

1. **Table: `bin_dump_count`**
    - **Columns**:
        - `id`: An auto-incrementing integer that serves as the unique identifier for each row.
        - `date`: A text field that records the date of the bin dump.
        - `time`: A text field that records the time of the bin dump.
        - `count`: An integer field that records the count of bin dumps.

    - **Purpose**: This table is used to track the number of times bins are dumped each day. Each record includes the date and time of the bin dump and an incremental count of dumps.

2. **Table: `case_count`**
    - **Columns**:
        - `date`: A text field that serves as the unique identifier (primary key) for each row, recording the date of the case count.
        - `count`: An integer field that records the count of cases for that date.

    - **Purpose**: This table is used to track the number of cases recorded each day. Each record includes the date and the total count of cases for that date.

---

#### Relationships

Currently, there are no explicit relationships (foreign keys) between the `bin_dump_count` and `case_count` tables. Each table operates independently to store its respective type of data.

#### Usage Examples

**Inserting Data into `bin_dump_count`**:
```python
import psycopg2
from datetime import datetime
import os
import db_conf


# Example function to insert data into bin_dump_count
def insert_bin_dump_count():
    date = datetime.now().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H:%M:%S")
    con = psycopg2.connect(
                dbname=db_conf.db_name,
                user=db_conf.db_user,
                password=db_conf.db_pass,
                host=db_conf.db_host,
                port=db_conf.db_port
            )
    
    cur = con.cursor()
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS bin_dump_count (
            id SERIAL PRIMARY KEY,
            date DATE NOT NULL,
            time TIME NOT NULL,
            count INTEGER NOT NULL
        )
    """)
    
    cur.execute("SELECT count FROM bin_dump_count WHERE date = %s ORDER BY id DESC LIMIT 1", (date,))
    row = cur.fetchone()
    
    if row:
        last_count = row[0]
    else:
        last_count = 0
    
    new_count = last_count + 1
    cur.execute("INSERT INTO bin_dump_count (date, time, count) VALUES (%s, %s, %s)",
                (date, time, new_count))
    
    con.commit()
    print(f"Inserted data - Date: {date}, Time: {time}, Count: {new_count}")
    cur.close()
    con.close()


```

**Inserting Data into `case_count`**:
```python
# Example function to insert data into case_count
def insert_case_count():
    date = datetime.now().strftime("%Y-%m-%d")
    con = psycopg2.connect(
                dbname=db_conf.db_name,
                user=db_conf.db_user,
                password=db_conf.db_pass,
                host=db_conf.db_host,
                port=db_conf.db_port
            )
    
    cur = con.cursor()
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS case_count (
            date DATE PRIMARY KEY,
            count INTEGER NOT NULL
        )
    """)
    
    cur.execute("SELECT count FROM case_count WHERE date = %s", (date,))
    row = cur.fetchone()
    
    if row:
        cur.execute("UPDATE case_count SET count = count + 1 WHERE date = %s", (date,))
    else:
        cur.execute("INSERT INTO case_count (date, count) VALUES (%s, 1)", (date,))
    
    con.commit()
    cur.execute("SELECT * FROM case_count WHERE date = %s", (date,))
    print(cur.fetchone())
    cur.close()
    con.close()


```



