# list filtering
# problem: record daily temperatures above 30 degrees 
# input: daily tempeture in degrees (list)(whole numbers)
daily_temperature = [0,19,20,25,28,29,30]

# output: temperature listed above 30
hot_days = []

for temperature in daily_temperature:
    if temperature  > 30:
        hot_days = hot_days + [temperature]

print(hot_days)
