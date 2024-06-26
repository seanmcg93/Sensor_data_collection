# Sensor Data Dashboard

## Overview
This project is designed to create a local web application that displays real-time data from various sensors connected to a Raspberry Pi. The sensors log their data into a PostgreSQL database, and the web application provides a dashboard to visualize this data. Additionally, users can perform basic queries to retrieve historical data from the database.

## Features
- **Real-Time Data Display:** Pulls and displays real-time data from the PostgreSQL database, with each sensor logging data to a different table.
- **Query Functionality:** Allows users to perform basic queries to retrieve historical data.
- **Scalability:** Easily accommodates the addition of new sensors and corresponding tables in the database.

## Technical Specifications
### Frontend
- **Technologies:** HTML, CSS, JavaScript (React.js or another modern framework)
- **Real-Time Updates:** Utilizes WebSockets or another appropriate technology for real-time updates.

### Backend
- **Database:** PostgreSQL
- **Hosting:** The web application is hosted on a separate computer (not the Raspberry Pi) and is accessible only on the local network.

## Setup Instructions
### Prerequisites
- Raspberry Pi for sensor data collection
- Separate computer for hosting the web application
- Sixteen LV Digital Inputs 8-Layer Stackable HAT for Raspberry Pi: This HAT is used to connect the sensors to the Raspberry Pi. It uses the lib16inpind library to interface with the sensor channels. More information can be found here. https://sequentmicrosystems.com/products/16-universal-inputs-card-for-raspberry-pi.
- SQLite3 installed on the hosting computer

### Configuration
1. **Clone the repository:**
    ```bash
    git clone https://github.com/seanmcg93/sensor_data_collection.git
    cd sensor_data_collection
    ```

2. **Configure the database connection:**
    Update the database configuration in the project to point to your PostgreSQL database.


## Usage
- The dashboard will automatically display real-time data for each sensor.
- Use the query interface to retrieve specific historical data from the database.

## Project Structure
- `src/`: Contains the source code for the web application.
- `public/`: Contains public assets and the main HTML file.
- `database/`: Contains the PostgreSQL database file (if included) and migration scripts.
- `README.md`: Project overview and setup instructions.

## Contribution
Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT Lisense - see the [LICENSE](LICENSE) file for details.

## Contact
For any questions or suggestions, please contact Sean McGovern at seanmcgovern93@proton.me .
