import os
import glob
import subprocess

file_name = glob.glob("*.cpp")
fn = file_name[0].split('.')[0]    # the file name of the testing program
try :
  os.remove(fn + ".exe")
except :
  pass
subprocess.run("g++ -std=c++11 -o " + fn + ' ' + file_name[0], shell = True)    # compile the program
# "-std=c++11 " is not a must but it is required in the hkust comp courses(c++)
# if you don't need to use this, replace the code with : os.system("g++ -o " + fn + ' ' + file_name[0])

if not(os.path.isfile(fn + ".exe")) :
  subprocess.run("cls", shell = True)    # clear the terminal
  os.system("cmd /k g++ -std=c++11 -o " + fn + ' ' + file_name[0])    #show the compilation error and end the program
else :

  subprocess.run("cls", shell = True)    # clear the terminal
  input_cases = glob.glob("./**/input*.txt", recursive = True)    # list of sample input files
  print("Testing for : " + fn)

  try : 
    for case in input_cases :
      c = case.split('\\')
      address = ''
      cn = c[len(c)-1]    # the filename of the input file
      for i in range(1, len(c)-1) :
        address += c[i] + '/'
      address.rstrip('/')    # the address of the input file
      
      subprocess.run(fn + " < " + address + cn + " > myOutput" + cn[5:], shell = True)    # generate myOutput file by given sample input case

###
#  Actually, I know that I can use filecmp.cmp() to compare two files.
#  However, I found that 2 files with the same content(look like the same) may have different file size due to the encoding ???
#  filecmp.cmp() may return False while 2 text file look like exactly same
#  I compare 2 files using the method below and it return True(that's what i want), so i use it
#  If you know what is the problem, please tell me.
###
      with open("myOutput" + cn[5:]) as myOut, open(address + "output" + cn[5:]) as out :
        if (myOut.read() == out.read()) :
          print(cn + " is okay.")
        else :
          print(cn + " is WRONG!!!!")    # compare myOutput file with the sample output file

    print("DONE")
  except :
    print("testing failed")
