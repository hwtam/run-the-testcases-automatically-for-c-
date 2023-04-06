import os
import glob

os.system("cls")
file_name = glob.glob("*.exe")
fn = file_name[0].split('.')[0]    #the file name of the testing program
input_cases = glob.glob("./**/input*.txt")
input_cases.extend(glob.glob("./input*.txt"))    #list of sample input files

print("Testing for : " + fn)

try : 
  for case in input_cases :
    c = case.split('\\')
    address = ''
    cn = c[len(c)-1]    #the filename of the input file
    for i in range(1, len(c)-1) :
      address += c[i] + '/'
    address.rstrip('/')    #the address of the input file
    
    os.system(fn + " < " + address + cn + " > myOutput" + cn[5:])    #generate myOutput file by given sample input case

###
#  Actually, I know that I can use filecmp.cmp() to compare two files.
#  However, I found that 2 files with the same content(look like the same) may have different file size due to the encoding ???
#  filecmp.cmp() may return False while 2 text file look like exactly same
#  I compare 2 files using the method below and it return True(that's what i want), so i use it
#  If you know what is the problem, please tell me.
###
    with open("myOutput" + cn[5:]) as myOut, open(address + "output" + cn[5:]) as out :
      if (myOut.read() == out.read()) :
        print("No." + cn[5:-4] + " is okay.")
      else :
        print("No." + cn[5:-4] + " is WRONG!!!!")    #compare myOutput file with the sample output file

  print("DONE")
except :
  print("testing failed")
