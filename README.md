
#Project Name: CPT to ICD-10 Code Mapping Automation
Overview
This project automates the mapping of CPT codes to ICD-10 codes using the Find-A-Code web application. The automation process requires a subscription to the Find-A-Code service, which provides the necessary tools for CPT to ICD-10 conversions.

Files
chrome_automation.py: Automates interaction with Google Chrome to input CPT codes into the Find-A-Code website and initiate the mapping process.
processing_chunk_files_and_appending.py: Processes text files containing CPT codes, divides them into manageable chunks, submits these chunks for mapping via the automated Chrome interface, and appends the results into a consolidated CSV file.
Pre-requisites
Before running the scripts, ensure that:

You have an active subscription to Find-A-Code, which you can purchase here.
You are logged into the Find-A-Code website in Google Chrome to enable seamless automation.
Dependencies
This project relies on the following Python packages:

pandas
pyautogui
pygetwindow
pyperclip
Install these packages using the following command:

bash
Copy code
pip install pandas pyautogui pygetwindow pyperclip
How to Use
Prepare Your Environment

Ensure Python is installed on your system.
Install all required dependencies.
Ensure you have a text file containing CPT codes at the known location.
Setting Up the Text File

Place your text file containing CPT codes, with one code per line, in a known directory.
Running the Scripts

To automate the mapping process, execute the chrome_automation.py script:
bash
Copy code
python chrome_automation.py
To process the CPT code text files, divide them into chunks, and append the results, run:
bash
Copy code
python processing_chunk_files_and_appending.py
Important Notes
Logging In: Ensure you are logged into the Find-A-Code website before running the automation script to prevent any interruptions.
Chrome Interaction: The script chrome_automation.py directly interacts with the Google Chrome browser; make sure that the browser is not used for other tasks during the script execution.
