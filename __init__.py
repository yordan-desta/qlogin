import subprocess
import LoginFormui
import sys
from PyQt4.QtCore import  *
from PyQt4.QtGui import *


user="root"
pwd="pass"
authenticated= False
openFile="/home/pyordan/build-master2.6/output/bin/qgis"
writeText="user is authenticated"
def sendToprinter(username,password):
    file=open("/home/pyordan/logfile","w+")
    
    file.write("&*********************&&&**%#$")

    print username,":",password


    if (username == user) and (password == pwd):
        global authenticated
        authenticated=True
        print "authenticated user"
    else:
        form.username.clear()



    file.write("username@"+str(username) +"\npassword@"+ str(password))

    if(authenticated):
        form.hide()
        print "authenticated"
        file.write(writeText)
        subprocess.call(openFile)
        file.write("^^&$%&*(YHHYGYUVF(&&*)()(UIHG^FYUGYU^S%^&TUTYTYTRTWJHGYGGI#*")
        app.quit()



class Form(QDialog,LoginFormui.Ui_loginFormMain):
    def __init__(self,parent=None):
        super(Form,self).__init__(parent)

        self.setupUi(self)

        self.connect(self.login_button,SIGNAL("clicked()"),self.logInfunc)
        self.connect(self.cancel_button,SIGNAL("clicked()"),app.quit)

    def logInfunc(self):
        print "Logged in by:user ",self.username.text(),":\n","password: ",self.password.text()

        sendToprinter(self.username.text(),self.password.text())

app=QApplication(sys.argv)
form=Form()
form.show()
app.setQuitOnLastWindowClosed(True)
app.exec_()
