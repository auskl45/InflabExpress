from decouple import config

import pymysql

def get_connection():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='2005',
                                 database='inflabexpress',
                                 charset='utf8mb4')
    return connection