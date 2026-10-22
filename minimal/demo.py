import sys

### PySide6
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

### fluent-qt
import fluentqt
from fluentqt.windowing import Window
from fluentqt.basicinput import Button

if __name__ == "__main__":
    fluentqt.prepare_high_dpi_application()
    app = QApplication(sys.argv)
    fluentqt.initialize_resources()
    app.setFont(fluentqt.font_for_role(fluentqt.FontRole.Body))

    w = Window()
    w.setWindowTitle("FluentQt Hello world!");
    
    
    content = QWidget()
    layout = QVBoxLayout(content)
    layout.setContentsMargins(32, 32, 32, 32)
    
    button = Button("Hello from FluentQt", content)
    button.setFluentStyle(Button.ButtonStyle.Accent)
    layout.addWidget(button, 0, Qt.AlignmentFlag.AlignCenter)
    
    w.setContentWidget(content)

    w.resize(800, 600)
    w.show()

    sys.exit(app.exec())
