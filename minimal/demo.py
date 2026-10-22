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
    # app.setFont(fluentqt.font_for_role(fluentqt.FontRole.Body))

    w = Window()
    w.setWindowTitle("FluentQt Hello world!");
    
    
    content = QWidget()
    layout = QHBoxLayout(content)
    layout.setContentsMargins(32, 32, 32, 32)
    
    # button = Button("Hello from FluentQt", content)
    # button.setFluentStyle(Button.ButtonStyle.Accent)
    
    standard = Button("Standard", content)
    standard.setFixedWidth(120)
    standard.setFluentStyle(Button.ButtonStyle.Standard)
    
    accent = Button("Accent", content)
    accent.setFixedWidth(120)
    accent.setFluentStyle(Button.ButtonStyle.Accent)
    
    subtle = Button("Subtle", content)
    subtle.setFixedWidth(120)
    subtle.setFluentStyle(Button.ButtonStyle.Subtle)
    
    layout.addWidget(standard)
    layout.addWidget(accent)
    layout.addWidget(subtle)
    
    w.setContentWidget(content)

    w.resize(800, 600)
    w.show()

    sys.exit(app.exec())
