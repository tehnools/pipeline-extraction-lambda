#!/usr/bin/python
import psycopg2
import os

db_host = os.environ["DB_HOST"]
db_port = os.environ["DB_PORT"]
db_name = os.environ["DB_NAME"]
db_user = os.environ["DB_USER"]
db_pass = os.environ["DB_PASS"]

def make_conn():
    conn = None
    try:
        conn = psycopg2.connect("dbname='%s' user='%s' host='%s' password='%s'" % (db_name, db_user, db_host, db_pass))
    except:
        print "I am unable to connect to the database"
    return conn


def fetch_data(conn, query):
    result = []
    print "Now executing: %s" % (query)
    cursor = conn.cursor()
    cursor.execute(query)

    raw = cursor.fetchall()
    for line in raw:
        result.append(line)

    return result
