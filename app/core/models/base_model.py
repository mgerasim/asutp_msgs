from peewee import *

from playhouse.pool import PooledMySQLDatabase
from playhouse.shortcuts import ReconnectMixin
from playhouse.sqliteq import SqliteQueueDatabase, SqliteExtDatabase

db2 = SqliteExtDatabase('asutp_msgs.db')

db = SqliteQueueDatabase(
    'asutp_msgs.db',
    use_gevent=False,  # Use the standard library "threading" module.
    autostart=True,  # The worker thread now must be started manually.
    queue_max_size=64,  # Max. # of pending writes that can accumulate.
    results_timeout=5.0)  # Max. time to wait for query to be executed.

class ReconnectMySQLDatabase(ReconnectMixin, PooledMySQLDatabase):
    pass

#conn = SqliteDatabase(configs.database.DBNAME, pragmas={
#    'journal_mode': 'wal',
#    'cache_size': 10000,  # 10000 pages, or ~40MB
#    'foreign_keys': 1,  # Enforce foreign-key constraints
#})

#conn = MySQLDatabase('tgbotdb', user='tgbot', password='3-Gj%Aw{L@+Ds.79',
#                         host='localhost', port=3306)

dbname='tgbotdb'

dbhost='localhost'

conn = ReconnectMySQLDatabase(dbname,
                     user='tgbot',
                     password='3-Gj%Aw{L@+Ds.79',
                     host=dbhost,
                     port=3306,
                     max_connections=100,
                     stale_timeout=300,
                     timeout=0)


def set_conn(new_conn):
    global conn
    conn=new_conn


def get_conn():
    global conn
    return conn


class BaseModel(Model):
    class Meta:
        global db2
        database = db2
        #database = conn  # соединение с базой, из шаблона выше
