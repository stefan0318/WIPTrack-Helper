import re
import pandas as pd
from config import EXCEL_FILE_PATH

df = pd.read_excel(EXCEL_FILE_PATH, sheet_name="Form1")  # type: ignore


def get_data_from_specific_row_by_id(input_id: str, col_index: int) -> str:
    # Filter the row by ID and select the column using index
    filtered_sries: pd.Series[str] = df.loc[df["ID"] == input_id].iloc[:, col_index]
    return str(filtered_sries.iloc[0])


def get_comments_data_from_excel(input_id: int):
    # Column index of "Future holds to be added Format: {Operation Number - Hold Reason}"
    comments_column_index = 9  # J column
    comments_data = get_data_from_specific_row_by_id(input_id, comments_column_index)

    # Extract operation number and comment from the comments data
    pattern = r"(\d+)\s*-\s*(.*?)(?=\s*(?:\d+\s*-|$))"
    matches = re.findall(pattern, comments_data)

    parsed_data: list[tuple[str, str]] = []
    for match in matches:
        operation_number = match[0]
        comment = match[1]
        parsed_data.append((operation_number.strip(), comment.strip()))
    return parsed_data


def get_lot_numbers_from_excel(input_id: str) -> list[str]:
    lot_numbers_column_index = 6  # G column
    lot_numbers = get_data_from_specific_row_by_id(input_id, lot_numbers_column_index)
    return lot_numbers.split("\n")
