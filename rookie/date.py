#! /usr/bin/env python3
# coding=utf-8

import datetime

def main():

	d1 = datetime.datetime(2019,11,18)
	now = datetime.datetime.now()
	print((now-d1).days)

if __name__ == "__main__":

   main()
