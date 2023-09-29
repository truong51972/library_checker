from PyQt5 import QtCore, QtGui, QtWidgets
from UI.addBook_UI import Ui_addBook
from package.sqlQuery import sqlQuery
from UI.showMassage import showMessage

class func_addBook(Ui_addBook):
    def __init__(self) -> None:
        super().__init__()
        self.sqlQuery = sqlQuery('./package/data.db')

    def setupAction(self):
        self.b_add.clicked.connect(self.addBook)

    def addBook(self):
        try:
            bookId = self.bookId.text().strip()
            ageAllow = self.ageAllow.text().strip()
            bookTitle = self.bookTitle.text().strip()
            bookAuthor = self.bookAuthor.text().strip()
            amount = self.amount.text().strip()

            if bookId == '':
                showMessage('Thông báo', "ID sách trống!")
            elif ageAllow == '':
                showMessage('Thông báo', "Tuổi cho phép trống!")
            elif bookTitle == '':
                showMessage('Thông báo', "Tiêu đề sách trống!")
            elif bookAuthor == '':
                showMessage('Thông báo', "Tác giả sách trống!")
            elif amount == '':
                showMessage('Thông báo', "Số lượng sách trống!")
            else:
                if (self.sqlQuery.addNewBook(bookId, bookTitle, bookAuthor, ageAllow, amount)):
                    showMessage('Thông báo', "Thêm sách thành công!")
                    self.bookId.setText('')
                    self.ageAllow.setText('')
                    self.bookTitle.setText('')
                    self.bookAuthor.setText('')
                    self.amount.setText('')
                else:
                    showMessage('Thông báo', "ID đã tồn tại!")
        except:
            showMessage('Thông báo', "Vui lòng kiểm tra lại thông tin!")