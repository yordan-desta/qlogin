import subprocess
import LoginFormui
import sys
from PyQt4.QtCore import  *
from PyQt4.QtGui import *
import ldap

server="LDAP://172.20.0.71"
user="root"
pwd="pass"
authenticated= False
openFile="../../bin/qgis"
writeText="user is authenticated"
statusText="<html><head/><body><p><span style=\" font-style:italic; color:#ff2b0f;\">Incorrect username or password</span></p></body></html>"

def sendToprinter(username,password):
    file=open("../logfile","w+")

    print username,":",password


    if (username == user) and (password == pwd):
        global authenticated
        authenticated=True
        print "authenticated user"
    else:
        form.username.clear()
        form.password.clear()
        form.username.setFocus()
        form.status_label.setText(statusText)



    file.write("username@"+str(username) +"\npassword@"+ str(password))

    if(authenticated):
        form.hide()
        print "authenticated"
        file.write(writeText)
        subprocess.call(openFile)
        file.write("")
        file.close()
        app.quit()
""" """
def ldapConLogin(username,password):
    con = ldap.initialize(server)
    who = str(username)
    cred = str(password)
    con.protocol_version=ldap.VERSION2

    try:

        con.bind("qgis", "P@$$123",ldap.AUTH_SIMPLE)
        print "bind successful"

        baseDN = "ou=RECS,DC=cadaster,DC=local"
        searchScope = ldap.SCOPE_SUBTREE

        retrieveAttributes = None
        searchFilter = "cn=qgis"

        try:
            ldap_result_id =con.search(baseDN,searchScope,searchFilter,retrieveAttributes)

            result_set = []

            while 1:
                print "here is the problem"
                result_type, result_data = con.result(ldap_result_id, 0)

                if (result_data == []):
                    print "empty result data"
                    break
                else:
                    if result_type == ldap.RES_SEARCH_ENTRY:
                        result_set.append(result_data)
            print result_set

        except ldap.INVALID_CREDENTIALS:
            print "Your username or password is incorrect."
        except ldap.LDAPError, e:
            print e

    except ldap.INVALID_CREDENTIALS:
        print "invalid credentials"
    except ldap.LDAPError, e:
        if type(e.message) == dict and e.message.has_key('desc'):
            print e.message['desc']
        else:
            print e
        print "can't connect to the server"
        sys.exit()

class Form(QDialog,LoginFormui.Ui_loginFormMain):
    def __init__(self,parent=None):
        super(Form,self).__init__(parent)

        self.setupUi(self)


        self.connect(self.login_button,SIGNAL("clicked()"),self.logInfunc)
        self.connect(self.cancel_button,SIGNAL("clicked()"),app.quit)

    def logInfunc(self):
        print "Logged in by:user ",self.username.text(),":\n","password: ",self.password.text()

        sendToprinter(self.username.text(),self.password.text())
        ldapConLogin(self.username.text(),self.password.text())

app=QApplication(sys.argv)
form=Form()
form.show()
app.setQuitOnLastWindowClosed(True)
app.exec_()
