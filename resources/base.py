from flask import request
from flask_restful import Resource
from db import db
import json


class Base(Resource):
    def get(self):
        result = {"pgsql": {}}
        raw_sql_result = db.engine.execute("SELECT VERSION();")
        for r in raw_sql_result:
            print(r)
            result['pgsql']['version'] = r[0]
        raw_sql_result = db.engine.execute("SELECT pg_database_size('dota2')/1024/1024 as dota2_db_size;")
        for r in raw_sql_result:
            print(r)
            result['pgsql']['dota_2_db_size'] = r[0]
        return result

class HealthCheck(Resource):
    def get(self):
        return {"working": True}
