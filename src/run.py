#!/usr/bin/env python3
"""
   Week 2 lab in Automating Real World Tasks With Python
   Jonas Bird
   2021-12-23
"""
import os
import requests


#  path = '/home/jonas/Projects/W2-IT-Automation-Web-Services/src/'
path = '/data/feedback/'
feedback_files = []
dict_keys = ['title', 'name', 'date', 'feedback']
url = 'https://en77f3mmrirw2qk.m.pipedream.net'
#  url = 'http://34.135.90.70/feedback/'    # add machine IP to address


def collect_files(path):
    filenames = os.listdir(path)
    for file_name in filenames:
        if file_name.endswith(".txt"):
            continue
        filenames.remove(file_name)
    return filenames


def extract_feedback(feedback_files, dict_keys):
    dict1 = {}
    for f in feedback_files:
        full_path = path + f
        with open(full_path, 'r') as feedback_file:
            lines = feedback_file.readlines()
            for k, line in zip(dict_keys, lines):
                dict1.update({k: line})
        response = requests.post(url, json=dict1)
        if response.status_code != requests.codes.ok:
            print(response.status_code)


if __name__ == "__main__":
    feedback_files = collect_files(path)
    extract_feedback(feedback_files, dict_keys)
