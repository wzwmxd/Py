#!/usr/bin/python

import sqlite3

# 创建数据库demo
conn = sqlite3.connect('test.db')
print "Opened database successfully";

conn.execute(
    'CREATE TABLE weather_day(prov varchar(16),city varchar(16) PRIMARY KEY,\
        year smallint,month smallint,day smallint,weather varchar(16),\
        wind varchar (32),highest_temp smallint)'
)
print "Table created successfully"

conn.close()
