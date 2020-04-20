#! /usr/bin/env python3
# coding=utf-8

import datetime

def main():

	d1 = datetime.datetime(2019,11,18)
	now = datetime.datetime.now()
	a = (now-d1).days
	print("我和珊珊认识有 {} 天了!".format(a))

if __name__ == "__main__":

   main()
