import pymysql

class OperationMysql(object):
    def __init__(self):
        # 连接数据库,主机，用户名，密码，数据库的名（哪个数据库），端口
        self.conn = pymysql.connect(host='localhost',
                               user='root',
                               password='123456',
                               database='test01',
                               port=3306,
                               charset='utf8',
                               cursorclass = pymysql.cursors.DictCursor)
        self.cur = self.conn.cursor()       # 创建游标

    def search_one(self,sql):
        self.cur.execute(sql)
        result = self.cur.fetchone()
        return result

if __name__ == '__main__':
    op_mysql = OperationMysql()
    print(op_mysql.search_one("select * from test"))