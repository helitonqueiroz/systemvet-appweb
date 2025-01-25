from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
import sys

class MainWindow(QMainWindow):
    def __init__(self, url):
        super().__init__()
        
        # Cria um widget central e layout
        central_widget = QWidget()
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Configura o navegador
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(url))
        layout.addWidget(self.browser)  # Adiciona o navegador ao layout
        
        # Define o widget central e o layout na janela principal
        self.setCentralWidget(central_widget)
        self.setWindowIcon(QIcon('icon.webp'))
        # Exibe a janela com barra de título e maximizada
        self.show()
        self.showMaximized()  # Maximiza a janela após ser exibida
        self.setWindowTitle("Sistema Veterinário")  # Define o título da janela

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MainWindow("http://127.0.0.1:8000/")
    sys.exit(app.exec_())
