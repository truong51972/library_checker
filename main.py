from UI.main_UI import Ui_MainWindow
from UI.addUser_func import func_addUser
from UI.addBook_func import func_addBook
from UI.showMassage import showMessage
from package.sqlQuery import sqlQuery
from package.linkedList import LinkedList
from package.ArrayStack import ArrayStack
from setting.readScale import readScaleFile
from PyQt5 import QtWidgets
import sys
import os

class test(Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.sqlQuery = sqlQuery('./package/data.db')
    def setupAction(self):
        self.b_findUser.clicked.connect(self.findUser)
        self.b_findBook.clicked.connect(self.findBook)
        self.newUser.triggered.connect(self.addUser)
        self.newBook.triggered.connect(self.addBook)
        self.b_borrow.clicked.connect(self.borrowBook)
        self.b_return.clicked.connect(self.returnBook)
        self.deleteUser.triggered.connect(self.deleteUser_func)
        self.deleteBook.triggered.connect(self.deleteBook_fuc)
        self.show100.triggered.connect(self.changeShow100)
        self.show200.triggered.connect(self.changeShow200)

    def changeShow200(self):
        f = open('./setting/scale.size', 'w')
        int(f.write('2'))
        f.close()
        showMessage('Thông báo', "Khởi động lại ứng dụng để áp dụng cài đặt!")
        sys.exit()

    def changeShow100(self):
        f = open('./setting/scale.size', 'w')
        int(f.write('1'))
        f.close()
        showMessage('Thông báo', "Khởi động lại ứng dụng để áp dụng cài đặt!")
        sys.exit()

    def addUser(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = func_addUser()
        self.ui.setupUi(self.window, readScaleFile())
        self.ui.setupAction()
        self.window.show()

    def addBook(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = func_addBook()
        self.ui.setupUi(self.window, readScaleFile())
        self.ui.setupAction()
        self.window.show()

    def findUser(self):
        try:
            idUser = self.i_user.text().strip()
            if (idUser == ''):
                showMessage('Thông báo', "Vui lòng nhập ID khách!")
            else:
                data = self.sqlQuery.showUser(idUser)
                if (data == None):
                    showMessage('Thông báo', "ID người dùng không tồn tại!")
                    self.o_userInfo.setText('')
                    self.o_bookBorrowed.setText('')
                    self.i_user.setText('')
                else:
                    idUser, name, sex, birth = data
                    age = int(self.sqlQuery.getAge(idUser))
                    output = f'ID: {idUser}\nHọ và Tên: {name}\nGiới tính: {sex}   Tuổi: {age}\nNgày sinh: {birth.split("-")[2]}/{birth.split("-")[1]}/{birth.split("-")[0]}'
                    self.o_userInfo.setText(output)

                    books = self.sqlQuery.showBookBorrow(idUser)
                    if (len(books) == 0):
                        self.o_bookBorrowed.setText('Không có!')
                    else:
                        listBook = LinkedList()
                        printOut = ''
                        books.sort(reverse=True)
                        for values in books:
                            # print(values)
                            bookInfo = ArrayStack()
                            for value in values:
                                bookInfo.push(value)
                            listBook.push(bookInfo)

                        while True:
                            info = listBook.pop()
                            if info == None: break
                            day = info.pop()
                            dayBorrow = info.pop()
                            bookId, title, author = self.sqlQuery.showBook(info.pop())[0:3]
                            text = f'Id: {bookId}\nTiêu đề: {title}\nTác giả: {author}\nNgày mượn: {day.split("-")[2]}/{day.split("-")[1]}/{day.split("-")[0]}\n\n'
                            
                            printOut += text
                        self.o_bookBorrowed.setText(printOut)
        except:
            showMessage('Thông báo', "Vui lòng kiểm tra lại thông tin!")

    def deleteUser_func(self):
        try:
            idUser = self.i_user.text().strip()
            if (idUser == ''):
                showMessage('Thông báo', "Vui lòng nhập ID!")
            else:
                data = self.sqlQuery.showUser(idUser)
                if (data == None):
                    showMessage('Thông báo', "ID người dùng không tồn tại!")
                else:
                    if(self.sqlQuery.deleteUser(idUser)):
                        showMessage('Thông báo', "Đã xoá khách hàng!")
                        self.o_userInfo.setText('')
                        self.o_bookBorrowed.setText('')
                        self.i_user.setText('')
                    else:
                        showMessage('Thông báo', "Xoá không thành công!")
        except:
            showMessage('Thông báo', "Vui lòng kiểm tra lại thông tin!")
    
    def findBook(self):
        try:
            idBook = self.i_bookId.text().strip()
            if (idBook == ''):
                showMessage('Thông báo', "Vui lòng nhập ID sách!")
            else:
                data = self.sqlQuery.showBook(idBook)
                if (data == None):
                    showMessage('Thông báo', "ID sách không tồn tại!")
                    self.o_bookInfo.setText('')
                else:
                    bookId, bookTitle, bookAuthor, ageAllow, amount = data
                    output = f'ID: {bookId}\nTiêu đề: {bookTitle}\nTác giả: {bookAuthor}\nTuổi cho phép: {ageAllow}\nSố Lượng: {amount}'
                    self.o_bookInfo.setText(output)
        except:
            showMessage('Thông báo', "Vui lòng kiểm tra lại thông tin!")

    def borrowBook(self):
        try:
            idBook = self.i_bookId.text().strip()
            idUser = self.i_user.text().strip()
            if (idUser == ''):
                showMessage('Thông báo', "Vui lòng nhập ID khách!")
            elif (idBook == ''):
                showMessage('Thông báo', "Vui lòng nhập ID sách!")

            else:
                if not self.sqlQuery.checkUserBorrow(idUser, idBook):
                    if (self.sqlQuery.borrowBook(idUser, idBook, 30)):
                        showMessage('Thông báo', "Mượn sách thành công!")
                        self.findUser()
                        self.findBook()
                    else:
                        showMessage('Thông báo', "Mượn sách không thành công!")
                else:
                    showMessage('Thông báo', "Mượn sách không thành công!")
        except:
            showMessage('Thông báo', "Vui lòng kiểm tra lại thông tin!")

    def returnBook(self):
        try:
            idBook = self.i_bookId.text().strip()
            idUser = self.i_user.text().strip()
            if (idUser == ''):
                showMessage('Thông báo', "Vui lòng nhập ID khách!")
            elif (idBook == ''):
                showMessage('Thông báo', "Vui lòng nhập ID sách!")

            else:
                if self.sqlQuery.checkUserBorrow(idUser, idBook):
                    if (self.sqlQuery.returnBook(idUser, idBook)):
                        showMessage('Thông báo', "Trả sách thành công!")
                        self.findUser()
                        self.findBook()
                    else:
                        showMessage('Thông báo', "Trả sách không thành công!")
                else:
                    showMessage('Thông báo', "Trả sách không thành công!")
        except:

            showMessage('Thông báo', "Vui lòng kiểm tra lại thông tin!")
    def deleteBook_fuc(self):
        try:
            idBook = self.i_bookId.text().strip()
            if (idBook == ''):
                showMessage('Thông báo', "Vui lòng nhập ID sách!")

            else:
                if self.sqlQuery.deleteBook(idBook):
                    showMessage('Thông báo', "Xoá sách thành công!")
                    self.o_bookInfo.setText('')
                else:
                    showMessage('Thông báo', "Xoá sách không thành công!")

        except:
            showMessage('Thông báo', "Vui lòng kiểm tra lại thông tin!")
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = test()
    ui.setupUi(MainWindow, readScaleFile())
    ui.setupAction()
    MainWindow.show()
    sys.exit(app.exec_())
