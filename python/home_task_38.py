from pprint import pprint

import mysql.connector
from local_settings import *

import mysql.connector
dbconfig = {
    'host': HOST,
    'user': USER,
    'password': PASSWORD,
    'database': DATABASE,
}