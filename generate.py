#!./venv/bin/python3
from jinja2 import Environment, FileSystemLoader
from pprint import pprint
from passlib.hash import md5_crypt
import random
import string

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)
    return result_str

data = {
    20936: {
        'downstreams': [5000,4000,3000,2000,1000],
        'peers': [10000,9000,8000,7000,6000],
        'upstreams': [],
        'roamings': [],
    },
    60000: {
        'downstreams': [500,600],
        'peers': [],
        'upstreams': [9000],
        'roamings': [100],
    },
    10000: {
        'downstreams': [1000,2000],
        'peers': [20936],
        'upstreams': [],
        'roamings': [],
    },
    9000: {
        'downstreams': [60000],
        'peers': [20936],
        'upstreams': [],
        'roamings': [],
    },
    8000: {
        'downstreams': [300,400],
        'peers': [20936],
        'upstreams': [],
        'roamings': [],
    },
    7000: {
        'downstreams': [],
        'peers': [6000,20936],
        'upstreams': [],
        'roamings': [],
    },
    6000: {
        'downstreams': [],
        'peers': [7000,20936],
        'upstreams': [],
        'roamings': [],
    },
    5000: {
        'downstreams': [],
        'peers': [6000,20936],
        'upstreams': [20936],
        'roamings': [],
    },
    4000: {
        'downstreams': [100,200],
        'peers': [],
        'upstreams': [20936],
        'roamings': [],
    },
    3000: {
        'downstreams': [],
        'peers': [],
        'upstreams': [20936],
        'roamings': [],
    },
    2000: {
        'downstreams': [],
        'peers': [],
        'upstreams': [10000,20936],
        'roamings': [],
    },
    1000: {
        'downstreams': [],
        'peers': [],
        'upstreams': [10000,20936],
        'roamings': [],
    },
    600: {
        'downstreams': [],
        'peers': [],
        'upstreams': [60000],
        'roamings': [100,200],
    },
    500: {
        'downstreams': [],
        'peers': [],
        'upstreams': [60000],
        'roamings': [100,200],
    },
    400: {
        'downstreams': [],
        'peers': [],
        'upstreams': [8000],
        'roamings': [200],
    },
    300: {
        'downstreams': [],
        'peers': [],
        'upstreams': [8000],
        'roamings': [100],
    },
    200: {
        'downstreams': [],
        'peers': [],
        'upstreams': [4000],
        'roamings': [400,500],
    },
    100: {
        'downstreams': [],
        'peers': [],
        'upstreams': [4000],
        'roamings': [60000],
    },
}

for asn, config in data.items():
    password = get_random_string(12)
    data[asn]['password'] = password
    data[asn]['password_hashed'] = md5_crypt.using(salt_size=4).hash(password)

pprint(data)

environment = Environment(loader=FileSystemLoader("./"))
template = environment.get_template('irrd.tmpl')
for asn, config in data.items():
    irrd_output = template.render(asn=asn,config=config)
    with open(str(asn)+'.dat', mode="w", encoding="utf-8") as irrd_output_file:
        irrd_output_file.write(irrd_output)
        print(f"... wrote {irrd_output_file}")
