# -*- coding: utf-8 -*-
"""main.py"""
import geatpy as ea # import geatpy
from MyProblem import MyProblem# 导入自定义问题接口
"""=========================实例化问题对象==========================="""
problem = MyProblem() # 实例化问题对象
"""===========================种群设置=============================="""
Encoding = 'RI' # 编码方式
NIND = 100 # 种群规模
Field = ea.crtfld(Encoding, problem.varTypes, problem.ranges,problem.borders) # 创建区域描述器
population = ea.Population(Encoding, Field, NIND) #
#实例化种群对象（此时种群还没被真正初始化，仅仅是生成一个种群对象）
"""=========================算法参数设置============================"""
myAlgorithm = ea.moea_NSGA2_templet(problem, population) #实例化一个算法模板对象
myAlgorithm.MAXGEN = 200 # 最大遗传代数
myAlgorithm.drawing = 1 # 设置绘图方式

"""===================调用算法模板进行种群进化=======================
调用run执行算法模板，得到帕累托最优解集NDSet。
NDSet是一个种群类Population的对象。
NDSet.ObjV为最优解个体的目标函数值；NDSet.Phen为对应的决策变量值。
详见Population.py中关于种群类的定义。
"""
# NDSet = myAlgorithm.run() # 执行算法模板，得到非支配种群
# NDSet.save()
#
# # 输出
# print('用时：%f 秒'%(myAlgorithm.passTime))
# print('评价次数：%d 次'%(myAlgorithm.evalsNum))
# print('非支配个体数：%d 个'%(NDSet.sizes))
# print('单位时间找到帕累托前沿点个数：%d 个'%(int(NDSet.sizes // myAlgorithm.passTime)))

import csv

with open(r'C:\Users\Lenovo\Nsga2Test\NSGAIIDemo\Result\ObjV.csv') as f:
    reader = csv.reader(f)

    for row in reader:
        print(row)
# # 计算指标
# PF = problem.getReferObjV() # 获取真实前沿
# print(PF.shape)
# print(NDSet.ObjV.shape)
# if PF is not None and NDSet.sizes != 0:
#     GD = ea.indicator.GD(NDSet.ObjV, PF) # 计算GD指标
#     IGD = ea.indicator.IGD(NDSet.ObjV, PF) # 计算IGD指标
#     HV = ea.indicator.HV(NDSet.ObjV, PF) # 计算HV指标
#     Spacing = ea.indicator.Spacing(NDSet.ObjV) # 计算Spacing指标
#     print('GD: %f'%GD)
#     print('IGD: %f'%IGD)
#     print('HV: %f'%HV)
#     print('Spacing: %f'%Spacing)
# """=====================进化过程指标追踪分析========================"""
# if PF is not None:
#     metricName = [['IGD'], ['HV']]
#     [NDSet_trace, Metrics] = ea.indicator.moea_tracking(myAlgorithm.pop_trace, PF,
#     metricName, problem.maxormins)
#     # 绘制指标追踪分析图
#     ea.trcplot(Metrics, labels = metricName, titles = metricName)