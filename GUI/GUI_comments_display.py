from PyQt5.QtWidgets import (
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

from GUI.GUI_validation_display import ValidationDisplayWindow
from src import (
    get_comments_data_from_excel,
    get_lot_numbers_from_excel,
)


class CommentsDisplayWindow(QWidget):
    def __init__(self, transfer_id: int):
        super().__init__()
        self.transfer_id = transfer_id
        self.comments_data = get_comments_data_from_excel(int(transfer_id))
        self.operation_numbers = [comment[0] for comment in self.comments_data]
        self.comments = [comment[1] for comment in self.comments_data]
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
        add_notes_button = QPushButton("Validate")
        add_notes_button.clicked.connect(self.open_validation_window)
        buttons_layout.addWidget(add_notes_button)

        # Add buttons layout to the main layout
        self.layout.addLayout(buttons_layout)

        # Set the modern stylesheet
        self.setStyleSheet(gui_style_settings)

        self.setLayout(self.layout)

    def open_validation_window(self):
        self.validation_window = ValidationDisplayWindow(
            self.transfer_id, self.comments_data
        )
        self.validation_window.show()
        self.validation_window.raise_()
        self.validation_window.activateWindow()
        self.close()
