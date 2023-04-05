import os

a = "pa2 < testcase/input0"
b = ".txt > myOutput0"
c = ".txt"

####### cahnge this
num = 8 
####### change this

for i in range(1, num + 1) :
  os.system(a + str(i) + b + str(i) + c)