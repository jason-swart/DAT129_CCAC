#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:40:12 2020

@author: kynligbein
"""

import json
import requests


class APICall:
    def __init__(self, company, model, year):
        self.company = company
        self.model = model
        self.year = year

    @property
    def url(self):
        return f'https://webapi.nhtsa.gov/api/Recalls/vehicle/modelyear/' \
               + f'{self.year}/make/{self.company}/model/' \
               + f'{self.model}?format=json'

    def get_request(self):
        api_response = requests.get(self.url)
        if int(api_response.status_code) == 200:
            return json.loads(api_response.text)

    def get_count(self, api_response):
        return api_response["Count"]

    def json_dump(self, api_response):
        output_path = f'{self.company}_{self.model}_{self.year}_recalls.json'
        print(f'Dumping API data to {output_path}')
        with open(output_path, 'w') as out_file:
            json.dump(api_response, out_file, indent=4)


if __name__ == '__main__':
    kia = APICall('kia', 'forte', 2011)
    api_data = kia.get_request()
    kia.get_count(api_data)
    kia.json_dump(api_data)
