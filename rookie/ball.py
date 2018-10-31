#!/usr/bin/env python3

import random
import math
'这是一个彩票生成程序, 可以随机生成双色球和大乐透'
 
class newBall:
    _redQuantity = 0
    _blueQuantity = 0
    _redMax = 0
    _blueMax = 0
    _oneRecord = ()
    

    #类的初始化
    def __init__(self, redMax, redQuantity, blueMax, blueQuantity,kind):
        self._redMax = redMax
        self._redQuantity = redQuantity
        self._blueQuantity = blueQuantity
        self._blueMax = blueMax
        self.kind = kind
    #生成一组新的数据
    def produce_new(self):
        #从一个队列里面随机选取self._redQuantity数目的数字
        redBallList = range(1, self._redMax + 1)
        redNewList = random.sample(redBallList, self._redQuantity)
        redNewList = sorted(redNewList)
        #随机生成蓝球
        blueBallList = range(1, self._blueMax + 1)
        blueNewList = random.sample(blueBallList, self._blueQuantity)
        self._oneRecord = redNewList + blueNewList
    
    #在console里面显示结果
    def showResult(self):
        print(self.kind,'\033[40;31m',self._oneRecord[:self._redQuantity],'\033[40;34m',self._oneRecord[self._redQuantity:],'\033[0m')
 
#双色球规则：33个红球中抽取6个，16个蓝球中抽取1个
redball = newBall(33, 6, 16, 1,"双色球6+1")
redball.produce_new()
redball.showResult()
#大乐透规则：35个红球中抽取5个，12个蓝球中抽取2个
sevenBall = newBall(35, 5, 12, 2,"大乐透5+2")
sevenBall.produce_new()
sevenBall.showResult()
