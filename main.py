import os, sys
from ui.mainUi import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtGui import QPixmap

# def trans_any_audio_types(filepath, input_audio_type, output_audio_type):
#     song = AudioSegment.from_file(filepath, input_audio_type)
#     filename = filepath.split(".")[0]
#     if os.getcwd() != "/static/":
#         print(os.getcwd())
#         os.chdir('./static/')
#     song.export(f"{filename}.{output_audio_type}", format=f"{output_audio_type}")

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.PixmapLabel.setPixmap(QPixmap("bg.jpg").scaledToHeight(self.ui.PixmapLabel.width()))
        # self.ui.SmoothScrollArea.setWidget(self.ui.PixmapLabel)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())