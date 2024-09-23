import json
import pandas as pd
import sys
from requests import Session
from icdc.requestswithsystemca import setup_session
from requests.auth import HTTPBasicAuth
import datetime
import os

URL_GAMERA_API = "https://gamera.serv.cdc.fr/squash/api/rest/latest/"


def send_score_to_testcase_gamera(testcase, username, password):
    session = Session()
    setup_session(session)
    data = {
            "_type" : "test-case",
            "automation_priority" : testcase['score_final']
        }
    url_query = URL_GAMERA_API+'test-cases/'+str(testcase['id'])
    print(url_query)
    response = session.patch(URL_GAMERA_API + 'test-cases/'+str(testcase['id']), auth = HTTPBasicAuth(username, password), json= data)
    if response.ok:
        print('Request was successful:', response.status_code)
    else:
        print('Request failed:', response.status_code, response.text)

def send_all_scores_to_gamera():
    excel_path = "../docs/score.xlsx"
    column_names = ["id", "test", "score_final"]

    # json_data = read_excel_and_convert_to_json(excel_path, column_names)
    json_data = read_excel_and_convert_to_json(excel_path)

    json_list = json.loads(json_data)

    for testcase in json_list:
        print(testcase)
        send_score_to_testcase_gamera(testcase, "usine_test_auto", "usine_test_auto")

def read_excel_and_convert_to_json(path):
# Load the Excel file
    file_path = path
    df = pd.read_excel(file_path)

    # Select only the columns 'id', 'tests', and 'score_final'
    df_filtered = df[['id', 'test', 'score_final']]

    df_filtered = df_filtered.dropna()

    df_filtered['id'] = df_filtered['id'].astype(int)
    df_filtered['score_final'] = df_filtered['score_final'].astype(int)


    # Convert the DataFrame to a list of dictionaries (JSON-like structure)
    data_json = df_filtered.to_dict(orient='records')

    # Convert the list to a JSON string
    json_data = json.dumps(data_json, indent=4)

    # Save the JSON string to a file
    return json_data

    print("JSON data successfully written to output.json")

if __name__ == "__main__":
    excel_path = "../docs/score.xlsx"
    column_names = ["id", "test", "score_final"]

    # json_data = read_excel_and_convert_to_json(excel_path, column_names)
    json_data = read_excel_and_convert_to_json(excel_path)

    json_list = json.loads(json_data)

    for testcase in json_list:
        print(testcase)
        send_score_to_testcase_gamera(testcase, "usine_test_auto", "usine_test_auto")
