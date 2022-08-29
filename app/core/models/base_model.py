import os

from peewee import *

from playhouse.pool import PooledMySQLDatabase
from playhouse.shortcuts import ReconnectMixin
from playhouse.sqliteq import SqliteQueueDatabase, SqliteExtDatabase

from app.config.config_loader import ConfigLoader


class ReconnectMySQLDatabase(ReconnectMixin, PooledMySQLDatabase):
    pass


config = ConfigLoader.load()

DATABASE_PROVIDER = os.getenv('DATABASE_PROVIDER', config['provider'])

conn = None

if DATABASE_PROVIDER == 'mysql':
    conn = ReconnectMySQLDatabase(os.getenv('MYSQL_DB', config['mysql_db']),
                                  user=os.getenv('MYSQL_USERNAME', config['mysql_username']),
                                  password=os.getenv('MYSQL_PASSWORD', config['mysql_password']),
                                  host=os.getenv('MYSQL_HOSTNAME', config['mysql_hostname']),
                                  port=os.getenv('MYSQL_PORT', config['mysql_port']),
                                  max_connections=100,
                                  stale_timeout=300,
                                  timeout=0)
else:
    conn = SqliteExtDatabase('asutp_msgs.db')


def set_conn(new_conn):
    global conn
    conn=new_conn


def get_conn():
    global conn
    return conn


class BaseModel(Model):
    class Meta:
        global conn
        database = conn  # соединение с базой, из шаблона выше
