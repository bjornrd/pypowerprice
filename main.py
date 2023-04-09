import sys
from pyentsoe.entsoe import core

from PySide6 import QtCore, QtWidgets
from ui import Application

if __name__ == '__main__':
#    pricedata = core.getPriceData(core.Zone.NO4, currency=core.Currencies.NOK)
#
#    if pricedata is not None:
#        print(pricedata.price)
#        print(pricedata.resolution)
#        print(pricedata.description)

    app = QtWidgets.QApplication([])

    QtCore.QCoreApplication.setApplicationName("PowerPrice")
    QtCore.QCoreApplication.setOrganizationDomain("")

    main_window = Application.ApplicationMainWindow()
    main_window.show()

    sys.exit(app.exec())

    