from PyQt5.QtWidgets import *
#import krita
from krita import * #change when testing

class Griddify(DockWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Griddify")

    def canvasChanged(self, canvas):
        pass

Krita.instance().addDockWidgetFactory(DockWidgetFactory("griddify", DockWidgetFactoryBase.DockRight, Griddify))

