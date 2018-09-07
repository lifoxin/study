#!/usr/bin/env python3

import calendar

yy = int(input("输入年份： "))
mm = int(input("输入月份： "))

#打印日历
print(calendar.month(yy,mm))
