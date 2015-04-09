import subprocess
import LoginFormui
import sys
from PyQt4.QtCore import  *
from PyQt4.QtGui import *
import ldap
server=""
user="root"
pwd="pass"
authenticated= False
openFile="../../bin/qgis"
writeText="user is authenticated"

correctStatusText="<html><head/><body><p><span style=\" font-style:italic; color:#35B512;\">Authenticated</span></p></body></html>"
incorrectStatusText="<html><head/><body><p><span style=\" font-style:italic; color:#ff2b0f;\">Incorrect username or password</span></p></body></html>"
emptyStatusText="<html><head/><body><p><span style=\" font-style:italic; color:#ff2b0f;\">fields cannot be empty</span></p></body></html>"

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
        try:
            con = ldap.initialize(server)
            user = str(username)
            pwd = str(password)
            con.protocol_version=ldap.VERSION2
        except:
            form.displayErrorMsg("could not initialize connection with the server")

        try:
            con.bind_s(user, pwd,ldap.AUTH_SIMPLE)
            form.status_label.setText(correctStatusText)
            search(con,user)

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
                form.displayErrorMsg(e.message['desc'])
                print e.message['desc']
            else:
                print e

def search(con,keyword,uname="",upass=""):

    count=0
    timeout=0

    baseDN = "ou=RECS,DC=cadaster,DC=local"
    searchScope = ldap.SCOPE_SUBTREE

    retrieveAttributes = None
    searchFilter = "cn=" + keyword

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

        if len(result_set) == 0:
            print "No Results."
            return
        print result_set
        for i in range(len(result_set)):

            for entry in result_set[i]:

                try:
                    name = entry[1]['cn'][0]
                    userName=entry[1]['userPrincipalName'][0]
                    count = count + 1
                    print "%d.\nCName: %s\nUserName: %s\n" %\
                           (count, name,userName)
                except:
                    pass
                    print "here"

    except ldap.LDAPError, e:
        if type(e.message) == dict and e.message.has_key('desc'):
            form.displayErrorMsg(e.message['desc'])
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
    def displayErrorMsg(self,errorMsg):
        QMessageBox.warning(self,"Error",errorMsg)
def constructor():
    global server
    try:
        file=open("config","r+")
        rline=file.readlines()
        for line in rline:
            if line.startswith("#") or line.startswith("\n"):
                continue
            else:
                lsplit=line.split("=")

                if lsplit[0]=="server":
                    if lsplit[1]=="":
                        server="LDAP://localhost"
                    else:
                        server=lsplit[1]
        file.close()

    except:
        pass

if __name__=="__main__":
    constructor()

app=QApplication(sys.argv)
form=Form()
form.show()
app.setQuitOnLastWindowClosed(True)
app.exec_()
