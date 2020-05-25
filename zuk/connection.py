import pymysql


def connection():
    con = pymysql.connect('localhost', 'root',
                          'rootroot', 'reminderbot')
    return con