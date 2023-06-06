import os
import glob
import subprocess
import sys

# a function for generating myOutput file, still in debug state
def myOut_gen(fa, ext) :
  try :
    subprocess.run("mainCPP < " + fa + " > myOutput" + ext,
                   shell=True, timeout=20, check=True)
  except subprocess.TimeoutExpired:    # if the process time exceed 20s
    subprocess.run("taskkill /IM mainCPP.exe /F /T" if os.name == 'nt'
                   else ("pkill -f mainCPP.exe") ,    # mac and linux
                   shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    os.remove("myOutput" + ext)    # stop generating myOutput file and delete it
    print(fa + " may be invalid / There is a infinte loop in your program")
  except subprocess.CalledProcessError:    # if runtime error is raised
    print("There are runtime error(s) when testing : " + fa + "\n")
  except Exception as e:    # others
    print("Error in compiling : " + fa)
    #print(e)
  else :
    return False    # return false if no error
  return True    # else return true

# clear the terminal ,from : https://stackoverflow.com/a/36941376
try :
  subprocess.run("cls||clear", shell = True)
except :
  pass

# change to the correct workspace
path = os.path.dirname(__file__)
os.chdir(path)

# ensure the correct version is tested (not the previous one)
try :
  os.remove("mainCPP.exe")
except :
  pass

# search for the cpp files
cpp_list = glob.glob("./**/*.cpp", recursive=True)

# compilation, support seperate compilation
str_o = "g++ -std=c++11 -c -o "
str_exe = "g++ -std=c++11 -o mainCPP "
flag = False
for cpp in cpp_list :
  o = os.path.basename(cpp)[:-4] + '.o '
  str_exe += o
  try :
    subprocess.run(str_o + o + cpp, shell=True, check=True)    # produce object files
  except :
    print('-----------------------------------------------------------------------')
    print("-- There are compilation error(s) in : " + cpp.lstrip('.').lstrip('/\\'))
    print('-----------------------------------------------------------------------')
    print('\n')
    flag = True

# produce executable program if no compilation error
if flag :
  sys.exit()
try :
  subprocess.run(str_exe, shell=True, check=True)
except :
  print("\nThere are compilation error(s) in the main program")
  sys.exit()


# start testing
str = 'testing : '
for cpp in cpp_list :
  str += cpp.lstrip('.').lstrip('/\\') + ' , '
print(str[:-3]+'\n')

# generate myOutput file by given sample input
input = glob.glob("./**/input*.txt", recursive=True)
output = glob.glob("./**/output*.txt", recursive=True)
for fa in input :
  fa = fa.lstrip('.').lstrip('/\\')
  myOut_t = os.path.basename(fa)[5:]
  if myOut_gen(fa, myOut_t) :
    continue

  # compare your output with the sample output
  try :
    sample = ''
    target = "output" + myOut_t
    for out in output :
      if os.path.basename(out) == target :
        sample = out
        break
    if not(sample) :
      print(target + " not found")
      continue
    with open("myOutput" + myOut_t) as myOut, open(sample) as sOut :
        if (myOut.read() == sOut.read()) :
          print(fa + " is okay.")
        else :
          print(fa + " is WRONG!!!!")
  except Exception as e:
    #print(e)    # remove the '#' in the beginning of this line to show the error
    print("Error in testing : " + fa)

# done
print("\nFinish testing")
