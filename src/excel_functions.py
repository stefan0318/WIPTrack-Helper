import re
import pandas as pd
from config import EXCEL_FILE_PATH
import openpyxl

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


def write_lot_data_into_excel_file(lot_number: str) -> None:
    from .WIPTrack_login import log_in_and_find_wiptrack_lot
    from .WIPTrack_lot_functions import get_step_number, get_operation

    driver, elements = log_in_and_find_wiptrack_lot(lot_number)
    excel_file_name = f"Lot-{lot_number}-data.xlsx"
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = f"{lot_number}"  # type: ignore
    ws.append(["Step Number", "Operation Number", "Operation"])  # type: ignore
    for el in elements:
        op_number = el.accessible_name
        step_number = get_step_number(elements, op_number)
        operation = get_operation(elements, op_number)
        print(
            f"Step Number: {step_number}, Operation Number: {op_number}, , Operation: {operation}"
        )
        # Write data on an excel file
        ws.append([step_number, op_number, operation])  # type: ignore
        wb.save(excel_file_name)
