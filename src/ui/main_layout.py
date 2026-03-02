from PySide6.QtWidgets import QMainWindow, QVBoxLayout

class MainLayout(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nie Unite")
        self.setGeometry(100, 100, 800, 600)
    
    def setup_ui(self):
        # Setup UI components for the main layout
        main_layout = QVBoxLayout()
        # Add widgets to the main_layout as needed
    
        main_layout_widget = QWidget()
        main_layout_widget.setLayout(main_layout)
        self.setCentralWidget(main_layout_widget)