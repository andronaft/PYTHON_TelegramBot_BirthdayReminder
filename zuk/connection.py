import pymysql

con = pymysql.connect('localhost', 'root',
                      'rootroot', 'reminderbot')

def connection():
    con = pymysql.connect('localhost', 'root',
                          'rootroot', 'reminderbot')
    return con

# with con:
#     cur = con.cursor()
#     cur.execute("SELECT * FROM remember")
#
#     rows = cur.fetchall()
#
#     for row in rows:
#         print("{0} {1} {2} {3}".format(row[0], row[1], row[2], row[3]))