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

correctStatusText="<html><head/><body><p><span style=\" font-style:italic; color:#35B512;\">Authenticated</span></p></body></html>"
incorrectStatusText="<html><head/><body><p><span style=\" font-style:italic; color:#ff2b0f;\">Incorrect username or password</span></p></body></html>"
emptyStatusText="<html><head/><body><p><span style=\" font-style:italic; color:#ff2b0f;\">fields cannot be empty</span></p></body></html>"
"""
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
"""
ldapAdmin="qgis"
ldapAdminPass="P@$$123"
atemptsCount=0

def ldapConLogin(username,password):
    global atemptsCount
    if (username=="" or password==""):

        form.username.clear()
        form.password.clear()
        form.username.setFocus()
        form.status_label.setText(emptyStatusText)
    else:
        con = ldap.initialize(server)
        user = str(username)
        pwd = str(password)
        con.protocol_version=ldap.VERSION2

        try:
            #print con.bind_s(ldapAdmin, ldapAdminPass,ldap.AUTH_SIMPLE)
            print con.bind_s(user, pwd,ldap.AUTH_SIMPLE)
            print "bind successful"
            form.status_label.setText(correctStatusText)

            global authenticated
            authenticated=True
            print "authenticated user"

            file=open("../logfile","w+")

            if(authenticated):
                #form.hide()
                file.write(writeText)
                #subprocess.call(openFile)
                file.close()
                file=open("../logfile","w+")
                file.write("")
                file.close()
                #app.quit()

        except ldap.INVALID_CREDENTIALS:
            form.username.clear()
            form.password.clear()
            form.username.setFocus()
            form.status_label.setText(incorrectStatusText)
            print "invalid credentials"
            atemptsCount+=1
            if atemptsCount==3:
                sys.exit(0)
        except ldap.LDAPError, e:
            if type(e.message) == dict and e.message.has_key('desc'):
                print e.message['desc']
            else:
                print e

def search(con,keyword,uname,upass):

    print con.bind_s(ldapAdmin, ldapAdminPass,ldap.AUTH_SIMPLE)

    timeout=3

    baseDN = "ou=RECS,DC=cadaster,DC=local"
    searchScope = ldap.SCOPE_SUBTREE

    retrieveAttributes = None
    searchFilter = "cn=" + keyword
    #print searchFilter

    try:
        ldap_result_id =con.search(baseDN,searchScope,searchFilter,retrieveAttributes)

        result_set = []

        while 1:
            result_type, result_data = con.result(ldap_result_id, timeout)

            if (result_data ==[]):
                break
            else:
                if result_type == ldap.RES_SEARCH_ENTRY:
                    result_set.append(result_data)
        #print result_set
        #print "login succesful"

    except ldap.INVALID_CREDENTIALS:
        print "Your username or password is incorrect."

    except ldap.LDAPError, e:
        if type(e.message) == dict and e.message.has_key('desc'):
            print e.message['desc']
        else:
            print e



class Form(QDialog,LoginFormui.Ui_loginFormMain):
    def __init__(self,parent=None):
        super(Form,self).__init__(parent)
        self.setupUi(self)
        self.connect(self.login_button,SIGNAL("clicked()"),self.logInfunc)
        self.connect(self.cancel_button,SIGNAL("clicked()"),app.quit)

    def logInfunc(self):
        ldapConLogin(self.username.text(),self.password.text())

app=QApplication(sys.argv)
form=Form()
form.show()
app.setQuitOnLastWindowClosed(True)
app.exec_()
