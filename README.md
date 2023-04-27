# Simulate various IP printer web servers

The purpose of this project is to create a partial replica of a Printer IP web server allowing to simulate an endpoint that offers a csv file to be downloaded.

It was built to be an extra feature related to this [project](https://github.com/mvarrone/printer-monitoring)

# Software used:

- Docker

    *By creating Docker containers and using Docker Compose, we can have multiple IP addresses in a network (such as 192.168.1.0/24) used to do some testing*
- FastAPI

    *Python 3 web framework created to serve an API
# Resource used:

- A CSV file downloaded from a Brother HL-1210W Series

# More information

About endpoints: 

1) Root endpoint: `/`

    * Created to test API availability. 
    * It returns a dictionary with a message and a datetime info

2) CSV endpoint: `/etc/mnt_info.csv`

    * Created to download a specific maintenance CSV file
    * It returns that CSV file