#!/usr/bin/env python

import json
import os
import sys

records = []

def get_base():
    # Get the base directory from command line arguments.
    try:
        return sys.argv[1]
    except IndexError:
        sys.exit("[-] Usage: python cloudtrail_parser.py <Cloudtrail_dir>")
    

def list_and_parser(dir):
    # Recursively list files in a directory and parse CloudTrail JSON files.
    for item in os.listdir(dir):
        item = os.path.join(dir, item)
        if os.path.isdir(item):
            list_and_parser(item)
        if item.endswith(".json"):
            parser(item)


def parser(file):
    # Parse CloudTrail JSON file and extract 'Records' field.
    global records
    f = open(file, "r").read()
    print(f"[+] Parsering {file}")
    try:
        p = json.loads(str(f))
    except json.decoder.JSONDecodeError:
        print(f"[-] Failed parsering {file}")
        pass
    try:
        records += p["Records"]
    except TypeError:
        print(f"[-] Failed parsering {file}")
        pass
    

def validate_path(base):
    # Validate if the provided path exists.
    try:
        os.listdir(base)
    except FileNotFoundError:
        sys.exit("[-] Path not valid!")
        

def write_log_file(result):
    # Write CloudTrail records to a JSON file.
    file1 = open("./cloudtrails.json", "w") 
    file1.write(json.dumps(result))
    print("[+] Done!")

if __name__ == '__main__':
    base = get_base() 
    validate_path(base)
    list_and_parser(base)
    write_log_file(records)
