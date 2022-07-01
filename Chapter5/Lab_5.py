"""LAB 5: EXAMINING A LIST In this lab, the task is to read a set of temperature
data (the monthly high temperatures at Heathrow Airport for 1948 through
2016) from a file and then find some basic information: the highest and low-
est temperatures, the mean (average) temperature, and the median tempera-
ture (the temperature in the middle if all the temperatures are sorted).
The temperature data is in the file lab_05.txt in the source code directory for
this chapter. Because I haven’t yet discussed reading files, here’s the code to
read the files into a list:
temperatures = []
with open('lab_05.txt') as infile:
for row in infile:
temperatures.append(int(row.strip())
You should find the highest and lowest temperature, the average, and the
median. You’ll probably want to use the min(), max(), sum(), len(),
and sort() functions/methods.
BONUS
Determine how many unique temperatures are in the list."""

temperatures = []
with open('lab_05.txt') as infile:
    for row in infile:
        temperatures.append(float(row.strip()))
print(min(temperatures)) 
#Min: 0.8

print(max(temperatures))
#Max: 28.2

print(sum(temperatures)/ len(temperatures))
#Ave: 14.848309178743966

x = sorted(temperatures)
print(x)

y = len(x)
print(y)

z = (temperatures[y//2] + temperatures[(y//2)+1]) // 2
print(z)
#Med: 22.0

unique1 =set(temperatures)
print(unique1)
name_value = len(unique1)
print(name_value)
#BONUS: 217


