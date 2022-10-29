from PySide2.QtWidgets import QMainWindow, QFileDialog ,QMessageBox, QTableWidgetItem
from ui_mainWindow import Ui_MainWindow
from particle import Particle
from particle_list import  Particle_List

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.particle_list = Particle_List()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.addToStart_pushButton.clicked.connect(self.click_addStart)
        self.ui.addEnd_pushButton.clicked.connect(self.click_addEnd)
        self.ui.showListParticle_pushButton.clicked.connect(self.click_show)
        self.ui.actionAbrir.triggered.connect(self.action_abrir)
        self.ui.actionGuardar.triggered.connect(self.action_guardar)
        self.ui.search_pushButton.clicked.connect(self.search_tableParticle)
        self.ui.show_pushButton.clicked.connect(self.show_tableParticle)
    
    def search_tableParticle(self):
        id = self.ui.search_lineEdit.text()
        encontrado = False
        for particle in self.particle_list:
            print(id)
            print(particle.id)
            if(id == str(particle.id)):
                self.ui.particle_tableWidget.clear()
                headers = [ "ID", "Origen X","Origen Y","Destino X",
                    "Destino Y", "Velocidad","Rojo", "Verde", "Azul",
                    "Distancia"]
                self.ui.particle_tableWidget.setHorizontalHeaderLabels(headers)
                self.ui.particle_tableWidget.setRowCount(1)

                id_widget = QTableWidgetItem(str(particle.id))
                origen_x_widget = QTableWidgetItem(str(particle.origen_x))
                origen_y_widget = QTableWidgetItem(str(particle.origen_y))
                destino_x_widget = QTableWidgetItem(str(particle.destino_x))
                destino_y_widget = QTableWidgetItem(str(particle.destino_y))
                velocidad_widget = QTableWidgetItem(str(particle.velocidad))
                red_widget = QTableWidgetItem(str(particle.red))
                green_widget = QTableWidgetItem(str(particle.green))
                blue_widget = QTableWidgetItem(str(particle.blue))
                distance_widget = QTableWidgetItem(str(particle.distancia))

                self.ui.particle_tableWidget.setItem(0, 0, id_widget)
                self.ui.particle_tableWidget.setItem(0, 1, origen_x_widget)
                self.ui.particle_tableWidget.setItem(0, 2, origen_y_widget)
                self.ui.particle_tableWidget.setItem(0, 3, destino_x_widget)
                self.ui.particle_tableWidget.setItem(0, 4, destino_y_widget)
                self.ui.particle_tableWidget.setItem(0, 5, velocidad_widget)
                self.ui.particle_tableWidget.setItem(0, 6, red_widget)
                self.ui.particle_tableWidget.setItem(0, 7, green_widget)
                self.ui.particle_tableWidget.setItem(0, 8, blue_widget)
                self.ui.particle_tableWidget.setItem(0, 9, distance_widget)
                encontrado = True
                return
        if not encontrado:
            QMessageBox.warning(
                self, "Atencion",
                'La particula con el id ' + id + ' no fue encontrado...'
            )

    def show_tableParticle(self):
        self.ui.particle_tableWidget.setColumnCount(10)
        headers = [ "ID", "Origen X","Origen Y","Destino X",
            "Destino Y", "Velocidad","Rojo", "Verde", "Azul",
            "Distancia"]
        self.ui.particle_tableWidget.setHorizontalHeaderLabels(headers)
        self.ui.particle_tableWidget.setRowCount(len(self.particle_list))

        row = 0
        for particle in self.particle_list:
            id_widget = QTableWidgetItem(str(particle.id))
            origen_x_widget = QTableWidgetItem(str(particle.origen_x))
            origen_y_widget = QTableWidgetItem(str(particle.origen_y))
            destino_x_widget = QTableWidgetItem(str(particle.destino_x))
            destino_y_widget = QTableWidgetItem(str(particle.destino_y))
            velocidad_widget = QTableWidgetItem(str(particle.velocidad))
            red_widget = QTableWidgetItem(str(particle.red))
            green_widget = QTableWidgetItem(str(particle.green))
            blue_widget = QTableWidgetItem(str(particle.blue))
            distance_widget = QTableWidgetItem(str(particle.distancia))

            self.ui.particle_tableWidget.setItem(row, 0, id_widget)
            self.ui.particle_tableWidget.setItem(row, 1, origen_x_widget)
            self.ui.particle_tableWidget.setItem(row, 2, origen_y_widget)
            self.ui.particle_tableWidget.setItem(row, 3, destino_x_widget)
            self.ui.particle_tableWidget.setItem(row, 4, destino_y_widget)
            self.ui.particle_tableWidget.setItem(row, 5, velocidad_widget)
            self.ui.particle_tableWidget.setItem(row, 6, red_widget)
            self.ui.particle_tableWidget.setItem(row, 7, green_widget)
            self.ui.particle_tableWidget.setItem(row, 8, blue_widget)
            self.ui.particle_tableWidget.setItem(row, 9, distance_widget)

            row += 1

    def action_abrir(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        ) [0]
        if(self.particle_list.abrir(ubicacion)):
            QMessageBox.information(
                self,
                "Exito",
                "Se pudo abrir el archivo" + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo abrir el archivo" + ubicacion
            )

    def action_guardar(self):

        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        ) [0]
        if(self.particle_list.guardar(ubicacion)):
            QMessageBox.information(
                self,
                "Exito",
                "Se pudo crear el archivo" + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo crear el archivo" + ubicacion
            )

    def click_addStart(self):
        self.particle_list.addFirst(self.make_particle())
        self.reset_spinBoxs()

    def click_addEnd(self):
        self.particle_list.addToEnd(self.make_particle())
        self.reset_spinBoxs()

    def click_show(self):
        self.ui.particle_PlainText.clear()
        self.ui.particle_PlainText.insertPlainText(str(self.particle_list))

    def make_particle(self)->Particle:
        id = self.ui.id_lineEdit.text()
        x1 = self.ui.originX_spinBox.value()
        y1 = self.ui.originY_spinBox.value()
        x2 = self.ui.destX_spinBox.value()
        y2 = self.ui.destY_spinBox.value()
        speed = self.ui.speed_spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()
        myParticle = Particle(id, x1, y1, x2, y2, speed, red, green, blue)
        return myParticle

    def reset_spinBoxs(self):
        id = self.ui.id_lineEdit.setText("")
        self.ui.originX_spinBox.setValue(0)
        self.ui.originY_spinBox.setValue(0)
        self.ui.destX_spinBox.setValue(0)
        self.ui.destY_spinBox.setValue(0)
        self.ui.speed_spinBox.setValue(0)
        self.ui.red_spinBox.setValue(0)
        self.ui.green_spinBox.setValue(0)
        self.ui.blue_spinBox.setValue(0)
