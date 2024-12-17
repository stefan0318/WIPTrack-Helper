from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import time
from src.WIPTrack_login import operator_number


def get_op_num_elements(driver: webdriver.Edge):
    """
    Returns a list of operation number elements.
    """
    elements = driver.find_elements(By.XPATH, "//a[@title='VIEW LINKED DOCS']")
    return elements


def validate_operation_numbers(driver: webdriver.Edge, operation_numbers: list[str]):
    """
    This function checks if there are any duplicated operation numbers in the list of operation number elements.
    """
    operation_number_elements: list[WebElement] = get_op_num_elements(driver)
    op_numbers_in_lot: list[str] = []
    for el in operation_number_elements:
        operation_number = el.accessible_name
        if operation_number in op_numbers_in_lot:
            raise ValueError(f"Duplicated operation number: {operation_number}")
        op_numbers_in_lot.append(operation_number)
    for op_number in operation_numbers:
        if op_number not in op_numbers_in_lot:
            raise ValueError(f"Operation number {op_number} not found.")


def click_ADD_NOTE(operation_number_element: WebElement):
    parent_td = operation_number_element.find_element(
        By.XPATH, "./.."
    )  # Go to the parent <td>
    grand_parent_td = parent_td.find_element(By.XPATH, "./..")  # Go to the parent <>
    all_links = grand_parent_td.find_elements(By.TAG_NAME, "a")
    middle_element = all_links[1]  # The second link is the ADD NOTE link
    middle_element.click()


def filter_op_number_element_by_op_number(
    op_number: str, elements: list[WebElement]
) -> WebElement | None:
    """
    This function filters the operation number elements by operation number.
    """
    for el in elements:
        operation_number = el.accessible_name
        if operation_number == op_number:
            return el
    return None


def add_comments_to_lot(
    driver: webdriver.Edge,
    operation_numbers: list[str],
    comments: list[str],
):
    """
    This function adds comments to the operation numbers.
    """
    op_number_elements = get_op_num_elements(driver)
    for comment, OP_number in zip(comments, operation_numbers):
        print("-" * 15)
        print(f"Operation number: {OP_number}\nComment: {comment}")
        op_number_element = filter_op_number_element_by_op_number(
            OP_number, op_number_elements
        )
        if op_number_element is None:
            raise ValueError(f"Operation number {OP_number} not found.")
        click_ADD_NOTE(op_number_element)
        time.sleep(0.3)
        driver.switch_to.window(driver.window_handles[1])

        text_area = driver.find_element(By.XPATH, "//textarea[@name='NewNotes']")
        text_area.send_keys(comment)

        userID_field = driver.find_element(By.XPATH, "//input[@name='UserID']")
        userID_field.send_keys(operator_number)

        save_new_notes_button = driver.find_element(
            By.XPATH, "//input[@value='Save New Note']"
        )
        # save_new_notes_button.click()

        driver.close()
        driver.switch_to.window(driver.window_handles[0])


def change_lot_from_exisiting_lot(driver: webdriver.Edge, new_lot_number: str):
    driver.find_element(By.XPATH, "//input[@name='LotID']").send_keys(new_lot_number)
    driver.find_element(By.XPATH, "//input[@type='Submit']").click()


def get_all_td_elements(op_number_element: WebElement) -> list[WebElement]:
    parent_td = op_number_element.find_element(
        By.XPATH, "./.."
    )  # Go to the parent <td>
    grand_parent_td = parent_td.find_element(By.XPATH, "./..")  # Go to the parent <tr>
    all_td_elements = grand_parent_td.find_elements(By.TAG_NAME, "td")
    return all_td_elements


def get_step_number(op_number_elements: list[WebElement], op_number: str) -> str:
    el = filter_op_number_element_by_op_number(op_number, op_number_elements)

    all_td_elements = get_all_td_elements(el)
    step_number = all_td_elements[0].accessible_name
    step_number = step_number.split(" ")[0]
    return step_number


def get_operation(op_number_elements: list[WebElement], op_number: str) -> str:
    el = filter_op_number_element_by_op_number(op_number, op_number_elements)
    all_td_elements = get_all_td_elements(el)
    operation = all_td_elements[5].accessible_name
    return operation
