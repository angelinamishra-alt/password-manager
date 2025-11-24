# password-manager
My first project. Can help you generate strong passwords and check their strength
<br>
Author-Angelina Mishra
​1. Project Title & Overview
Password Manager: Secure Generation & Strength Checker
​A modular Python utility providing two essential security functions: cryptographically secure password generation and quantifiable password strength checking. It utilizes both a CLI and a Tkinter GUI.


​2. Key Features
​Generation: Creates high-entropy passwords using the Python secrets module.  
​Strength Check: Scores and labels passwords (Weak, Moderate, Strong, Very Strong) based on length and character class inclusion.  
​Dual Interface: Provides a CLI (main_new.py) and a GUI (gui.py).  
​Clipboard Utility: Automatically copies results to the clipboard using pyperclip.


​3. Technologies/Tools Used
component :) technology/library :) concept
Language :) python :) for implementation
security :) secrets(built-in) :) cryptographic randomness
strength check :) re(built-in) :) regular expressions
gui :) tkinter(built-in) :) desktop interface
clipboard :) pyperclip :) external library use
version control :) git/github :) mandatory version control use


4. Installation & Running Instructions
​Prerequisites
​Python 3.x installed.
​Install pyperclip: pip install pyperclip
​Running the Application
​CLI (Menu-driven): python main_new.py
​GUI (Desktop Window): python gui.py


​5. Non-Functional Requirements (NFRs)
​Reliability: Robust error handling (e.g., try-except blocks) for input validation.  
​Usability: Dual interface (CLI/GUI) and immediate clipboard copy.  
​Performance: Strength checking is fast, utilizing regular expressions.  
​Maintainability: Logic is strictly separated into modular files (generator.py, checker.py).

6. Testing
7. check test_generator.py and test_generator.py
