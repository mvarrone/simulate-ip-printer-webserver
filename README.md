# Simulation of Multiple IP Printer Web Servers

This project aims to provide a simulation of a small partial replica of a IP Printer web server, allowing to recreate an endpoint that offers a CSV file to be downloaded. 

This feature was built to complement the [printer-monitoring project](https://github.com/mvarrone/printer-monitoring)

## Technologies used

- Docker

    - By using Docker and Docker Compose, it is possible to create various containers in order to simulate we have multiple IP Printers connected directly in our physical network
    
    - So, this way we can use those IP addresses from each container and writing them in the `devices.json` file available at the `app` folder on [printer-monitoring project](https://github.com/mvarrone/printer-monitoring) to make some tests
    
- FastAPI

    - FastAPI is a web framework for building APIs with Python 3. Only a small amount of what this framework offers has been used

## Considerations

### About networking
- In this project, network chosen was 192.168.1.0/24 with a gateway of 192.168.1.1 and containers were configured to obtain the following IP addresses: 192.168.1.201/24 and 192.168.1.202/24

- So, unless your network be the same and you have those specific IP addresses available to assign to new hosts, you should adapt this [docker-compose.yml](https://github.com/mvarrone/simulate-ip-printer-webserver/blob/main/docker-compose.yml) file to your network specs

### About Docker Desktop on Windows
- Driver `ipvlan` is needed to make containers obtain an IP address directly from your physical network. Unfortunately, it is not available on Windows systems at the moment.

- So, to mitigate this problem an Ubuntu VM has been deployed on Windows. Inside that VM, docker and docker compose were installed.

## Resources used

- A CSV file downloaded from a Brother HL-1210W Series printer is provided to make it available in the correspondant endpoint to be downloaded

## Endpoints

1. Root Endpoint: `/`

    * This endpoint was created to test the availability of the API
    * It returns a dictionary with a message and datetime information

2. CSV Endpoint: `/etc/mnt_info.csv`

    * This endpoint was created to download a maintenance CSV file
    * It returns the CSV file

## Usage

1. Clone this repository

    ```md
    git clone https://github.com/mvarrone/simulate-ip-printer-webserver.git
    cd simulate-ip-printer-webserver
    ```
2. Install Docker and Docker Compose
    ```md
    sudo apt-get update && sudo apt-get install docker docker-compose -y
    ```
3. Run Docker Compose

    a) Start
    ```md
    docker-compose up -d
    ```

    b) Stop
    ```md
    docker-compose down
    ```

4. Test the containers are working by using a web browser and visiting `http://192.168.1.201/` and `http://192.168.1.202/`

    You can also use `curl` or `Postman`
    
    If working, you should see something like:
    ```md
    {
        'message': 'App is working',
        'time': datetime string
    } 
    ```

5. Add data printer inside the `devices.json` file. It must be added in the format of Python 3 dictionaries

    Example:
    ```md
    {
        "protocol": "http",
        "ip_address": "192.168.1.201",
        "port": 80,
        "path": "etc",
        "csv_filename": "mnt_info.csv"
    }
    ```

6. Now, you can use that other project with new hosts available to be tested

## Contributions

Contributions are welcome! Please create a pull request with any changes or improvements you would like to make

## License
This project is licensed under the MIT License. See the [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
 file for details