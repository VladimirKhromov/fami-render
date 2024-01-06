from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow

import sys

def application():
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle("FamiRender")
    window.setGeometry(300, 250, 500, 500)

    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    application()

