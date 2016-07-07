# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
dt = map(int, raw_input().split())
print calendar.day_name[calendar.weekday(dt[2], dt[0], dt[1])].upper()