# Run the testcases automatically for c++ assignments

Feel tired of typing "pa1 < testcase/input01.txt > myOutput01.txt" and comparing your output with the sample output again and again? Use this simple python program to do them automatically!

Basically for hkust students taking comp c++ courses (I don't know how other school are doing XD)

(However, you may watch [How if you are not hkust student but still facing similiar problem when your professor tells you to compare your output with given sample input and output?](https://github.com/hwtam/run-the-testcases-automatically-for-cpp/blob/main/README.md#how-if-you-are-not-hkust-student-but-still-facing-similiar-problem-when-your-professor-tells-you-to-compare-your-output-with-given-sample-input-and-output) before leaving.)

## How to get the "batch.py"?

 - You can download the zip from < Code > in github or click [this link](https://github.com/hwtam/run-the-testcases-automatically-for-cpp/archive/refs/heads/main.zip)
 - Extract "batch.py" from the zip

## How to use?
- Put the 'batch.py' into the same folder of your main cpp file
- Make sure your testcases are in/within that folder too

For example :

![before](pics/before.png)

You can see that I put the testcases into a subfolder.

Everything is fine as long as the testcases are put in/within the folder where you put your cpp file

#

Run the "batch.py"!

![after](pics/after.png)

You can see that :

- "pa2.cpp" is compiled and "pa2.exe" is built!
- "myOutput01" to "myOutput08" are generated!
- the result shown in the terminal telling you the result!

In the terminal, it shows : 
- the name of your main program
- the results of each testcases
- "DONE", telling you that the program finished successfully 

## Why it is not working?? - Some tips/rules

- Make sure python is installed in your computer.
- Your cpp file and "batch.py" should be in the same folder. Their directory should be the same.
- The sample input cases and sample output cases should be in the same folder. Their directory should be the same.
- The folder of testcases should be inside the folder of the main program unless the tescases and the main program are in the same folder.

#

If the program is not working AND you can't understand the rules, you can just follow how I put my files.

![before](pics/before.png)

If it is still not working, please report to me.

## How if you are not hkust student but still facing similiar problem when your professor tells you to compare your output with given sample input and output?

You can still use this simple pyhton program!!

What you need to do is just rename your testcases in the format below:

![before](pics/before.png)

- sample input cases -> input*.txt (* can be any string you like)
- sample output cases -> output*.txt (* should be equal to the * of the corresponding sample input case)

#

Hope it can help you!
