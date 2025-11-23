Project Title- Student Report Card Program


Overview of the project- This is a small-scale, procedural command-line utility implemented in Python designed to automate the core academic calculation for an individual student. The project accepts basic student details and marks for three predefined subjects (English, Math, Science). Its primary function is to accurately calculate the total marks, determine the overall percentage, and assign a final letter grade based on a fixed grading scale. The program immediately displays a clean, formatted report card to the console, serving as a functional proof-of-concept for the calculation engine of a larger academic management system.


Features- The program focuses on five core functions:Data Input (FR 4.1): Prompts the user to enter the student's name, roll number, and marks for English, Math, and Science.Calculation (FR 4.2): Accurately calculates the Total Marks (out of 300) and the Overall Percentage.Grade Determination (FR 4.3): Assigns a final letter grade using a fixed conditional scale:A+ ($\geq 90\%$), A ($\geq 80\%$), B ($\geq 70\%$), C ($\geq 60\%$), D ($\geq 50\%$), F ($< 50\%$).Report Output (FR 4.4): Prints a clearly formatted report card to the console, displaying all inputs and calculated results.Data Handling (FR 4.5): Processes subject scores as floating-point numbers to support non-integer marks.


Technologies/Tools Used-
Category,Technology/Tool,Purpose
Development Language,Python 3,"Used for its clear, procedural syntax and robust mathematical capabilities."
Architecture,Procedural / Monolithic,Chosen for simplicity and rapid development of a single-purpose utility.
Libraries/Dependencies,None,The program utilizes only the Python Standard Library (built-in functions).
I/O,input() and print(),Standard Python built-in functions for console interaction.


Steps to Install & Run the Project- Since the project uses only the Python Standard Library, installation is minimal.
 Prerequisites
Ensure Python 3 (version 3.6 or newer) is installed on your operating system (Windows, macOS, or Linux).
 Running the Program
Save the Code: Save the project code into a single file, for example, report_card.py.
Open Terminal: Open your operating system's command prompt, terminal, or PowerShell.
Navigate: Change the directory to where you saved the report_card.py file.
Execute: Run the program using the Python interpreter command:python report_card.py
Follow Prompts: The program will begin execution, prompting you sequentially for the student's name, roll number, and the three subject scores.


Instructions for Testing- Testing focuses on Black Box and Boundary Value scenarios to confirm calculation accuracy and grade determination logic.
Test Case,English,Math,Science,Total (Expected),Percentage (Expected),Grade (Expected),Purpose
High Pass,95.0,90.0,92.0,277.0,92.33%,A+,Test the highest band.
Boundary (A),80.0,80.0,80.0,240.0,80.00%,A,Test the lower boundary of Grade A (≥80%).
Boundary (C),60.0,60.0,60.0,180.0,60.00%,C,Test the lower boundary of Grade C (≥60%).
Failing,40.0,30.0,45.0,115.0,38.33%,F,Test the failing band (<50%).


Verification Steps
Run the program (python report_card.py).
Input the scores for one of the test cases above.
Compare the program's output for Total Marks, Percentage, and Grade against the expected values in the table.
If the calculated results match the expected results, the system is verified as working correctly.

Navigate: Change the directory to where you saved the report_card.py file.

Execute: Run the program using the Python interpreter command:
