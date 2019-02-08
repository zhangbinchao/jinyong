# -*- coding: UTF-8 -*-
import urllib.request
from bs4 import BeautifulSoup
import re

class PaChong:
	def __init__(self, URL, URL_ID, URL_Base):
		self.URL = URL
		self.URL_ID = URL_ID
		self.URL_Base = URL_Base
		self.listpath = None

	def OpenSeeion(self):  # 获取小说所有章节链接；
		try:
			respond = urllib.request.urlopen(self.URL)
			html = respond.read()
			soup = BeautifulSoup(html, 'lxml', from_encoding='utf-8')
			OringialPath = soup.find_all(class_="mlist");
			pattern = re.compile('(?<=href=").*?(?=")')
			self.listpath = re.findall(pattern, str(OringialPath))
		except:
			print('Error')

	def gettext(self, sessionURL):  # 获取该章节所有段落
		web = self.URL_Base + sessionURL
		respond = urllib.request.urlopen(web)
		html = respond.read()
		soup = BeautifulSoup(html, 'lxml', from_encoding='utf-8')
		pattern = re.compile('(?<=<p>).*?(?=</p>)')
		text = re.findall(pattern, str(soup))
		return text
