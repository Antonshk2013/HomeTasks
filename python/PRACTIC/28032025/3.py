#!/usr/bin/env python3
import argparse
from pprint import pprint

parser = argparse.ArgumentParser()
parser.add_argument("--domain", nargs='?', default="http://127.0.0.1")
parser.add_argument("--port", nargs='?', default=8000, type=int)
args = parser.parse_args()
pprint({
    "domain": args.domain,
    "port": args.port
})


# python task_06.py --domain website.com --port 8888