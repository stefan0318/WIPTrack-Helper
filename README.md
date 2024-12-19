# WIPTrack-Helper - Automation with Python Selenium
This project is developed to assist WIPTrack users at Sivers by automating repetitive tasks using Python Selenium for browser manipulation. It aims to improve efficiency by reducing manual input, streamlining workflows, and minimizing errors in WIPTrack operations.

## Disclaimer
This project is a work in progress and serves as an initial step toward full WIPTrack automation. Significant development is still required to make it a complete and robust solution.

## Getting started
1. Download and install Prerequisites.
2. Clone this repository.
3. Create a Virtual Enviroment.
4. Install dependencies using pip install -r requirements.txt.
5. Configure the scripts to match your WIPTrack use cases.
6. Run the automation scripts and watch Selenium handle your repetitive tasks!

## Prerequisites

   1. Install Python to your machine.
      - Download from: https://www.python.org/
      - Make sure add python path to system enviroment is enable during installation.
        
   2. Install and Configure VSCode.
      - After downloading and installing VSCode from https://code.visualstudio.com/ or the Microsoft Store, open it.
      - Install the Python Extension:
         - Go to the Extensions view in VSCode (Ctrl+Shift+X or Cmd+Shift+X on Mac).
         - Search for "Python" by Microsoft and click "Install."
           
   3. Verify Python Installation.
      - Ensure Python is installed by running the following command in your terminal or command prompt:
        ```bash
        python --version
        ```
      - If Python isn't recognized, ensure you selected "Add Python to PATH" during installation.
         - To verify PATH, open Environment Variables (on Windows) and ensure Python's directory (e.g., C:\Python39\) is included in the PATH variable.
      
   5. Make sure Git is installed on your system:
      - Windows: Download Git from https://git-scm.com/download/win.
      - macOS: Run `brew install git` (if using Homebrew) or download Git from https://git-scm.com/download/mac.
      - Linux: Run `sudo apt-get install git` (Debian/Ubuntu) or `sudo yum install git` (Fedora).

## Clone WIPTrack-Helper
   1. Open a Terminal (or Command Prompt/PowerShell on Windows).
   2. Navigate to the Desired Directory:
   Change to the folder where you want to clone the repository:
   ```bash
    cd /path/to/your/directory
   ```
   3. Clone the Repository: Run the following command:
   ```bash
  git clone https://github.com/stefan0318/WIPTrack-Helper.git
   ```

## Create a Virtual Enviroment.
   1. Open a Terminal on VSCode.
   2. Run the following commands on the terminal.
   ```bash
   python -m venv venv
   ```
   ```bash
   venv\Scripts\activate
   ```
## Install dependencies
   1. Run the following commands on the terminal to install the required libraries.
   ```bash
   pip install -r requirements.txt
   ```
## Configure the scripts
   ### Setting Up Credentials
   1. Copy `credentials.example.txt` and rename to `credentials.txt`.
   2. Fill in your credentials in `credentials.txt`.
   3. Ensure `credentials.txt` is not tracked by Git (this is handled automatically via `.gitignore`).
   4. Add your notes the the excel file and save before running the script.

## Run the code
   - To run the code, open main.py and press Shift + Enter.
   - It should open up an interactive window on VSCode and a GUI where you will be prompted to input a transfer ID.
   - Enter the transfer ID corresponding to the row that contains the notes you wish to add to each lot.
   - A second window should open with the preview of notes and lot numbers, if the details matches, press Add Notes. 

  
