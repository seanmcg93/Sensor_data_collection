# Sensor Data Dashboard

## Overview
This project collects and visualizes real-time data from various sensors connected to a Raspberry Pi. The sensor data is stored in a PostgreSQL database, and **Metabase** is used to display the data on a web-based dashboard. Users can view real-time insights, perform queries, and access historical data via this interactive interface.

## Features
- **Real-Time Data Display:** Real-time sensor data is logged into the PostgreSQL database and displayed through Metabase.
- **Metabase Dashboards:** Easy-to-use dashboards provide data visualization and querying.
- **Query Functionality:** Users can perform custom queries directly through the Metabase interface.
- **Scalability:** Easily add new sensors and corresponding tables in the database for real-time tracking.

## Technical Specifications

### Frontend
- **Data Visualization:** **Metabase** for easy dashboard creation and real-time sensor data visualization.
- **Real-Time Updates:** WebSockets or alternative technology for live data streaming.

### Backend
- **Technologies:** Python is used to run the sensor code and write to the database.
- **Database:** PostgreSQL to store sensor data.
- **Data Hosting:** Sensor data is hosted locally on the Raspberry Pi, while Metabase is set up to visualize this data on the web app.
- **Metabase Setup:** Metabase is connected to PostgreSQL to generate interactive reports and dashboards.

## Setup Instructions
### Prerequisites
- Raspberry Pi for collecting sensor data.
- Separate computer for hosting the Metabase instance and the web application.
- [Sixteen LV Digital Inputs 8-Layer Stackable HAT](https://sequentmicrosystems.com/products/16-universal-inputs-card-for-raspberry-pi): Used to connect the sensors to the Raspberry Pi, interfacing through the `lib16inpind` library.
- PostgreSQL installed on the Raspberry Pi for data storage.
- **Metabase** installed to visualize the data.

### Configuration
1. **Clone the repository:**
    ```bash
    git clone https://github.com/seanmcg93/sensor_data_collection.git
    cd sensor_data_collection
    ```

2. **Configure the database connection:**
    Update the PostgreSQL configuration to ensure your sensor data is being logged correctly.

3. **Install and Configure Metabase:**
   - Install Metabase on the server where the web app is hosted.
   - Connect Metabase to the PostgreSQL database by setting up a new database connection inside the Metabase admin panel.

4. **Run the web application:**
    Follow the instructions to start your local development server.

## Usage
- The dashboard will automatically display real-time data from the sensors.
- **Metabase:** Access the Metabase interface at `http://<your_metabase_url>` to visualize data or run custom queries.
- Use the query interface in Metabase for historical data retrieval.

## Project Structure
- `src/`: Web app source code.
- `public/`: Public assets
- `database/`: PostgreSQL configuration and migration scripts.
- `README.md`: Project overview and setup instructions.

## Contribution
Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss your proposed changes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For questions or suggestions, please contact Sean McGovern at seanmcgovern93@proton.me.
