from pathlib import Path

# Make sure the DRF Transfer Log excel shared file is syncronized to the local machine
# Change the path by replacing the path below with the path to the local copy of the excel file OR Change USER to the name of the user on the local machine

ROOT_DIR = Path(__file__).parents[1]
CONFIG_DIR = ROOT_DIR / "config"
CREDENTIALS_FILE_PATH = str(ROOT_DIR / "credentials.txt")
GUI_LOGO_PATH = str(CONFIG_DIR / "Sivers_Semiconductors_Logo.png")

EXCEL_FILE_PATH = str(ROOT_DIR / "DFR Transfer Log.xlsx")
