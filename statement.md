Problem Statement- The foundational challenge addressed is the inaccuracy and inefficiency of manual calculation and presentation of student academic results. Manually aggregating marks, calculating percentages, and determining final letter grades for individual students is prone to human error and lacks an instantaneous, reliable mechanism for feedback. The project aims to solve this by providing a portable, procedural program that guarantees calculation accuracy and instant grade determination for core academic results.


Scope of the project- The project's scope is narrow and focused on demonstrating core calculation logic within a procedural, command-line environment.
Area,Scope Definition
Functionality,"Limited to accepting input, performing calculations, applying a fixed grading scale, and printing a report."
Data Persistence,Out of Scope (Transient): Data is processed in memory only and is lost upon program termination (No database integration).
User Interface,Out of Scope (Console only): Limited to basic text input/output via the command line.
Customization,Out of Scope: The number of subjects (fixed at three) and the grading scale are hardcoded.


Target Users- The primary target user for this console utility is:
Students or Developers Learning Programming: Individuals using the program as a proof-of-concept or learning exercise to master fundamental programming concepts like data types, conditional logic (if/elif), and procedural flow.
Educators/Administrators: For quick, one-off calculations to verify manually calculated results, needing a high degree of calculation accuracy.


High-Level Features- These features represent the core functions and quality attributes of the program:
Accurate Calculation Engine: Provides 100% accurate total marks and percentage calculation based on standard arithmetic rules.
Automated Grading: Instantly determines the final letter grade (A+, A, B, C, D, F) based on a fixed, hardcoded percentage scale.
Console I/O: Provides clear, sequential input prompts and a distinctly formatted report card output in the terminal.
Portability: Runs on any standard Python 3 environment without requiring any external dependencies or libraries.

