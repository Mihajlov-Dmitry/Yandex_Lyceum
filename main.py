import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QInputDialog


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('data\\untitled.ui', self)

        self.button_add_1.clicked.connect(lambda: self.add_element(self.listWidget_1))
        self.button_insert_1.clicked.connect(lambda: self.insert_element(self.listWidget_1))
        self.button_remove_1.clicked.connect(lambda: self.remove_element(self.listWidget_1))
        self.button_clear_1.clicked.connect(lambda: self.clear_list(self.listWidget_1))

        self.button_add_2_1.clicked.connect(lambda: self.add_element(self.listWidget_2_1))
        self.button_insert_2_1.clicked.connect(lambda: self.insert_element(self.listWidget_2_1))
        self.button_remove_2_1.clicked.connect(lambda: self.remove_element(self.listWidget_2_1))
        self.button_clear_2_1.clicked.connect(lambda: self.clear_list(self.listWidget_2_1))

        self.button_add_2_2.clicked.connect(lambda: self.add_element(self.listWidget_2_2))
        self.button_insert_2_2.clicked.connect(lambda: self.insert_element(self.listWidget_2_2))
        self.button_remove_2_2.clicked.connect(lambda: self.remove_element(self.listWidget_2_2))
        self.button_clear_2_2.clicked.connect(lambda: self.clear_list(self.listWidget_2_2))

    def add_element(self, list_widget):
        text, ok = QInputDialog.getText(self, 'Добавить записку', 'Введите название или вставьте ссылку')
        if ok and text:
            list_widget.addItem(text)

    def insert_element(self, list_widget):
        text, ok = QInputDialog.getText(self, 'Вставить записку', 'Введите название или вставьте ссылку')
        if ok and text:
            current_row = list_widget.currentRow()
            list_widget.insertItem(current_row + 1, text)

    def remove_element(self, list_widget):
        current_row = list_widget.currentRow()
        if current_row >= 0:
            current_item = list_widget.takeItem(current_row)
            del current_item

    def clear_list(self, list_widget):
        list_widget.clear()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
