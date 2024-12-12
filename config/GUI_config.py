gui_style_settings = """
            QWidget {
                font-family: 'Arial', sans-serif;
                background-color: #f4f4f9;
                color: #333;
            }
            QLineEdit {
                background-color: #fff;
                border: 2px solid #ccc;
                border-radius: 12px;
                padding: 8px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 2px solid #0078d4;
            }
            QPushButton {
                background-color: #0078d4;
                color: #fff;
                border-radius: 12px;
                padding: 10px 20px;
                font-size: 14px;
                min-width: 100px;
            }
            QPushButton:hover {
                background-color: #005a9e;
            }
            QPushButton:pressed {
                background-color: #003f6b;
            }
            QScrollArea {
                border: none;
            }
            QFrame {
                border: none;
            }
            .remove-button {
                background-color: #f44336;
                color: #fff;
                border-radius: 8px;
                padding: 6px 12px;
            }
            .remove-button:hover {
                background-color: #d32f2f;
            }
        """


lot_label_style = """
                font-size: 18px;
                font-weight: bold;
                margin: 10px 20px;  /* Increase space around the label */
                padding: 5px 10px;   /* Add padding inside the label */
                background-color: #f0f0f0;  /* Light background color */
                border: 1px solid #cccccc;  /* Subtle border */
                border-radius: 5px;  /* Rounded corners */
            """

comments_label_style = """
            font-size: 12px;               /* Set a readable font size */
            line-height: 1.6;              /* Adjust line height for readability */
            padding: 2px;                 /* Add padding around the text */
            background-color: #f9f9f9;    /* Light background color */
            border: 1px solid #d0d0d0;    /* Light border around the QTextEdit */
            border-radius: 5px;           /* Rounded corners */
            color: #333333;               /* Dark text color for contrast */
            selection-background-color: #cceeff; /* Light blue selection background */
            selection-color: #000000;     /* Dark selection text color */
        """


comments_header_style = """
            font-size: 14px;               /* Slightly larger font size for header */
            font-weight: bold;             /* Make header text bold for emphasis */
            line-height: 1.6;              /* Adjust line height for readability */
            padding: 5px 2px;             /* Add padding around the text */
            background-color: #e0e0e0;    /* Light gray background for header */
            color: #333333;               /* Dark text color for contrast */
            border: 1px solid #d0d0d0;    /* Light border around the header */
            border-radius: 5px;           /* Rounded corners */
            text-align: center;           /* Center align header text */
            selection-background-color: #cceeff; /* Light blue selection background */
            selection-color: #000000;     /* Dark selection text color */
        """
