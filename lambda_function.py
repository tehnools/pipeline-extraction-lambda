#!/usr/bin/python
import json
from .db_util import make_conn, fetch_data

def lambda_handler(event, context):
    query = "SELECT * FROM %s WHERE "
    conn = make_conn()
    result = fetch_data(conn, query) 
    conn.close()

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }