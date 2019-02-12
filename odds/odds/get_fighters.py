# -*- coding: utf-8 -*-

import psycopg2

conn = psycopg2.connect(
    host='baasu.db.elephantsql.com',
    user='vimfzmjn',
    password='VJAW7UC3x3MtSsxnaOsCTMQv0zCtRdUT',
    dbname='vimfzmjn',
)
cur = conn.cursor()
cur.execute('''SELECT fighter_name FROM "fighters" ''')
res = cur.fetchall()
for name in res:
    name = tuple(name[0].split(' '))
    last_name = name[1]
    name = ' '.join(name)
    if 'A' in last_name or 'B' in last_name or 'C' in last_name:
        print(name)
