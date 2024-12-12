# %%
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QLabel,
    QHBoxLayout,
    QDesktopWidget,
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

from config import (
    gui_style_settings,
    lot_label_style,
    comments_label_style,
    comments_header_style,
    GUI_LOGO_PATH,
)

from src import (
    log_in_and_find_wiptrack_lot,
    add_comments_to_lot,
    change_lot_from_exisiting_lot,
    get_comments_data_from_excel,
    get_lot_numbers_from_excel,
)


class CommentsDisplayWindow(QWidget):
    def __init__(self, transfer_id: str, comments_data: list[tuple[str, str]]):
        super().__init__()
        self.transfer_id = transfer_id
        self.comments_data = comments_data
        self.operation_numbers = [comment[0] for comment in comments_data]
        self.comments = [comment[1] for comment in comments_data]
        self.lot_numbers = get_lot_numbers_from_excel(int(transfer_id))  # type: ignore
        self.remaining_lot_numbers = self.lot_numbers[:]  # Copy of the lot numbers list
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Comments Preview")
        self.setWindowIcon(QIcon(GUI_LOGO_PATH))
        # Get the screen's resolution
        screen = QDesktopWidget().screenGeometry()

        window_width = 600
        window_height = 600

        # Calculate the position to center the window
        x_pos = ((screen.width() - window_width) // 2) - 600
        y_pos = ((screen.height() - window_height) // 2) - 200

        self.setGeometry(x_pos, y_pos, window_width, window_height)

        # Main layout
        self.layout = QVBoxLayout()

        transfer_id_label = QLabel(f"Transfer ID: {self.transfer_id}")
        transfer_id_label.setStyleSheet(
            "font-weight: bold; font-size: 30px; margin-bottom: 10px;"
        )
        transfer_id_label.setFixedHeight(50)
        transfer_id_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(transfer_id_label)

        lot_number_display_label = QLabel("Lot Numbers:")
        lot_number_display_label.setStyleSheet(
            "font-weight: bold; font-size: 15px; margin-bottom: 5px;"
        )
        lot_number_display_label.setFixedHeight(30)
        lot_number_display_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(lot_number_display_label)

        # Lot numbers and Remove buttons
        self.lot_numbers_remove_buttons = []
        for lot_number in self.lot_numbers:
            lot_number_layout = QHBoxLayout()

            # Create label for lot number
            lot_number_label = QLabel(lot_number)
            lot_number_label.setAlignment(Qt.AlignCenter)
            # Set improved styling
            lot_number_label.setStyleSheet(lot_label_style)
            lot_number_layout.addWidget(lot_number_label)

            self.layout.addLayout(lot_number_layout)

        comments_header_layout = QHBoxLayout()
        operation_number_header_label = QLabel("Operation\nNumber")
        operation_number_header_label.setStyleSheet(comments_header_style)
        operation_number_header_label.setFixedSize(80, 50)
        operation_number_header_label.setAlignment(Qt.AlignCenter)
        comments_header_layout.addWidget(operation_number_header_label)

        notes_header_label = QLabel("Note")
        notes_header_label.setStyleSheet(comments_header_style)
        notes_header_label.setAlignment(Qt.AlignCenter)
        notes_header_label.setFixedSize(500, 50)
        comments_header_layout.addWidget(notes_header_label)
        self.layout.addLayout(comments_header_layout)

        # Display comments in QlineEdit widgets
        for operation_number, comment in zip(self.operation_numbers, self.comments):
            note_layout = QHBoxLayout()
            operation_number_label = QLineEdit(operation_number)
            operation_number_label.setReadOnly(True)
            operation_number_label.setStyleSheet(comments_label_style)
            # Fix size of the QLineEdit (width, height in pixels)
            operation_number_label.setFixedSize(80, 25)
            operation_number_label.setAlignment(Qt.AlignCenter)
            note_layout.addWidget(operation_number_label)

            comment_label = QLineEdit(comment)
            comment_label.setReadOnly(True)
            comment_label.setStyleSheet(comments_label_style)
            comment_label.setAlignment(Qt.AlignLeft)
            note_layout.addWidget(comment_label)

            self.layout.addLayout(note_layout)

        # Horizontal layout for buttons
        buttons_layout = QHBoxLayout()

        # "Close" button
        close_button = QPushButton("Close")
        close_button.clicked.connect(self.close)
        buttons_layout.addWidget(close_button)

        # "Add Notes" button
        add_notes_button = QPushButton("Add Notes")
        add_notes_button.clicked.connect(self.add_notes)
        buttons_layout.addWidget(add_notes_button)

        # Add buttons layout to the main layout
        self.layout.addLayout(buttons_layout)

        # Set the modern stylesheet
        self.setStyleSheet(gui_style_settings)

        self.setLayout(self.layout)

    def add_notes(self):
        driver = log_in_and_find_wiptrack_lot(self.lot_numbers[0])
        add_comments_to_lot(driver, self.operation_numbers, self.comments)
        print("\n")
        print(f"All comments added to lot {self.lot_numbers[0]} successfully.")
        print("\n" * 2)
        if len(self.remaining_lot_numbers) > 1:
            for lot_number in self.remaining_lot_numbers[1:]:
                change_lot_from_exisiting_lot(driver, lot_number)
                add_comments_to_lot(driver, self.operation_numbers, self.comments)
                print("\n")
                print(f"All comments added to lot {lot_number} successfully.")
                print("\n" * 2)


class WIPTrackAutoCommentHelper(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.comments_data = []

    def init_ui(self):
        self.setWindowTitle("WIPTrack Auto Comment Helper")
        self.setWindowIcon(QIcon(GUI_LOGO_PATH))

        # Get the screen's resolution
        screen = QDesktopWidget().screenGeometry()

        window_width = 400
        window_height = 100

        # Calculate the position to center the window
        x_pos = (screen.width() - window_width) // 2
        y_pos = (screen.height() - window_height) // 2

        self.setGeometry(x_pos, y_pos, window_width, window_height)

        # Set the modern stylesheet
        self.setStyleSheet(gui_style_settings)

        # Main layout
        self.main_layout = QVBoxLayout()

        # Transfer ID input at the top
        self.transfer_id_input = QLineEdit()
        self.transfer_id_input.setPlaceholderText("Transfer ID")
        self.transfer_id_input.setStyleSheet("margin-bottom: 20px;")

        # OK button
        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.save_data)

        # Main layout setup
        self.main_layout.addWidget(
            self.transfer_id_input
        )  # Add Transfer ID input at top
        self.main_layout.addWidget(self.ok_button)
        self.setLayout(self.main_layout)

    def save_data(self):
        # Collect data from all fields, including Transfer ID
        transfer_id = self.transfer_id_input.text()
        comments_data = get_comments_data_from_excel(int(transfer_id))
        self.comments_data = comments_data

        # Show the comments preview window
        self.preview_window = CommentsDisplayWindow(transfer_id, comments_data)
        self.preview_window.show()


def run_helper_app():
    # Check for an existing QApplication instance
    app = QApplication.instance()
    if not app:  # Create a new instance if none exists
        app = QApplication(sys.argv)

    window = WIPTrackAutoCommentHelper()
    window.show()
    window.raise_()  # Bring the window to the front
    window.activateWindow()  # Make the window active and focused
    app.exec_()  # Run the application event loop


if __name__ == "__main__":
    comments_data = run_helper_app()
    print(comments_data)

# %%
