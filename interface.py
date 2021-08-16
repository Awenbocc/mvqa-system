# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         interface
# Description:
# Author:       Boliu.Kelvin
# Date:         2021/5/26
# -------------------------------------------------------------------------------

from PyQt5.QtCore import QThread, pyqtSignal
import selector



class VQAsignal(QThread):
    # define signal, str tpye
    breakSignal = pyqtSignal(dict)

    def __init__(self, parent=None, question='',image= None):
        super().__init__(parent)
        self.q = question
        self.v = image


    def run(self):
        self.breakSignal.emit(selector.getResult(self.q,self.v))


