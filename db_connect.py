import MySQLdb

dbinfo = {}
with open('config/properties') as f:
    for line in f:
        (key, val) = line.split('=')
        dbinfo[(key)] = val[:-1]


def connection():
    conn = MySQLdb.connect(host=dbinfo['dbhost'],
                           user=dbinfo['dbuser'],
                           passwd=dbinfo['dbpasswd'],
                           db=dbinfo['dbname'])
    c = conn.cursor()

    return c, conn


if __name__ == '__main__':
    c, conn = connection()
    print('Connection Successful')
