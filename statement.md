Problem Statement- The foundational challenge addressed is the inaccuracy and inefficiency of manual calculation and presentation of student academic results. Manually aggregating marks, calculating percentages, and determining final letter grades for individual students is prone to human error and lacks an instantaneous, reliable mechanism for feedback. The project aims to solve this by providing a portable, procedural program that guarantees calculation accuracy and instant grade determination for core academic results.


Scope of the project- The project's scope is narrow and focused on demonstrating core calculation logic within a procedural, command-line environment.
Area,Scope Definition Functionality,"Limited to accepting input, performing calculations, applying a fixed grading scale, and printing a report."
Data Persistence,Out of Scope (Transient): Data is processed in memory only and is lost upon program termination (No database integration).
User Interface,Out of Scope (Console only): Limited to basic text input/output via the command line.
Customization,Out of Scope: The number of subjects (fixed at three) and the grading scale are hardcoded.


Target Users- The primary target user for this console utility is:
A Student or Developer Learning Programming: A programmer using the program as proof of concept or an exercise to learn basic programming concepts such as data types, conditional logic (if/elif), and procedural flow.  An Educator/Administrator: Quick calculations or one-off computational utility to verify results they have manually calculated with a high degree of accuracy.


High-Level Characteristics- These characteristics represent the essential functions and quality attributes of software:
Accurate Calculation Engine: Gives 100% accurate total marks and percentage calculation, based on standard arithmetic rules.
Automated Grading: Instantly provides the letter grade (A+, A, B, C, D, F) based on a fixed, hardcoded percentage scale.
Console I/O: Provides well-formatted, sequential version of input prompts and unit test style report card output to the terminal.
Portability: Can run in any standard Python 3 environment with no additional dependencies or libraries. 


