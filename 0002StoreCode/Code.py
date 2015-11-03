#!/usr/bin/env python
# coding=utf-8

import mysql.connector

def store_mysql(filepath):
    conn = mysql.connector.connect(user = 'root', password = '', database = 'Code')
    cursor = conn.cursor()

    # 判断表是否已经存在
    cursor.execute('show tables in Code;')
    tables = cursor.fetchall()
    findtables = False
    for table in tables:
        if 'code' in table:
            findtables = True
    if not findtables:
        cursor.execute('''
                CREATE TABLE `Code`.`code` (
                `id` INT NOT NULL AUTO_INCREMENT,
                `code` VARCHAR(50) NOT NULL,
                PRIMARY KEY (`id`));
        ''')

    f = open(filepath, 'rb')
    for line in f.readlines():
        code = line.strip()
        cursor.execute("insert into Code.code (code) values(%s);", [code])

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    store_mysql('activation_code.txt')
