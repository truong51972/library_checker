from PyQt5 import QtWidgets

def showMessage(title: str, message: str):
    message_box = QtWidgets.QMessageBox()
    message_box.setText(message)
    message_box.setWindowTitle(title)
    message_box.setIcon(QtWidgets.QMessageBox.Information)
    message_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
    message_box.exec_()