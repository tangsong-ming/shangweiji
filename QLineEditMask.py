from PyQt5.QtWidgets import *
import sys
class QLineEditMask(QWidget):
    def __init__(self):
        super(QLineEditMask, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('用掩码限制输入')
        formLayout=QFormLayout()

        ipLineEdit=QLineEdit()
        macLineEdit=QLineEdit()
        dataLineEdit=QLineEdit()
        licenseLineEdit=QLineEdit()

        ipLineEdit.setInputMask('000.000.000.000;_')
        macLineEdit.setInputMask('HH:HH:HH:HH:HH:HH;_')
        dataLineEdit.setInputMask('0000-00-00;_')
        licenseLineEdit.setInputMask('>AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#')
        formLayout.addRow('数字掩码',ipLineEdit)
        formLayout.addRow('mac掩码',macLineEdit)
        formLayout.addRow('日期掩码',dataLineEdit)
        formLayout.addRow('许可证掩码',licenseLineEdit)

        self.setLayout(formLayout)

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QLineEditMask()

    main.show()
    sys.exit(app.exec_())
