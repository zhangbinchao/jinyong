import OperateMySQL
import json
import xlwt

def buildmatrix(x, y):
    return [[0 for j in range(y)] for i in range(x)]

def inimatrix(matrix, dic, length):
    matrix[0][0] = '+'
    for i in range(1, length):
        matrix[0][i] = dic[i]
    for i in range(1, length):
        matrix[i][0] = dic[i]
    return matrix

def countmatirx(matrix, sValue, mlength):
    for ech in sValue:
        data = str(ech[2])
        Value = json.loads(data)
        lst = []
        for med in Value:
            lst.append(med["ID"])
        for row_id in range(1,mlength):
            for col_id in range(1,mlength):
                if row_id in lst and col_id in lst:
                    matrix[row_id][col_id] += 1
                else:
                    continue
    return matrix

def main():
    url = "127.0.0.1"
    username = "root"
    pwd = "********"
    db = "jinyong"
    cu = OperateMySQL.OperateMySQL(url, username, pwd, db)
    cu.connection()
    sql = "SELECT * FROM jinyong.`peoples` "
    re = cu.select(sql)
    namelist = []
    for row in re:
        namelist.append(row[1])
    del cu
    length = len(namelist)
    matrix = buildmatrix(length, length)
    print('Matrix had been built successfully!')
    matrix = inimatrix(matrix, namelist, length)
    print('Col and row had been writen!')
    cu2 = OperateMySQL.OperateMySQL(url, username, pwd, db)
    cu2.connection()
    sql = "SELECT count(Novel) FROM jinyong.yuanshidata "  # idYuanShiData
    re = cu2.select(sql)
    for row in re:
        num = int(row[0])
        loop = int(num / 1000) + 1
    for temp in range(loop):
        sql2 = "SELECT * FROM jinyong.yuanshidata " + " limit " + str(temp * 1000) + ",1000"
        print(sql2)
        re2 = cu2.select(sql2)
        matrix = countmatirx(matrix, re2, length)
    print('Matrix had been counted successfully!')
    for i in range(1, length):
        for j in range(1, length):
            if i==j :
                matrix[i][j] =0
    # 创建一个工作簿
    workbook = xlwt.Workbook('ascii')
    # 创建工作表
    worksheet = workbook.add_sheet('my_worksheet1')
    for x in range(length):
        for y in range(length):
            worksheet.write(x, y, matrix[x][y])
    workbook.save(r'2.xls')

if __name__ == '__main__':
    main()
