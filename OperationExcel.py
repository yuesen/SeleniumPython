import xlrd
from xlutils.copy import copy

class OperationExcel(object):

    def __init__(self,file_name=None,sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = r'G:\case02.xls'
            self.sheet_id = 0
        self.data = self.get_data()    # 获取sheet内容

    def get_data(self):
        # 获取sheet的内容
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    def get_lines(self):
        # 获取单元格行数
        tables = self.data
        return tables.nrows

    def get_cell_value(self,row,col):
        # 获取某一个单元格的内容
        return self.data.cell_value(row,col)

    def write_value(self,row,col,value):
        # 写入数据   row,col,value
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row,col,value)    # 写入第几行第几列，写入的值是啥
        write_data.save(self.file_name)    # 保存文件

    def get_rows_data(self,case_id):
        # 根据对应的case_id,找到对应行的内容
        row_num = self.get_row_num(case_id)
        rows_data = self.get_row_values(row_num)
        return rows_data

    def get_row_num(self,case_id):
        # 根据对应的case_id找到对应的行号
        num = 0
        clols_data = self.get_cols_data()
        for col_data in clols_data:
            if case_id in col_data:
                return num
            num = num + 1

    def get_row_values(self,row):
        # 根据行号，找到该行的内容
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

    def get_cols_data(self,col_id=None):
        # 获取某一列的内容
        if col_id != None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return  cols





if __name__ == '__main__':
    opers = OperationExcel()
    print(opers.get_cell_value(2,2))
    # print(opers.get_data())
    print(opers.get_lines())
