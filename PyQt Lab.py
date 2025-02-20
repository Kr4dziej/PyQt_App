from PyQt6.QtWidgets import QApplication, QTabWidget, QWidget, QFileDialog, QVBoxLayout, QGridLayout, QLineEdit
from PyQt6.QtWidgets import QLabel, QSpinBox, QPlainTextEdit, QPushButton, QHBoxLayout
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QStatusBar
from PyQt6.QtWidgets import QToolBar
from PyQt6.QtGui import QIcon, QAction, QPixmap
from PyQt6.QtCore import Qt


# Tworzenie klasy głównego okna aplikacji dziedziczącej po QMainWindow

class Window(QMainWindow):
    # Dodanie konstruktora przyjmującego okno nadrzędne
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('PyQt Lab')
        self.setFixedSize(700, 400)
        self.createMenu()
        self.createTabs()
        self.textFileName = None   # Do saveTask2

    # Funkcja dodająca pasek menu do okna
    def createMenu(self):
        # Stworzenie paska menu
        self.menu = self.menuBar()
        # Dodanie do paska listy rozwijalnej o nazwie File
        self.fileMenu = self.menu.addMenu("File")
        # Dodanie do menu File pozycji zamykającej aplikacje
        self.actionExit = QAction('Exit', self)
        self.actionExit.triggered.connect(self.close)
        self.fileMenu.addAction(self.actionExit)

        # Dodanie do paska podmenu Task 1
        self.task1Menu = self.menu.addMenu("Task 1")
        self.actionOpen = QAction('Open', self)
        self.actionOpen.setShortcut('Ctrl+G')
        self.actionOpen.triggered.connect(self.openTask1)
        self.task1Menu.addAction(self.actionOpen)

        # Dodanie do paska podmenu Task 2
        self.task2Menu = self.menu.addMenu("Task 2")
        self.actionClearT2 = QAction('Clear', self)
        self.actionClearT2.setShortcut('Ctrl+W')
        self.actionClearT2.triggered.connect(self.clearTask2)
        self.task2Menu.addAction(self.actionClearT2)

        self.actionOpenT2 = QAction('Open', self)
        self.actionOpenT2.setShortcut('Ctrl+O')
        self.actionOpenT2.triggered.connect(self.openTask2)
        self.task2Menu.addAction(self.actionOpenT2)

        self.actionSaveT2 = QAction('Save', self)
        self.actionSaveT2.setShortcut('Ctrl+S')
        self.actionSaveT2.triggered.connect(self.saveTask2)
        self.task2Menu.addAction(self.actionSaveT2)

        self.actionSaveAsT2 = QAction('Save as', self)
        self.actionSaveAsT2.setShortcut('Ctrl+K')
        self.actionSaveAsT2.triggered.connect(self.saveAsTask2)
        self.task2Menu.addAction(self.actionSaveAsT2)

        # Dodanie do paska podmenu Task 3
        self.task3Menu = self.menu.addMenu("Task 3")
        self.actionClearT3 = QAction('Clear', self)
        self.actionClearT3.setShortcut('Ctrl+Q')
        self.actionClearT3.triggered.connect(self.clearTask3)
        self.task3Menu.addAction(self.actionClearT3)

    # Funkcje menu
    def openTask1(self):
        fileName, selectedFilter = QFileDialog.getOpenFileName(self, "Wybierz plik obrazu", "",
                                                               "Images (*.png *.jpg *.jpeg *.bmp)")
        if fileName:
            pixmap = QPixmap(fileName)
            pixmap = pixmap.scaled(self.tab_1.width(), self.tab_1.height(), Qt.AspectRatioMode.KeepAspectRatio) # Skalowanie
            self.imageLabel.setPixmap(pixmap)

    def clearTask2(self):
        self.textT2.clear()


    def openTask2(self):
        self.textFileName, _ = QFileDialog.getOpenFileName(self, "Wybierz plik tekstowy", "", "Text files (*.txt)")

        if self.textFileName:
            with open(self.textFileName, 'r+') as fileText:
                noteFile = fileText.read()
            self.textT2.setPlainText(noteFile)

    def saveTask2(self):
        if self.textFileName:
            with open(self.textFileName, 'w') as fileText:
                fileText.write(self.textT2.toPlainText())
        else:
            fileSaveAs, _ = QFileDialog.getSaveFileName(filter="Text files (*.txt)")
            if fileSaveAs:
                with open(fileSaveAs, 'w') as fileText:
                    fileText.write(self.textT2.toPlainText())
                self.textFileName = fileSaveAs

    def saveAsTask2(self):
        fileSaveAs, _ = QFileDialog.getSaveFileName(filter="Text files (*.txt)")
        if fileSaveAs:
            with open(fileSaveAs, 'w') as fileText:
                fileText.write(self.textT2.toPlainText())
            self.textFileName = fileSaveAs


    def clearTask3(self):
        self.text_A.clear()
        self.text_B.clear()
        self.number_C.setValue(0)


        # Funkcja dodająca wenętrzeny widżet do okna
    def createTabs(self):
        # Tworzenie widżetu posiadającego zakładki
        self.tabs = QTabWidget()

        # Stworzenie osobnych widżetów dla zakładek
        self.tab_1 = QWidget()
        # Utworzenie QLabel dla obrazu i dodanie go do zakładki Task 1
        self.imageLabel = QLabel()
        layoutT1 = QVBoxLayout()
        layoutT1.addWidget(self.imageLabel)
        self.tab_1.setLayout(layoutT1)

        self.tab_2 = QWidget()
        self.textT2 = QPlainTextEdit()
        self.buttonSave = QPushButton("Zapisz")
        self.buttonSave.clicked.connect(self.saveTask2)
        self.buttonClear = QPushButton("Wyczyść")
        self.buttonClear.clicked.connect(self.clearTask2)
        layoutT2 = QGridLayout()
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.buttonSave)
        buttonLayout.addWidget(self.buttonClear)
        layoutT2.addWidget(self.textT2, 0, 0)
        layoutT2.addLayout(buttonLayout, 1, 0)
        self.tab_2.setLayout(layoutT2)


        self.tab_3 = QWidget()
        label_A = QLabel("Pole A")
        self.text_A = QLineEdit()
        label_B = QLabel("Pole B")
        self.text_B = QLineEdit()
        label_C = QLabel("Pole C")
        self.number_C = QSpinBox()
        self.number_C.setMinimum(0)
        self.number_C.setMaximum(100000)
        labelSUM = QLabel("Pole A+B+C")
        layoutT3 = QGridLayout()
        self.sum = QLineEdit()
        self.sum.setReadOnly(True)
        self.update_sum()
        layoutT3.setAlignment(Qt.AlignmentFlag.AlignTop)
        layoutT3.addWidget(label_A, 0, 0)
        layoutT3.addWidget(self.text_A, 0, 1)
        layoutT3.addWidget(label_B, 1, 0)
        layoutT3.addWidget(self.text_B, 1, 1)
        layoutT3.addWidget(label_C, 2, 0)
        layoutT3.addWidget(self.number_C, 2, 1)
        layoutT3.addWidget(labelSUM, 3, 0)
        layoutT3.addWidget(self.sum, 3, 1)
        self.tab_3.setLayout(layoutT3)
        self.text_A.textChanged.connect(self.update_sum)
        self.text_B.textChanged.connect(self.update_sum)
        self.number_C.valueChanged.connect(self.update_sum)

        # Dodanie zakładek do widżetu obsługującego zakładki
        self.tabs.addTab(self.tab_1, "Task 1")
        self.tabs.addTab(self.tab_2, "Task 2")
        self.tabs.addTab(self.tab_3, "Task 3")

        # Dodanie widżetu do głównego okna jako centralny widżet
        self.setCentralWidget(self.tabs)

    def update_sum(self):
        self.sum.setText(self.text_A.text() + self.text_B.text() + str(self.number_C.value()))


# Uruchomienie okna
app = QApplication([])
win = Window()
win.show()
app.exec()

