import json

class OperationJson(object):

    def __init__(self):
        self.data = self.read_data()   # 读取json文件

    def read_data(self):
        # 读取json文件,整个文件加载出来了
        with open('G:\login.json',encoding='utf-8') as fp:
            data = json.load(fp)
            return data

    def get_data(self,id):
        # 根据关键字获取数据，根据login获取后边的请求数据
        return self.data[id]

if __name__ == '__main__':
    opjson = OperationJson()
    # print(opjson.get_data("zhuce"))
    print(opjson.read_data())


