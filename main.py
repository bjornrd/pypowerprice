import sys
from time import localtime, strftime
from pyentsoe.entsoe import core

from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QApplication

from PySide6.QtQml import QQmlApplicationEngine, QQmlContext
from PySide6.QtCore import QObject, Property, Signal
from PySide6.QtCharts import *



class PriceDataGetter(QObject):
    def __init__(self):
        QtCore.QObject.__init__(self)
        self.pricedata = core.getPriceData(core.Zone.NO4, currency=core.Currencies.NOK)

    # Description
    # ----------------
    def get_description(self) -> str:
        return self.pricedata.description
    
    def set_desription(self, description: str) -> None:
        self.pricedata.description = description

    @Signal
    def description_changed(self):
         pass
    
    description = Property(str, get_description, set_desription, notify=description_changed)

    # Price data
    # ----------------
    def get_price_data(self) -> list [float]:
        return self.pricedata.price

    @Signal
    def price_data_changed(self):
        pass

    price_data = Property('QVariantList', get_price_data, notify=price_data_changed)



if __name__ == '__main__':
    pricedata = PriceDataGetter()
#
#    if pricedata is not None:
#        print(pricedata.price)
#        print(pricedata.resolution)
#        print(pricedata.description)

    app = QApplication(sys.argv)

    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    
    description = "NOK/MWh" #pricedata.description
    engine.rootContext().setContextProperty('pricedata', pricedata)
    
    engine.load('ui/applicationMainWindow.qml')



    sys.exit(app.exec())

    