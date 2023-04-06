import os
import glob

os.system("cls")
file_name = glob.glob("*.exe")
fn = file_name[0].split('.')[0]
input_cases = glob.glob("./**/input*.txt")
input_cases.extend(glob.glob("./input*.txt"))

print("Testing for : " + fn)

try : 
  for case in input_cases :
    c = case.split('\\')
    address = ''
    cn = c[len(c)-1]
    for i in range(1, len(c)-1) :
      address += c[i] + '/'
    address.rstrip('/')
    
    os.system(fn + " < " + address + cn + " > myOutput" + cn[5:])

    with open("myOutput" + cn[5:]) as myOut, open(address + "output" + cn[5:]) as out :
      if (myOut.read() == out.read()) :
        print("No." + cn[5:-4] + " is okay.")
      else :
        print("No." + cn[5:-4] + " is WRONG!!!!")

  print("DONE")
except :
  print("testing failed")
