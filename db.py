#import config
import config

import pymysql

def get_connection():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 database='BDInflabExpress',
                                 port=3306,
                                 charset='utf8mb4')
    return connection

def get_connection2():
    return pymysql.connect(
        host=config('MYSQL_HOST'),
        database=config('MYSQL_DB'),
        user=config('MYSQL_USER'),
        password=config('MYSQL_PASSWORD')

    )