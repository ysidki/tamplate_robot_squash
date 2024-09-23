import requests
from robot.api import logger
import json
import pandas as pd
import sys
from requests import Session
from icdc.requestswithsystemca import setup_session
from requests.auth import HTTPBasicAuth
import datetime
import os

URL_GAMERA_API = "https://gamera.serv.cdc.fr/squash/api/rest/latest/"

class Gamera:
    ROBOT_LISTENER_API_VERSION = 3  # Defines the Robot Framework listener API version

    def __init__(self, id_campaign, username,password):
        self.id_campaign = id_campaign  # Replace with your API endpoint
        self.username = username
        self.password = password

    def get_test_plan(self):
        session = Session()
        setup_session(session)
        response = session.get(URL_GAMERA_API + 'campaigns/'+str(self.id_campaign), auth = HTTPBasicAuth(self.username, self.password))
        if response.ok:
            print('Request was successful:', response.status_code)
        else:
            print('Request failed:', response.status_code, response.text)


        response_json = response.json()
        test_plan_list = response_json['test_plan']
            
        return test_plan_list

    