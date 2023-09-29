import sqlite3
import os

class sqlQuery():
    def __init__(self, name) -> None:
        self.name = name
        
        self.con = sqlite3.connect(name)
        self.cur = self.con.cursor()

    def initTable(self):

        self.cur.execute(
            """
            create table user
                (
                    userId int not null primary key,
                    userName nvarchar(50) not null,
                    userSex char(5),
                    userBirth date
                )
            """
        )

        self.cur.execute(
            """
            create table borrow
                (
                    userId int not null,
                    bookId int not null,
                    numberOfDay int,
                    dayBorrow date,

                    --constraint pk_userBorrow primary key (userId, bookId),
                    constraint fk_bookId foreign key (bookId) references book (bookId),
                    constraint fk_userId foreign key (userId) references user (userId)
                )
            """
        )
        
        self.cur.execute(
            """
                create table book
                (
                    bookId int not null primary key,
                    bookName nvarchar(50) not null,
                    bookAuthor nvarchar(50),
                    ageAllow int,
                    amount int
                )
            """
        )

    def addNewUser(self, userId, userName, userSex, userBirth):
        data = self.cur.execute(
            f"""
            select userId
            from user
            where userId = {userId}
            """
        )
        if (data.fetchone() == None):
            self.cur.execute(
                f"""
                insert into user
                values ({userId}, '{userName}', '{userSex}', '{userBirth}')
                """
            )
            self.con.commit()
            print('Successful!')
            return True
        else:
            print('Failure!')
            return False

    def addNewBook(self, bookId: int, bookName: str, author: str, ageAllow: int, amount: int):
        data = self.cur.execute(
            f"""
            select bookId
            from book
            where bookId = {bookId}
            """
        )
        if (data.fetchone() == None):
            self.cur.execute(
                f"""
                insert into book
                values ({bookId}, '{bookName}', '{author}', {ageAllow}, {amount})
                """
            )
            self.con.commit()
            print('Successful!')
            return True
        else:
            print('Failure!')
            return False

    def bookCheck(self, bookId):
        data = self.cur.execute(
            f"""
            select amount, ageAllow
            from book
            where bookId = {bookId}
            """
        )
        if ((result:= data.fetchone()) != None):
            return result
        else:
            return None, None
    def showUser(self, userId):
        data = self.cur.execute(
            f"""
            select *
            from user
            where userId = {userId}
            """
        )
        if ((info:= data.fetchone()) != None):
            return info
        else:
            return None
        
    def showBook(self, bookId):
        data = self.cur.execute(
            f"""
            select *
            from book
            where bookId = {bookId}
            """
        )
        if ((info:= data.fetchone()) != None):
            return info
        else:
            return None
        
    def getAge(self, userId):
        data = self.cur.execute(
            f"""
            select (julianday(date('now')) - julianday(userBirth)) /365 
            from user
            where userId = {userId}
            """
        )
        if ((age:= data.fetchone()) != None):
            return age[0]
        else:
            return None
        
    def borrowBook(self, userId: int, bookId: int, dayBorrow: int):
        amount, ageAllow = self.bookCheck(bookId)
        if (amount == None):
            print('Book is not existed!')
            return False
        if (amount == 0):
            print('Out of book!')
            return False
        if (ageAllow > self.getAge(userId)):
            print('Age of user is not allowed!')
            return False
        
        self.cur.execute(
            f"""
            insert into borrow
            values ({userId}, {bookId}, {dayBorrow}, date('now'))
            """
        )
        self.con.commit()

        self.cur.execute(
            f"""
            update book
            set amount = {amount - 1}
            where bookId = {bookId}
            """
        )
        self.con.commit()

        print('Successful!')
        return True

    def deleteBook(self, bookId: int):

        self.cur.execute(
            f"""
            update book
            set amount = 0
            where bookId = {bookId}
            """
        )
        self.con.commit()

        print('Successful!')
        return True

    def returnBook(self, userId: int, bookId: int):  
        amount, ageAllow = self.bookCheck(bookId)   
        data = self.cur.execute(
            f"""
            select *
            from borrow
            where userId = {userId} and bookId = {bookId}
            """
        )
        if (data.fetchone() != None):
            self.cur.execute(
                f"""
                delete
                from borrow
                where userId = {userId} and bookId = {bookId}
                """
            )
            self.con.commit()

            self.cur.execute(
                f"""
                update book
                set amount = {amount + 1}
                where bookId = {bookId}
                """
            )
            self.con.commit()
            print('Successful!')
            return True
        else:
            print('Failure!')
            return False
        
    def showBookBorrow(self, userId):
        if (self.showUser(userId) == None): 
            print('User Id is not exist!')
            return False
        
        data = self.cur.execute(
                f"""
                select *
                from borrow
                where userId = {userId}
                """
            )
        return data.fetchall()

    def checkUserBorrow(self, userId, bookId):
        if (self.showUser(userId) == None): 
            print('User Id is not exist!')
            return False
        
        data = self.cur.execute(
                f"""
                select bookId
                from borrow
                where userId = {userId} and bookId = {bookId}
                """
            )
        return data.fetchone() != None
    
    def deleteUser(self, userId):
        if (self.showUser(userId) == None): 
            print('User Id is not exist!')
            return False
        if (self.showBookBorrow(userId) != None):
            print('User was borrowing book!')
            return False
        
        self.cur.execute(
                f"""
                delete
                from user
                where userId = {userId}
                """
            )
        self.con.commit()
        print('Successful!')
        return True

    def deleteBook(self, bookId):
        if (self.bookCheck(bookId) == None):
            print('Book Id is not exist!')
            return False
        self.cur.execute(
                f"""
                delete
                from book
                where bookId = {bookId}
                """
            )
        self.con.commit()
        print('Successful!')
        return True
def initializeData():
    os.system(f'rm ./package/data.db')
    os.system(f'type nul > ./package/data.db')
    
    table = sqlQuery('./package/data.db')
    table.initTable()

    table.addNewUser(1,'Nguyễn Văn A','Nam','2003-09-14')
    table.addNewUser(2,'Nguyễn Văn B','Nam','2004-09-14')
    table.addNewUser(3,'Nguyễn Văn C','Nam','2005-09-14')
    table.addNewUser(4,'Nguyễn Văn D','Nam','2006-09-14')
    table.addNewUser(5,'Nguyễn Văn E','Nam','2007-09-14')

    table.addNewBook(1, 'Sách A', 'Tác giả A', 18, 100)
    table.addNewBook(2, 'Sách B', 'Tác giả B', 17, 100)
    table.addNewBook(3, 'Sách C', 'Tác giả C', 16, 100)
    table.addNewBook(4, 'Sách D', 'Tác giả D', 15, 100)
    table.addNewBook(5, 'Sách E', 'Tác giả E', 14, 100)
