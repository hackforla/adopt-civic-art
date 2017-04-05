import pymysql

conn = pymysql.connect(host='localhost', port=8889, user='root', passwd='root', db='civic-art')
cur = conn.cursor()


