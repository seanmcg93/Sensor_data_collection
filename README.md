# Sensor Data Dashboard

## Overview
This project is designed to create a local web application that displays real-time data from various sensors connected to a Raspberry Pi. The sensors log their data into a SQLite3 database, and the web application provides a dashboard to visualize this data. Additionally, users can perform basic queries to retrieve historical data from the database.

## Features
- **Real-Time Data Display:** Pulls and displays real-time data from the SQLite3 database, with each sensor logging data to a different table.
- **Query Functionality:** Allows users to perform basic queries to retrieve historical data.
- **Scalability:** Easily accommodates the addition of new sensors and corresponding tables in the database.

## Technical Specifications
### Frontend
- **Technologies:** HTML, CSS, JavaScript (React.js or another modern framework)
- **Real-Time Updates:** Utilizes WebSockets or another appropriate technology for real-time updates.

### Backend
- **Database:** SQLite3
- **Hosting:** The web application is hosted on a separate computer (not the Raspberry Pi) and is accessible only on the local network.

## Setup Instructions
### Prerequisites
- Raspberry Pi for sensor data collection
- Separate computer for hosting the web application
- SQLite3 installed on the hosting computer

### Configuration
1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/sensor-data-dashboard.git
    cd sensor-data-dashboard
    ```

2. **Configure the database connection:**
    Update the database configuration in the project to point to your SQLite3 database.


## Usage
- The dashboard will automatically display real-time data for each sensor.
- Use the query interface to retrieve specific historical data from the database.

## Project Structure
- `src/`: Contains the source code for the web application.
- `public/`: Contains public assets and the main HTML file.
- `database/`: Contains the SQLite3 database file (if included) and migration scripts.
- `README.md`: Project overview and setup instructions.

## Contribution
Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Contact
For any questions or suggestions, please contact Sean McGovern at seanmcgovern93@proton.me .
