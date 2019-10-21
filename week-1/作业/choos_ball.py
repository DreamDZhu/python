#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     choos_ball.py
   Description :
   date：          2019-10-21
-------------------------------------------------
"""
red_balls = []
blue_balls = []

while True:
    if len(red_balls) < 6:
        ball_num = input(f"\033[31m[{len(red_balls)+1}]select red ball:")
        if not ball_num.isdigit():
            print("please input num")
            continue
        ball_num = int(ball_num)
        if ball_num < 1 or ball_num > 32:
            print("only can select n between 1-32")
            continue
        if ball_num in red_balls:
            print(f"number {ball_num} is already exist in red ball list")
            continue
        red_balls.append(ball_num)
    elif len(blue_balls) < 2:
        ball_num = input(f"\033[34m[{len(blue_balls)+1}]select blue ball:")
        if not ball_num.isdigit():
            print("please input num")
            continue
        ball_num = int(ball_num)
        if ball_num < 1 or ball_num > 16:
            print("only can select n between 1-16")
            continue
        if ball_num in blue_balls:
            print(f"number {ball_num} is already exist in blue ball list")
            continue
        blue_balls.append(ball_num)
    else:
        break

print(f"\033[30mRed ball: {red_balls}")
print(f"Blue ball: {blue_balls}")
print("Good Luck")
