import os
import sys

os.environ["QT_SCALE_FACTOR"] = "1.2"  # Или фиксированный коэффициент (150%)

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QLineEdit, QCheckBox, QSpinBox)

from utils import generate_multiple_passwords


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Generator (by 0xK3rn3l)")
        self.setGeometry(350, 60, 400, 500)

        with open("styles.qss", "r") as f:
            self.setStyleSheet(f.read())

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)
        
        label1 = QLabel("> PASSWORD_GENERATOR.exe <")
        label1.setObjectName("title")
        label1.setAlignment(Qt.AlignCenter)
        

        length_layout = QHBoxLayout()
        length_label = QLabel("Password length:")
        length_label.setObjectName("length_label")
        
        self.length_spinbox = QSpinBox()
        self.length_spinbox.setObjectName("length_spinbox")
        self.length_spinbox.setRange(8, 64)      # Мин 8, макс 64
        self.length_spinbox.setValue(12)          # По умолчанию 12
        self.length_spinbox.setSuffix("")
        self.length_spinbox.setFixedWidth(120)

        length_layout.addWidget(length_label)
        length_layout.addWidget(self.length_spinbox)
        length_layout.addStretch()

        btn_click = QPushButton("Generate Password")
        btn_click.setObjectName("generate_btn")
        btn_click.setFixedSize(180, 45)
        btn_click.clicked.connect(self.generate_password)

        self.password_output = QLineEdit()
        self.password_output.setObjectName("password_output")
        self.password_output.setReadOnly(True)
        self.password_output.setPlaceholderText("Generated password...")
        self.password_output.setAlignment(Qt.AlignCenter)


        options_label = QLabel("Character types:")
        options_label.setObjectName("options_label")
        
        self.uppercase_check = QCheckBox("Uppercase (A-Z)")
        self.uppercase_check.setChecked(True)
        
        self.lowercase_check = QCheckBox("Lowercase (a-z)")
        self.lowercase_check.setChecked(True)
        
        self.digits_check = QCheckBox("Digits (0-9)")
        self.digits_check.setChecked(True)
        
        self.special_check = QCheckBox("Special (!@#$%^&*_?)")
        self.special_check.setChecked(True)



        main_layout.addWidget(label1, alignment=Qt.AlignTop)
        main_layout.addLayout(length_layout)
        main_layout.addWidget(options_label)
        main_layout.addWidget(self.uppercase_check)
        main_layout.addWidget(self.lowercase_check)
        main_layout.addWidget(self.digits_check)
        main_layout.addWidget(self.special_check)
        main_layout.addWidget(self.password_output)
        main_layout.addWidget(btn_click, alignment=Qt.AlignCenter)



    def generate_password(self):
        """Генерация пароля в GUI"""
        length = self.length_spinbox.value()
        use_upper = self.uppercase_check.isChecked()
        use_lower = self.lowercase_check.isChecked()
        use_digits = self.digits_check.isChecked()
        use_special = self.special_check.isChecked()
        
        password = generate_multiple_passwords(
            1, 
            length=length,
            use_uppercase=use_upper,
            use_lowercase=use_lower,
            use_digits=use_digits,
            use_special=use_special
        )[0]
        
        if password:
            self.password_output.setText(password)
        else:
            self.password_output.setText("Select at least one character type!")
    

def GUI_mode():
    app = QApplication(sys.argv)  # Сначала создаём QApplication
    window = MainWindow()         # Потом создаём окно
    window.show()                 # Показываем окно
    sys.exit(app.exec_())         # Запускаем цикл событий

