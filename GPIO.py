import RPi.GPIO as GPIO
import time

A = [0]*8

def lightUp(ledNumber, period):
    GPIO.output(chan_list, 0)
    GPIO.output(chan_list[ledNumber], 1)
    time.sleep(period)
    GPIO.output(chan_list[ledNumber], 0)

def blink(ledNumber, blinkCount, blinkPeriod):
        GPIO.output(chan_list, 0)
        for i in range(0, blinkCount):
            GPIO.output(chan_list[ledNumber], 1)
            time.sleep(blinkPeriod)
            GPIO.output(chan_list[ledNumber], 0)
            time.sleep(blinkPeriod)

def runningLight(count, period):
    GPIO.output(chan_list, 0)
    for i in range(0, count):
        for j in range(0, 8):
            GPIO.output(chan_list[j], 1)
            time.sleep(period)
            GPIO.output(chan_list[j], 0)

def runningDark(count, period):
    GPIO.output(chan_list, 1)
    for i in range(0, count):
        for j in range(0, 8):
            GPIO.output(chan_list[j], 0)
            time.sleep(period)
            GPIO.output(chan_list[j], 1)

def decToBinList(decNumber):
    GPIO.output(chan_list, 0)
    b = int(bin(decNumber)[2::])
    for i in range(0, 8):
        A[7 - i] = b % 10
        b = b // 10
    return A    

def lightNumber(number):
    GPIO.output(chan_list, 0)
    C = decToBinList(number)
    for j in range(0, 8):
        if (C[7 - j] == 1):
            GPIO.output(chan_list[j], 1)


def runningPattern(pattern, direction):
    #direction: 1 - 0 -> 7, left, -1 - 7 -> 0, right
    GPIO.output(chan_list, 0)
    C = decToBinList(pattern)
    D = [0]*8
    for k in range(0, 9):
        for i in range(0, 8):
            D[i] = C[(i + k*direction) % 8]
        for j in range(0, 8):
            if (D[7 - j] == 1):
                GPIO.output(chan_list[j], 1)
        time.sleep(1)
        GPIO.output(chan_list, 0)


def shim(ledNumber, num):
    p = GPIO.PWM(chan_list[ledNumber], 50)
    p.start(0)
    for i in range(num):
        for d in range(0, 100):
            p.ChangeDutyCycle(d)
            time.sleep(0.01)
        for d in range(100, 0, -1):
            p.ChangeDutyCycle(d)
            time.sleep(0.01)
    p.stop()

GPIO.setmode(GPIO.BCM)
chan_list = [24, 25, 8, 7, 12, 16, 20, 21]
GPIO.setup(chan_list, GPIO.OUT)

#lightUp(4, 2)
#blink(4, 5, 0.1)
#runningLight(2, 0.1)
#runningDark(2, 0.1)
#print(decToBinList(3))
#lightNumber(133)
#time.sleep(1)
#runningPattern(3, -1)
shim(5, 5)
GPIO.cleanup(chan_list)