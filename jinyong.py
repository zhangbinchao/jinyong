# encoding:utf-8
import OperateMySQL
import spider
import cipin
import json
import time


def getname(namelist, nameliet_1, nameliet_2, nameliet_3):
	url = "127.0.0.1"
	username = "root"
	pwd = "********"
	db = "jinyong"
	cu = OperateMySQL.OperateMySQL(url, username, pwd, db)
	cu.connection()
	sql = "SELECT * FROM jinyong.`peoples` "
	re = cu.select(sql)

	for row in re:
		nameID = row[0]
		namelist.append(row[1])
		if len(str(row[2])) != 0:
			nameliet_1.append(row[2])
		if len(str(row[3])) != 0:
			nameliet_2.append(row[3])
		if len(str(row[4])) != 0:
			nameliet_3.append(row[4])
	del cu

def main():
	url = "127.0.0.1"
	username = "root"
	pwd = "********"
	db = "jinyong"
	cu2 = OperateMySQL.OperateMySQL(url, username, pwd, db)
	cu2.connection()

	namelist = []
	nameliet_1 = []
	nameliet_2 = []
	nameliet_3 = []
	getname(namelist, nameliet_1, nameliet_2, nameliet_3)

	URL = []
	# URL.append("http://www.jinyongwang.com/fei/")  # 飞狐外传
	# URL.append("http://www.jinyongwang.com/xue/")  # 雪山飞狐
	# URL.append("http://www.jinyongwang.com/lian/")  # 连城诀
	# URL.append("http://www.jinyongwang.com/tian/")  # 天龙八部
	# URL.append("http://www.jinyongwang.com/she/")  # 射雕英雄传
	# URL.append("http://www.jinyongwang.com/bai/")  # 白马啸西风
	# URL.append("http://www.jinyongwang.com/lu/")  # 鹿鼎记
	# URL.append("http://www.jinyongwang.com/xiao/")  # 笑傲江湖
	# URL.append("http://www.jinyongwang.com/shu/")  # 书剑恩仇录
	# URL.append("http://www.jinyongwang.com/shen/")  # 神雕侠侣
	# URL.append("http://www.jinyongwang.com/xia/")  # 侠客行
	URL.append("http://www.jinyongwang.com/yi/")  # 倚天屠龙记
	# URL.append("http://www.jinyongwang.com/bi/")  # 碧血剑
	# URL.append("http://www.jinyongwang.com/yuan/")  # 鸳鸯刀
	# URL.append("http://www.jinyongwang.com/yue/")  # 越女剑
	URL_Base = "http://www.jinyongwang.com"
	for i in range(len(URL)):
		cu = spider.PaChong(URL[i], i + 1, URL_Base)
		time.sleep(4)
		cu.OpenSeeion()
		for j in range(24,len(cu.listpath)):

			temp = cu.gettext(cu.listpath[j])
			print(cu.listpath[j])
			try:
				for text in temp:
					# print text
					print(text)
					resultJieDian = cipin.cipin.tongji(namelist, nameliet_1, nameliet_2, nameliet_3, text)
					li = list(set(resultJieDian))
					if len(li) == 1:
						continue
					data = []
					for t in range(len(resultJieDian)):
						if resultJieDian[t] != 0:
							dic = {}
							dic["ID"] = t
							dic["Nm"] = resultJieDian[t]
							data.append(dic)
					in_json = json.dumps(data)
					sql = "INSERT INTO jinyong.yuanshidata SET Novel = " + str(i + 1) + ", Dtat = '" + str(in_json) + "'"
					# print sql
					re = cu2.excute(sql)
					if re == 0:
						print('Error' + cu.listpath[j])

						m = input()
					del sql
					del resultJieDian
					del li
			except:
				continue

		del cu


if __name__ == "__main__":
	main()
