#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    """filter whit N"""
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        if "N" in row[1][0]:
            print(row)
    cur.close()
    conn.close()
