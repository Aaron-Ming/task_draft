#encoding=utf-8
#
import MySQLdb as mysql
con = None
cursor = None

def connect():
    global con
    global cursor
    con = mysql.connect(db='mingguangzhen', host='180.153.191.128', user='reboot', passwd='reboot123')
    con.autocommit(True)
    cursor = con.cursor()


def execute(sql):
    try:
        cursor.execute(sql)
    except Exception:
        try:
            con.close()
            cursor.close()
        except Exception:
            pass
        print 'db connect again.'
        connect()
        cursor.execute(sql)
        
