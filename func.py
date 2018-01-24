from test__mysqlmetaclass import Mysqlserver, MysqlDB, MysqlTable


class DBserver(Mysqlserver):
    pass


class Crm(MysqlDB, DBserver):
    pass


class Employee(MysqlTable, Crm):
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.search()


class Orderlist(MysqlTable, Crm):
    @classmethod
    def kw_fetchall(cls):
        __SQL = cls.select(DISTINCT='distinct', COLNAMES='order_Id', TABLES=cls.table_name)
        print(__SQL)
        res = cls.getdata(__SQL)
        print(res)


class Product(MysqlTable, Crm):
    pass


class Customer(MysqlTable, Crm):
    pass

e='''
      
        <input type="text" class="form-control" size="8" list="test_list" value="产品">
      <input type="text" class="form-control" aria-label="...">

            '''
if __name__ == '__main__':
    Orderlist.kw_fetchall()
