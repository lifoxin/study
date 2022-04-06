#! /usr/bin/env python3
# coding=utf-8

import re
import webbrowser

def main():


	file1 = open('www.txt')  #打开文件
	str1 = file1.read()      #读取文件
	#索引出要打开的网站
	str2 = re.findall(r'xxx.com/EX-\d+-\d+',str1)

	#打开网站
	for url in str2:
		url = "https://" + url 
		webbrowser.open(url)
		#print(url)

	#关闭文件
	file1.close()

if __name__ == "__main__":

	main()
