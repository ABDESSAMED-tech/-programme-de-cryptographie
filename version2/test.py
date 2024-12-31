from PyQt5.QtWidgets import QVBoxLayout, QMainWindow, QApplication, QWidget, QTabWidget, QGroupBox, QLabel
from PyQt5.QtCore import Qt

class ResponsiveMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.tab_widget = QTabWidget()
        self.central_layout = QVBoxLayout(self.central_widget)
        self.central_layout.addWidget(self.tab_widget)

        self.init_tabs()

    def init_tabs(self):
        # Create tabs with content
        tab1 = QWidget()
        tab2 = QWidget()

        # Layouts for each tab
        layout1 = QVBoxLayout(tab1)
        layout2 = QVBoxLayout(tab2)

        # Create QGroupBox widgets
        group_box1 = QGroupBox('GroupBox 1')
        label1 = QLabel('Content 1')  # Replace with your actual content
        group_box1_layout = QVBoxLayout(group_box1)
        group_box1_layout.addWidget(label1)

        group_box2 = QGroupBox('GroupBox 2')
        label2 = QLabel('Content 2')  # Replace with your actual content
        group_box2_layout = QVBoxLayout(group_box2)
        group_box2_layout.addWidget(label2)

        # Add QGroupBox widgets to layouts
        layout1.addWidget(group_box1)
        layout1.addWidget(group_box2)
        tab1.setLayout(layout1)

        group_box3 = QGroupBox('GroupBox 3')
        label3 = QLabel('Content 3')  # Replace with your actual content
        group_box3_layout = QVBoxLayout(group_box3)
        group_box3_layout.addWidget(label3)

        group_box4 = QGroupBox('GroupBox 4')
        label4 = QLabel('Content 4')  # Replace with your actual content
        group_box4_layout = QVBoxLayout(group_box4)
        group_box4_layout.addWidget(label4)

        # Add QGroupBox widgets to layouts
        layout2.addWidget(group_box3)
        layout2.addWidget(group_box4)
        tab2.setLayout(layout2)

        self.tab_widget.addTab(tab1, 'Tab 1')
        self.tab_widget.addTab(tab2, 'Tab 2')

        # Apply stylesheet to center the content
        center_stylesheet = """
            QGroupBox {
                border: 1px solid gray;
                border-radius: 9px;
                margin-top: 0.5em;
            }

            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top center;
                padding: 0 3px;
            }
        """

        group_box1.setStyleSheet(center_stylesheet)
        group_box2.setStyleSheet(center_stylesheet)
        group_box3.setStyleSheet(center_stylesheet)
        group_box4.setStyleSheet(center_stylesheet)

if __name__ == '__main__':
    app = QApplication([])
    main_window = ResponsiveMainWindow()
    main_window.showMaximized()
    app.exec_()
