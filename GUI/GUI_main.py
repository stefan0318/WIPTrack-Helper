# %%
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QDesktopWidget,
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

from GUI.GUI_comments_display import CommentsDisplayWindow

from config import (
    gui_style_settings,
    GUI_LOGO_PATH,
)


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
        self.ok_button = QPushButton("Preview Comments")
        self.ok_button.clicked.connect(self.open_comments_preview_display)

        # Main layout setup
        self.main_layout.addWidget(
            self.transfer_id_input
        )  # Add Transfer ID input at top
        self.main_layout.addWidget(self.ok_button)
        self.setLayout(self.main_layout)

    def open_comments_preview_display(self):
        # Collect data from all fields, including Transfer ID
        transfer_id: str = self.transfer_id_input.text()

        # Show the comments preview window
        self.preview_window = CommentsDisplayWindow(int(transfer_id))
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
