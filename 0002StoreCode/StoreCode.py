#!/usr/bin/env python
# coding=utf-8
import MySQLdb
class store_mysql(filepath):
    def store():
        try:
            conn = MySQLdb.connect(host='localhost',user='root',passwd='root',port=3306)
            cur = conn.cursor()
            cur.execute('create database if not exits Activate_Code')
            conn.select_db('Activate_Code')
            cur.execute('show tables in Code1;')
            tables = cur.fetchall()
            findtables = False
            for table in tables:
                if 'code' in table:
                    findtables = True
            
            if not findtables:
                cur.execute('''
                            CREATE TABLE 'Code1'.'code' (
                            'id' INT NOT NULL AUTO_INCREMENT,
                            'code' VARCHAR(10) NOT NULL,
                            PRIMARY KEY ('id')
                           );
                            ''')
            f = open(filepath,'rb')
            for line in f.readlines():
                code =line.strip()
                cur.execute("insert into Code1.code (code) values (%s)",[code])
            #cur.execute('create database if not exits Activate_Code')
            #conn.select_db('Activate_Code')
            #cur.execute('create table code1(id,varchar(50))')


if __name__=='__main__':
    store("activation_code.txt")

