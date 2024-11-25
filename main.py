import sys
import sqlite_function
from PyQt6 import uic
from PyQt6.QtCore import Qt, QEvent
from PyQt6.QtWidgets import QApplication, QMainWindow, QInputDialog, QListWidget, QMenu


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('data\\untitled.ui', self)

        self.listWidget_1.addItems([i[0] for i in sqlite_function.select(1)])
        self.button_add_1.clicked.connect(lambda: self.add_element(self.listWidget_1))
        self.button_insert_1.clicked.connect(lambda: self.insert_element(self.listWidget_1))
        self.button_remove_1.clicked.connect(lambda: self.remove_element(self.listWidget_1))
        self.button_clear_1.clicked.connect(lambda: self.clear_list(self.listWidget_1))

        self.listWidget_2_1.addItems([i[0] for i in sqlite_function.select(21)])
        self.button_add_2_1.clicked.connect(lambda: self.add_element(self.listWidget_2_1))
        self.button_insert_2_1.clicked.connect(lambda: self.insert_element(self.listWidget_2_1))
        self.button_remove_2_1.clicked.connect(lambda: self.remove_element(self.listWidget_2_1))
        self.button_clear_2_1.clicked.connect(lambda: self.clear_list(self.listWidget_2_1))

        self.listWidget_2_2.addItems([i[0] for i in sqlite_function.select(22)])
        self.button_add_2_2.clicked.connect(lambda: self.add_element(self.listWidget_2_2))
        self.button_insert_2_2.clicked.connect(lambda: self.insert_element(self.listWidget_2_2))
        self.button_remove_2_2.clicked.connect(lambda: self.remove_element(self.listWidget_2_2))
        self.button_clear_2_2.clicked.connect(lambda: self.clear_list(self.listWidget_2_2))

        self.listWidget_3.addItems([i[0] for i in sqlite_function.select(3)])
        self.button_add_3.clicked.connect(lambda: self.add_element(self.listWidget_3))
        self.button_insert_3.clicked.connect(lambda: self.insert_element(self.listWidget_3))
        self.button_remove_3.clicked.connect(lambda: self.remove_element(self.listWidget_3))
        self.button_clear_3.clicked.connect(lambda: self.clear_list(self.listWidget_3))

        self.listWidget_4.addItems([i[0] for i in sqlite_function.select(4)])
        self.button_add_4.clicked.connect(self.find_date)
        self.button_remove_4.clicked.connect(lambda: self.remove_element(self.listWidget_4))
        self.button_clear_4.clicked.connect(lambda: self.clear_list(self.listWidget_4))

        self.listWidget_5.addItems([i[0] for i in sqlite_function.select(5)])
        self.button_add_5.clicked.connect(lambda: self.add_element(self.listWidget_5))
        self.button_insert_5.clicked.connect(lambda: self.insert_element(self.listWidget_5))
        self.button_remove_5.clicked.connect(lambda: self.remove_element(self.listWidget_5))
        self.button_clear_5.clicked.connect(lambda: self.clear_list(self.listWidget_5))

        self.listWidget_6_1.addItems([i[0] for i in sqlite_function.select(61)])
        self.button_add_6_1.clicked.connect(lambda: self.add_element(self.listWidget_6_1))
        self.button_insert_6_1.clicked.connect(lambda: self.insert_element(self.listWidget_6_1))
        self.button_remove_6_1.clicked.connect(lambda: self.remove_element(self.listWidget_6_1))
        self.button_clear_6_1.clicked.connect(lambda: self.clear_list(self.listWidget_6_1))

        self.listWidget_6_2.addItems([i[0] for i in sqlite_function.select(62)])
        self.button_add_6_2.clicked.connect(lambda: self.add_element(self.listWidget_6_2))
        self.button_insert_6_2.clicked.connect(lambda: self.insert_element(self.listWidget_6_2))
        self.button_remove_6_2.clicked.connect(lambda: self.remove_element(self.listWidget_6_2))
        self.button_clear_6_2.clicked.connect(lambda: self.clear_list(self.listWidget_6_2))

        self.listWidget_7_1.addItems([i[0] for i in sqlite_function.select(71)])
        self.button_add_7_1.clicked.connect(lambda: self.add_element(self.listWidget_7_1))
        self.button_remove_7_1.clicked.connect(lambda: self.remove_element(self.listWidget_7_1))
        self.button_clear_7_1.clicked.connect(lambda: self.clear_list(self.listWidget_7_1))

        self.listWidget_7_2.addItems([i[0] for i in sqlite_function.select(72)])
        self.button_add_7_2.clicked.connect(lambda: self.add_element(self.listWidget_7_2))
        self.button_remove_7_2.clicked.connect(lambda: self.remove_element(self.listWidget_7_2))
        self.button_clear_7_2.clicked.connect(lambda: self.clear_list(self.listWidget_7_2))

        self.listWidget_7_3.addItems([i[0] for i in sqlite_function.select(73)])
        self.button_add_7_3.clicked.connect(lambda: self.add_element(self.listWidget_7_3))
        self.button_remove_7_3.clicked.connect(lambda: self.remove_element(self.listWidget_7_3))
        self.button_clear_7_3.clicked.connect(lambda: self.clear_list(self.listWidget_7_3))

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

    def find_date(self):
        string_date = self.calendarWidget.selectedDate().toPyDate()
        time_date = self.timeEdit.time().toPyTime()

        self.listWidget_4.addItem(f"{string_date}-{time_date} - {self.textEdit_4.toPlainText()}")

    def closeEvent(self, event):
        sqlite_function.delete(1)
        for element in [self.listWidget_1.item(x).text() for x in range(self.listWidget_1.count())]:
            sqlite_function.insert(element, 1)

        sqlite_function.delete(21)
        for element in [self.listWidget_2_1.item(x).text() for x in range(self.listWidget_2_1.count())]:
            sqlite_function.insert(element, 21)

        sqlite_function.delete(22)
        for element in [self.listWidget_2_2.item(x).text() for x in range(self.listWidget_2_2.count())]:
            sqlite_function.insert(element, 22)

        sqlite_function.delete(3)
        for element in [self.listWidget_3.item(x).text() for x in range(self.listWidget_3.count())]:
            sqlite_function.insert(element, 3)

        sqlite_function.delete(4)
        for element in [self.listWidget_4.item(x).text() for x in range(self.listWidget_4.count())]:
            sqlite_function.insert(element, 4)

        sqlite_function.delete(5)
        for element in [self.listWidget_5.item(x).text() for x in range(self.listWidget_5.count())]:
            sqlite_function.insert(element, 5)

        sqlite_function.delete(61)
        for element in [self.listWidget_6_1.item(x).text() for x in range(self.listWidget_6_1.count())]:
            sqlite_function.insert(element, 61)

        sqlite_function.delete(62)
        for element in [self.listWidget_6_2.item(x).text() for x in range(self.listWidget_6_2.count())]:
            sqlite_function.insert(element, 62)

        sqlite_function.delete(71)
        for element in [self.listWidget_7_1.item(x).text() for x in range(self.listWidget_7_1.count())]:
            sqlite_function.insert(element, 71)

        sqlite_function.delete(72)
        for element in [self.listWidget_7_2.item(x).text() for x in range(self.listWidget_7_2.count())]:
            sqlite_function.insert(element, 72)

        sqlite_function.delete(73)
        for element in [self.listWidget_7_3.item(x).text() for x in range(self.listWidget_7_3.count())]:
            sqlite_function.insert(element, 73)

        event.accept()

    def contextMenuEvent(self, event):
        context_menu = QMenu(self)
        action1 = context_menu.addAction("Корзина")
        action2 = context_menu.addAction("Текущие действия")
        action3 = context_menu.addAction("Ожидание")
        action4 = context_menu.addAction("Календарь")
        action5 = context_menu.addAction("Проекты")
        action6 = context_menu.addAction("Когда-нибудь потом")
        action7 = context_menu.addAction("Заметки")
        action8 = context_menu.addAction("Выполнено")

        action = context_menu.exec(self.mapToGlobal(event.pos()))

        if action == action1:
            print("Action 1 selected")
        elif action == action2:
            print("Action 2 selected")
        elif action == action4:
            print("Action 3 selected")
        elif action == action5:
            print("Action 3 selected")
        elif action == action6:
            print("Action 2 selected")
        elif action == action7:
            print("Action 3 selected")
        elif action == action8:
            print("Action 3 selected")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
