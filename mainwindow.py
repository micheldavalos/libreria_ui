from PySide2.QtWidgets import QMainWindow, QMessageBox, QFileDialog
from ui_mainwindow import Ui_MainWindow
from PySide2.QtCore import Slot
from libreria import Libreria, Libro

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Conexiones de los botones
        self.ui.agregar_pushButton.clicked.connect(self.agregar_inicio)
        self.ui.mostrar_pushButton.clicked.connect(self.mostrar)
        self.ui.agregar_final_pushButton.clicked.connect(self.agregar_final)
        self.ui.eliminar_pushButton.clicked.connect(self.eliminar)
        self.ui.modificar_pushButton.clicked.connect(self.modificar)

        # Conexiones de las actions
        self.ui.actionAbrir.triggered.connect(self.abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.guardar_archivo)

        self.libreria = Libreria()

    Slot()
    def abrir_archivo(self):
        ubicacion = QFileDialog.getOpenFileName(self, 'Abrir Archivi', '.', 'JSON (*.json)')
        ubicacion = ubicacion[0]
        print(ubicacion)
        
        if self.libreria.abrir(ubicacion):
            QMessageBox.information(self, 'Abrir archivo', 'Se abrió el archivo')
            self.mostrar
        else:
            QMessageBox.critical(self, 'Abrir archivo', 'Error al abrir el archivo')


    Slot()
    def guardar_archivo(self):
        ubicacion = QFileDialog.getSaveFileName(self, 'Guardar Archivo', '.', 'JSON (*.json)')
        ubicacion = ubicacion[0]
        if self.libreria.guardar(ubicacion):
            QMessageBox.information(self, 'Creación del archivo', 'Se creó el archivo')
        else:
            QMessageBox.critical(self, 'Creación del archivo', 'Hubo un error al crear el archivo')

    Slot()
    def agregar_inicio(self):
        titulo = self.ui.titulo_lineEdit.text()
        autor = self.ui.autor_lineEdit.text()
        publicado = self.ui.publicado_spinBox.value()
        editorial = self.ui.editorial_lineEdit.text()

        libro = Libro(titulo=titulo, autor=autor, publicado=publicado, editorial=editorial)

        self.libreria.agregar_inicio(libro)

        QMessageBox.information(self, 'Éxito!', 'Se agregó un libro a la libreria')

        self.ui.titulo_lineEdit.clear()
        self.ui.autor_lineEdit.clear()
        self.ui.editorial_lineEdit.clear()

    Slot()
    def mostrar(self):
        self.ui.plainTextEdit.clear()
        self.libreria.mostrar()
        self.ui.plainTextEdit.insertPlainText(str(self.libreria))

    Slot()
    def agregar_final(self):
        titulo = self.ui.titulo_lineEdit.text()
        autor = self.ui.autor_lineEdit.text()
        publicado = self.ui.publicado_spinBox.value()
        editorial = self.ui.editorial_lineEdit.text()

        libro = Libro(titulo=titulo, autor=autor, publicado=publicado, editorial=editorial)

        self.libreria.agregar_final(libro)

        QMessageBox.information(self, 'Éxito!', 'Se agregó un libro a la libreria')

        self.ui.titulo_lineEdit.clear()
        self.ui.autor_lineEdit.clear()
        self.ui.editorial_lineEdit.clear()

    Slot()
    def eliminar(self):
        id = self.ui.id_spinBox.value()
        ok = self.libreria.eliminar(id)
        if ok:
            QMessageBox.information(self, 'Éxito!', f'Se elimino el libro {id}')
        else:
            QMessageBox.critical(self, 'Error', f'No fue posible eliminar el libro {id}')

    Slot()
    def modificar(self):
        titulo = self.ui.titulo_lineEdit.text()
        autor = self.ui.autor_lineEdit.text()
        publicado = self.ui.publicado_spinBox.value()
        editorial = self.ui.editorial_lineEdit.text()

        libro = Libro(titulo, autor, publicado, editorial)

        id = self.ui.id_spinBox.value()

        ok = self.libreria.modificar(id, libro)
        if ok:
            QMessageBox.information(self, 'Éxito!', f'Se modificó el libro {id}')
            self.mostrar()
        else:
            QMessageBox.critical(self, 'Error', f'No fue posible modificar el libro {id}')

