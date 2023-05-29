# Run the testcases automatically for c++ assignments

Feel tired of typing "pa1 < testcase/input01.txt > myOutput01.txt" and comparing your output with the sample output again and again? Use this simple python program to do them automatically!

Basically for hkust students taking comp c++ courses (I don't know how other school are doing XD)

(However, you may watch [How if you are not hkust student but still facing similiar problem when your professor tells you to compare your output with given sample input and output?](https://github.com/hwtam/run-the-testcases-automatically-for-cpp/blob/main/README.md#how-if-you-are-not-hkust-student-but-still-facing-similiar-problem-when-your-professor-tells-you-to-compare-your-output-with-given-sample-input-and-output) before leaving.)

# How to get the "!CppTester.py"?

 - You can download the zip from < Code > in github or click [this link](https://github.com/hwtam/run-the-testcases-automatically-for-cpp/archive/refs/heads/main.zip)
 - Extract "!CppTester.py" from the zip

## How to use?
- Put the '!CppTester.py' into the same folder of your main cpp file
- Make sure ONLY the materials of this assignment are in the folder
- Just don't put other .cpp files in that folder

#

Run the "!CppTester.py"!

In the terminal, it shows : 
- the name(s) of your cpp file(s) {remove unwanted cpp files}
- the results of each testcases
- "DONE", telling you that the program ends

# Why it is not working?? - Some tips/rules

- Make sure python is installed in your computer
- Don't use python IDLE to run the !CppTester.py
  - Use IDE(VScode for example)
- [Open a new issue](https://github.com/hwtam/run-the-testcases-automatically-for-cpp-assignments/issues/new/choose)

#

You may see something like : "error", "invalid". It means that your program is WRONG.

You can try to compile your program by yourself to see what is the problem.

## How if you are not HKUST student but still facing similiar problem when your professor tells you to compare your output with given sample input and output?

You can still use this simple pyhton program!!

What you need to do is just rename your testcases in the format below:

- sample input cases -> input*.txt (* can be any string you like)
- sample output cases -> output*.txt (* should be equal to the * of the corresponding sample input case)

#

The program is unable to improve your programming skill and help you get a better grade.
