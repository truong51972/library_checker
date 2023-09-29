from PyQt5 import QtCore, QtGui, QtWidgets
from UI.addUser_UI import Ui_addUser
from package.sqlQuery import sqlQuery
from UI.showMassage import showMessage

class func_addUser(Ui_addUser):
    def __init__(self) -> None:
        super().__init__()
        self.sqlQuery = sqlQuery('./package/data.db')

    def setupAction(self):
        self.b_add.clicked.connect(self.addUser)

    def addUser(self):
        userId = self.userId.text()
        userName = self.userName.text()
        birth_year = self.birth_year.text()

        userSex = self.userSex.currentText()
        birth_day = str(self.birth_day.currentIndex() + 1).rjust(2,'0')
        birth_month = str(self.birth_month.currentIndex() + 1).rjust(2,'0')

        if userId == '':
            showMessage('Thông báo', 'ID trống!')
        elif userName == '':
            showMessage('Thông báo', 'Họ và tên trống!')
        elif birth_year == '':
            showMessage('Thông báo', 'Năm sinh trống!')
        else:
            birth_year = birth_year.rjust(4,'0')
            if (self.sqlQuery.addNewUser(userId,userName,userSex, f'{birth_year}-{birth_month}-{birth_day}')):
                print(userId,userName,userSex, f'{birth_year}-{birth_month}-{birth_day}')

                self.userId.setText('')
                self.userName.setText('')
                self.birth_year.setText('')

                self.userSex.setCurrentIndex(0)
                self.birth_day.setCurrentIndex(0)
                self.birth_month.setCurrentIndex(0)
                showMessage('Thông báo', 'Thêm thành công!')
            else:
                showMessage('Thông báo', 'Vui lòng kiểm tra lại thông tin khách hàng!')
                
# if __name__ == "__main__":

    # a = func_AddUser()
    # a.show()