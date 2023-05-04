# -*- coding: UTF-8 -*-

"""
mysql类，连接mysql并进行数据库操作
@Author : linbaixiang
@Date : 2023-04-25
"""

import pymysql
from util.setting import MYSQL_HOST, MYSQL_DBNAME, MYSQL_USER, MYSQL_PASSWORD, MYSQL_PORT


class DoMysql:
    def __init__(self):
        # 有中文要存入数据库的话要加charset='utf8'
        self.conn = pymysql.connect(host=MYSQL_HOST,
                                    user=MYSQL_USER,
                                    passwd=MYSQL_PASSWORD,
                                    db=MYSQL_DBNAME,
                                    port=MYSQL_PORT,
                                    charset='utf8mb4')

        # 创建游标
        self.cursor = self.conn.cursor()

    # 返回单条数据
    def fetch_one(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    # 返回多条数据
    def fetch_chall(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def fetch_code(self):
        self.cursor.close()
        self.conn.close()

    # 判断是否有数据
    def row_count(self, sql):
        self.cursor.execute(sql)
        return self.cursor.rowcount
