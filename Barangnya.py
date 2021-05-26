import mysql.connector
from PyQt5.QtWidgets import QMessageBox

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database ="document_management_system"
)
mycursor = mydb.cursor()

def show_Popup(message):
    msg = QMessageBox()
    msg.setWindowTitle("Message")
    msg.setText(message)
    x = msg.exec_()

class Document():
    def __init__(self,Category_ID,Topic_ID,Tag,Filename):
        self.CatID = Category_ID
        self.TopID = Topic_ID
        self.NFile = Filename
        self.Tag = Tag

    def masukin(self):
        order = f"""INSERT INTO document
        (document_id, category_id, topic_id, Tag, file_name) VALUES
        (NULL, '{self.CatID}', '{self.TopID}', '{self.Tag}', '{self.NFile}')"""
        mycursor.execute(order)
        mydb.commit()
        show_Popup("Berhasil Menginput Data")


    def hapus(Doc_ID):
        order = f"DELETE FROM document WHERE document.document_id = {Doc_ID}"
        try:
            mycursor.execute(order)
            mydb.commit()
            hasil = "Berhasil Mengapus Data"
        except mysql.connector.Error as error:
            hasil = f"Gagal menghapus data, error code: {error}"
        show_Popup(hasil)


    def update(self,ID_O):
        order = f"""UPDATE document SET
        category_id = '{self.CatID}',
        topic_id = '{self.TopID}',
        Tag = '{self.Tag}',
        file_name = '{self.NFile}'
        WHERE document.document_id = '{ID_O}'"""
        try:
            mycursor.execute(order)
            mydb.commit()
            hasil = "Berhasil Memperbarui Data"
        except mysql.connector.Error as error:
            hasil = f"Gagal Memperbarui data, error code: {error}"
        show_Popup(hasil)

    def getList():
        order = "Select * from document"
        mycursor.execute(order)
        result = mycursor.fetchall()
        hasil =[]
        for i in result:
            a = str(i[0]) + " - " + str(i[3])
            hasil.append(a)
        return hasil

class Topic():
    def __init__(self,Topic,Dir):
        self.Topic = Topic
        self.Direc = Dir

    def masukin(self):
        order = f"""INSERT INTO topic
        (topic_id, topic, storage_file) VALUES
        (NULL, '{self.Topic}', '{self.Direc}')"""
        mycursor.execute(order)
        mydb.commit()
        show_Popup("Berhasil Menginput Data")

    def hapus(ID):
        order = f"DELETE FROM topic WHERE topic.topic_id = {ID}"
        try:
            mycursor.execute(order)
            mydb.commit()
            hasil = "Berhasil Mengapus Data"
        except mysql.connector.Error as error:
            hasil = f"Gagal menghapus data, error code: {error}"
        return hasil

    def update(self,ID_O):
        order = f"""UPDATE topic SET
        topic = '{self.Topic}',
        storage_file = '{self.Direc}'
        WHERE topic.topic_id = '{ID_O}'"""
        try:
            mycursor.execute(order)
            mydb.commit()
            hasil = "Berhasil Memperbarui Data"
        except mysql.connector.Error as error:
            hasil = f"Gagal Memperbarui data, error code: {error}"
        show_Popup(hasil)

    def getList():
        order = "Select * from topic"
        mycursor.execute(order)
        result = mycursor.fetchall()
        hasil =[]
        for i in result:
            a = str(i[0]) + " - " + str(i[1])
            hasil.append(a)
        return hasil

class Category():
    def __init__(self,name):
        self.nama = name

    def masukin(self):
        # Masukin datanya
        order = f"""INSERT INTO category
        (category_id, name) VALUES
        (NULL, '{self.nama}')"""
        mycursor.execute(order)
        mydb.commit()
        show_Popup("Berhasil Menginput Data")

    def hapus(ID):
        order = f"DELETE FROM topic WHERE category.category_id = {ID}"
        try:
            mycursor.execute(order)
            mydb.commit()
            hasil = "Berhasil Mengapus Data"
        except mysql.connector.Error as error:
            hasil = f"Gagal menghapus data, error code: {error}"
        return hasil

    def update(self,ID_O):
        order = f"""UPDATE category SET
        name = '{self.nama}'
        WHERE category.category_id = '{ID_O}'"""
        try:
            mycursor.execute(order)
            mydb.commit()
            hasil = "Berhasil Memperbarui Data"
        except mysql.connector.Error as error:
            hasil = f"Gagal Memperbarui data, error code: {error}"
        show_Popup(hasil)

    def getList():
        order = "Select * from category"
        mycursor.execute(order)
        result = mycursor.fetchall()
        hasil =[]
        for i in result:
            a = str(i[0]) + " - " + str(i[1])
            hasil.append(a)
        return hasil
