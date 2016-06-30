# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

AB = int(raw_input())
BC = int(raw_input())

deg = round(math.degrees(math.asin(AB / math.sqrt(AB **2 + BC ** 2))))
print '{theta:.0f}°'.format(theta=deg)