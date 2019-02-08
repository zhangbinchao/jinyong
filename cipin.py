# -*- coding: utf-8 -*-
import sys
import importlib

stdi, stdo, stde = sys.stdin, sys.stdout, sys.stderr
importlib.reload(sys)
sys.stdin, sys.stdout, sys.stderr = stdi, stdo, stde
import jieba
from collections import Counter

class cipin:
	@staticmethod
	def tongji(namelist, namelist_1, namelist_2, namelist_3, text):

		result = [0] * (len(namelist))
		for t in range(len(result)):
			result[t] = 0
		seg_list = jieba.cut(text)
		c = Counter()
		for x in seg_list:
			if len(x) > 1 and x != '\r\n':
				c[x] += 1

		for (key, value) in c.items():
			k = "%s" % (key)
			v = int(value)

			if k in namelist:
				num = namelist.index(k)
				result[num] = result[num] + v
			elif k in namelist_1:
				num = namelist_1.index(k)
				result[num] = result[num] + v
			elif k in namelist_2:
				num = namelist_2.index(k)
				result[num] = result[num] + v
			elif k in namelist_3:
				num = namelist_3.index(k)
				result[num] = result[num] + v
			else:
				continue
		return result


