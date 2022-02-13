#!/usr/bin/env python

import sys
import os
import json


class JsonHandle:
    def __init__(self):
        pass

    def added_value_to_keywords(self,keys,value,json_string):
        """
            Argument:
            -keys:  json keys.
            -value: key value.
            -json_string:  jsonset.

            Return:
            -jsonpair:  host IPAddress

            author:liubin

            Examples:
            added_value_to_keywords | name | {"liubin"} | {"name":{},"age":"28"}
            result : {name:"liubin"}
        """
        json_str = json.loads(json_string)
        json_value = value
        #json_str[keys] = value
        try:
            json_value = json.loads(json_value)
        except Exception:
            print(str(value))
        json_str[keys] = json_value
        return json.dumps(json_str)

    # @staticmethod
    # def get_value_by_key(key, json_body):
    #     py_body = json.loads(json_body)
    #     if isinstance(json_body, dict):
    #         pass
    #
    #
    #     json_value = py_body[key]
    #     return json.dumps(json_value)

    @staticmethod
    def get_value_by_key_py(key, json_body):
        try:
            py_body = json.loads(json_body)
            get_value = py_body[key]
            return json.dumps(get_value)
        except Exception:
            get_value = json_body[key]
            if isinstance(get_value, list):
                return get_value
            else:
                return json.dumps(get_value)

    @staticmethod
    def get_item_by_index_py(index, json_body):
        try:
            py_body = json.loads(json_body)
            item = py_body[index]
            return item
        except Exception:
            item = json_body[index]
            return item

if __name__ == '__main__':
    json_aw = JsonHandle()
    json_body_tmp = {'aa':'bb', 'cc':[{'dd','ee'}, {'ff': 'gg'}]}
    value_tmp = json_aw.get_value_by_key_py('cc', json_body_tmp)
    print(value_tmp)
    item_tmp = json_aw.get_item_by_index_py(1, value_tmp)
    print(item_tmp)


	


