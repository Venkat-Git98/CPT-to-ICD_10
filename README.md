# CPT to ICD-10 Code Mapping Automation

## Overview
This project automates the mapping of CPT codes to ICD-10 codes utilizing the [Find-A-Code](https://www.findacode.com/tools/map-a-code/cpt-hcpcs-pcs.php) web application. It simplifies the process of converting multiple CPT codes into their corresponding ICD-10 codes through an automated browser-based interaction, which is particularly useful for healthcare data analysts and medical billing professionals.

## Project Files
- **chrome_automation.py**: Handles the automation of the Google Chrome browser to navigate the Find-A-Code website and input CPT codes for mapping.
- **processing_chunk_files_and_appending.py**: Manages the reading of CPT codes from text files, processes them in chunks, and appends the results into a single CSV file after conversion.

## Requirements
Before running the scripts, users must ensure the following:
- An active subscription to Find-A-Code is required for access to the mapping tools. Subscriptions can be purchased [here](https://www.findacode.com/sign-up.html).
- The user must be logged into the Find-A-Code website on Google Chrome to ensure uninterrupted automation.

## Dependencies
This project depends on several Python libraries listed below. These can be installed via pip:
\`\`\`
pip install pandas pyautogui pygetwindow pyperclip
\`\`\`

## Setup Instructions
1. **Environment Setup:**
   - Install Python and the required dependencies.
   - Log in to the Find-A-Code website in Google Chrome to prepare for automation.

2. **Text File Preparation:**
   - Prepare a text file containing CPT codes, listed one per line, and place it in a specified directory.

3. **Execution:**
   - Run \`chrome_automation.py\` to start the automation process in Google Chrome:
     \`\`\`bash
     python chrome_automation.py
     \`\`\`
   - Execute \`processing_chunk_files_and_appending.py\` to process CPT code files, automate their submission for mapping, and append the results:
     \`\`\`bash
     python processing_chunk_files_and_appending.py
     \`\`\`

## Usage
To automate the entire process of mapping CPT codes to ICD-10 codes:
1. Ensure you are logged into Find-A-Code.
2. Adjust script parameters as necessary to match your system setup, particularly screen coordinates used in \`pyautogui\`.
3. Run the scripts as per the instructions in the setup section.

## Note
The automation script interacts directly with the Google Chrome browser. Ensure that the browser is not used for other activities during the script's execution to avoid interruptions.

