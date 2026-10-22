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