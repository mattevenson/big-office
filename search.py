import requests
import json

def search_rows(term):
    login_uri = "https://www.bigparser.com/APIServices/api/common/login"
    login_data = {'emailId': 'matthewevenson2000@gmail.com', 'password': '2Bdifferent10'}
    login_headers = {'content-type': 'application/json'}

    res = requests.post(login_uri, data=json.dumps(login_data), headers=login_headers).json()
    auth_id = res['authId']

    grid_id = '59989e26eead21301bf4a14f'

    search_uri = 'https://www.bigparser.com/APIServices/api/query/table'
    search_data = {'gridId': grid_id,
                'keywords': [term],
                'rowCount': 20}
    search_headers = {'content-type': 'application/json', 'authId': auth_id}

    res = requests.post(search_uri, data=json.dumps(search_data), headers=search_headers).json()
    rows = []
    for row in res['rows']:
        for i in range(0, len(row['data'])):
            row['data'][i] = row['data'][i].replace(term, '<mark>' + term + '</mark>')
        rows.append(row['data'])
    return rows
        
