import requests
from datetime import datetime
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

server_name = config['connections']['local_server']
vm_server_name = config['connections']['vm_server']


def add_new_physician():
    str_time = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
    new_physician = {"phys_id": 10}
    r = requests.post(server_name+"/api/new_physician", json=new_physician)
    print(r.text)


def get_physician_status():
    r = requests.get(server_name+"/api/status/1")
    print(r.text)


def add_physician_data():
    data = {"phys_id": 10,
            "data": [10.0, 11.0, 12.0, 13.0, 14.0, 15.0]}
    r = requests.post(server_name+"/api/add", json=data)
    print(r.text)


def physician_ids():
    r = requests.get(server_name+"/api/available_physician_ids")
    print(r.text)


def dates():
    r = requests.get(server_name+"/api/retrieve_phys_dates/1")
    print(r.text)


def data():
    r = requests.get(server_name+"/api/get_data/10/2020-07-14")
    print(r.text)


if __name__ == '__main__':
    # data()
    # dates()
    # physician_ids()
    add_physician_data()
    # get_physician_status()
    # add_physician_data()
    # add_new_physician()
