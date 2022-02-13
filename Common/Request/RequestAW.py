#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Created on 2016年10月9日
@author: LiuBin
@note: requests
"""

# from RequestsLibrary import RequestsKeywords
from RequestsLibrary import RequestsLibrary

import logging


class RequestAW:
    def __init__(self):
        self.req_aw = RequestsLibrary()

    def login_aw(self):
        alias = 'test'
        url = 'so?apiKey=YOUR-API-KEY'
        headers = {
            'Authentication': 'apiKey=0548cc14b65b457f92207b6c1559442e'
        }
        alias = self.req_aw.create_session(alias, url, headers)
        return alias

    def send_post_recv_200(self, url, data):
        alias = self.login_aw()
        response = self.req_aw.post_request(alias, url, data)
        if response.content is not 200:
            raise logging.info(u'send_post_recv_200 is failed, response is %s' % data)
        return response

    def get_nutrition(self, url, data):
        url = 'https：//spoonacular.com/food-api/docs#Analyze-Recipe'
        data = {'includeNutrition': True}
        response = self.send_post_recv_200(url, data)
        return response


if __name__ == '__main__':
    pass
