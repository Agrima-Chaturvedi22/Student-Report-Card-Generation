Project Title- Student Report Card Program

Project Summary- This is a procedural command-line tool developed in Python aimed at automating the essential academic computations for a single student. The project receives student information and scores for three specific subjects (English, Math, Science). Its main purpose is to compute the total marks calculate the overall percentage and allocate a final letter grade according to a set grading system. The program immediately displays a clean, formatted report card to the console, serving as a functional proof-of-concept for the calculation engine of a larger academic management system.


Features- The program focuses on five core functions:
Data Input: Prompts the user to enter the student's name, roll number, and marks for English, Math, and Science.
Calculation: Accurately calculates the Total Marks (out of 300) and the Overall Percentage.
Grade Determination: Assigns a final letter grade using a fixed conditional scale:A+ ($\geq 90\%$), A ($\geq 80\%$), B ($\geq 70\%$), C ($\geq 60\%$), D ($\geq 50\%$), F ($< 50\%$).
Report Output: Prints a clearly formatted report card to the console, displaying all inputs and calculated results.
Data Handling: Processes subject scores as floating-point numbers to support non-integer marks.


Technologies/Tools Used: Python 3, Technology/Tool, Purpose Development Language,"Used for its robust mathematical capabilities and clear, procedural syntax."
Procedural/Monolithic Architectureselected due to its ease of use and quick development of a single-purpose tool.
Libraries and DependenciesNot at allThe Python Standard Library (built-in functions) is the only library used by the program.
I/O, input(), and print() are standard Python built-in console interaction functions.


How to Install & Run the project - Since this only uses Python Standard libraries installation is minimal.
Prerequisites
Make sure Python 3 (let’s say version 3.6 or higher) is installed on your computer (Windows, macOS or Linux).
Running the Program
Save the Code Save the project code in a file, report_card for instance. py.
Open your terminal: Open prompt, terminal or PowerShell of your operating system.
Navigate: cd to the directory where you saved report_card. py file.
Execute: Run the program using the Python interpreter command:python report_card.py
Follow Prompts: The program will begin execution, prompting you sequentially for the student's name, roll number, and the three subject scores.


Instructions for Testing- Testing focuses on Black Box and Boundary Value scenarios to confirm calculation accuracy and grade determination logic.
Test Case,English,Math,Science,Total (Expected),Percentage (Expected),Grade (Expected),Purpose
High Pass,95.0,90.0,92.0,277.0,92.33%,A+,Test the highest band.
Boundary (A),80.0,80.0,80.0,240.0,80.00%,A,Test the lower boundary of Grade A (≥80%).
Boundary (C),60.0,60.0,60.0,180.0,60.00%,C,Test the lower boundary of Grade C (≥60%).
Failing,40.0,30.0,45.0,115.0,38.33%,F,Test the failing band (<50%).


Verification Steps
Run the program (python report_card. py).
For one of the above test cases input scores.
Check your program's output for Total Marks, Percentage and Grade with the above table value.
If the computed values and expected values are found same, system is tested successfully.
Navigate: Change the directory to where you saved the report_card.py file.
Execute: Run the program using the Python interpreter command
