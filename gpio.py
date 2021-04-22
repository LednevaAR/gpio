import RPi.GPIO as GPIO
import time
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.io import wavfile

A = [0]*8

GPIO.setmode(GPIO.BCM)
chan_list = [26, 19, 13, 6, 5, 11, 9, 10]
led_list = [21, 20, 16, 12, 7, 8, 25, 24]
GPIO.setup(chan_list, GPIO.OUT)
GPIO.setup(led_list, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(4, GPIO.IN)

def decToBinList(decNumber):
    GPIO.output(chan_list, 0)
    b = int(bin(decNumber)[2::])
    for i in range(0, 8):
        A[7 - i] = b % 10
        b = b // 10
    return A

def num2dac(value):
    GPIO.output(chan_list, 0)
    C = decToBinList(value)
    for j in range(0, 8):
        if (C[j] == 1):
            GPIO.output(chan_list[j], 1)
    time.sleep(0)

def first(value):
    while (value != -1):
        print("Enter value (-1 to exit)>")
        try:
            value = int(input())
            num2dac(value)
        except ValueError: print("Некорректные данные поданы на ввод. Попробуйте еще раз")
        num = float((3.3/255)*value)
        print(value , " = ", "%.2f" % round(num, 2), "V")

def second(value):
    while(1):
        for i in range(0, 256):
            num2dac(i)
            time.sleep(0.005)
            if (GPIO.input(4) == 0):
                break
        num = float((3.3/255)*i)
        print("Digital value:", i, "Analog value:", "%.1f" % round(num, 1), "V")
        GPIO.output(chan_list, 0)

def bint(k, j):
    while (round(j / 2) > 0):
        num2dac(k)
        time.sleep(0.005)
        if (GPIO.input(4) == 0):
            return bint(k - j, round(j / 2))
        if (GPIO.input(4) == 1): return bint(k + j, round(j / 2))
    return k

def third(value):
    while(1):
        i = bint(58, 29)
        num = float((3.3/255)*i)
        print("Digital value:", i, "Analog value:", "%.1f" % round(num, 1), "V")
        GPIO.output(chan_list, 0)

def decToBinList(decNumber):
    b = int(bin(decNumber)[2::])
    for i in range(0, 8):
        A[7 - i] = b % 10
        b = b // 10
    return A    

def lightNumber(number):
    C = decToBinList(number)
    for j in range(0, 8):
        if (C[j] == 1):
            GPIO.output(led_list[j], 1)
        if (C[j] == 0):
            GPIO.output(led_list[j], 0)

def fourth(value):
    i = 0
    while(1):
        GPIO.output(chan_list, 0)
        for i in range(0, 256):
            num2dac(i)
            time.sleep(0.001)
            if (GPIO.input(4) == 0):
                break
        num = float((3.3/255)*i)
        print("Digital value:", i, "Analog value:", "%.1f" % round(num, 1), "V")
        if (0 < i) & (i < 14):
            lightNumber(1)

        if (14 <= i) & (i < 28):
            lightNumber(3)

        if (28 <= i) & (i < 42):
            lightNumber(7)

        if (42 <= i) & (i < 56):
            lightNumber(15)

        if (56 <= i) & (i < 70):
            lightNumber(31)

        if (70 <= i) & (i < 84):
            lightNumber(63)

        if (84 <= i) & (i < 98):
            lightNumber(127)
        if (98 <= i) & (i < 115):
            lightNumber(255)
        time.sleep(0.1)
            
        

GPIO.output(chan_list, 0)
GPIO.output(led_list, 0)
#first(0)
#second(0)
#third(0)
fourth(0)
GPIO.cleanup(chan_list)
GPIO.cleanup(led_list)