
import psycopg2 as pg

#connect to Direct Access
#get auth token
#get test URL

def da_connect(user, pw, db):

        conn = pg.connect(host="data.deltadna.net",port=5432 ,user=user, password=pw, database = db,sslmode='require')
        conn.set_session(autocommit = True)
        return conn

