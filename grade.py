#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 10:44:22 2022

@author: zionn
"""

# 讓學生輸入成績，輸出「及格/不及格」
grade = input('輸入成績： ')

grade_new = int(grade)

if grade_new >= 60:
    print('恭喜你及格了')
else:
    print('抱歉你不及格')