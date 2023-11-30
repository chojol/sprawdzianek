import sys
from PyQt6.QtWidgets import QDialog, QApplication
from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.order.clicked.connect(self.zamow)
        self.show()

    def zamow(self):
        price = 0
        if self.ui.hawajska.isChecked():
            price = 30
            pizza = "hawajska"
        elif self.ui.margherita.isChecked():
            price = 28
            pizza = "margherita"
        elif self.ui.capricciosa.isChecked():
            price = 32
            pizza = "capricciosa"
        elif self.ui.quattro.isChecked():
            price = 34
            pizza = "quattro"
        if self.ui.checkCheese.isChecked():
            price += 5

        email = self.ui.emailValue.text()

        if "@" in email :
            self.ui.ordered.setText(f'uzytkownik {email}'
                                    f' zamowil pizze {pizza}. '
                                    f'cena: {price}zł. ')
        else:
            self.ui.ordered.setText(f'niepoprawny email')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(app.exec())