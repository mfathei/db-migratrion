
import MySQLdb as mdb
import sys


def getValue(val):
    if val is None :
        return 'NULL'

    return str.format("'{}'", str.replace(str.replace(str(val).strip(), "\\", "\\\\"), "'", "\\'") )


rep = """ SET FOREIGN_KEY_CHECKS=0; SET @TRIGGER_CHECKS = FALSE;  """
sql = """ UPDATE `PrivilegeRole` SET `RoleId` = (SELECT `RoleId` FROM `Role` WHERE `RoleName` = 'sp_user') WHERE RoleId = 'Karim-eab1a78f-975d-11e5-8e75-90489af90556';  """
sql2 = """ UPDATE `PrivilegeRole` SET `RoleId` = (SELECT `RoleId` FROM `Role` WHERE `RoleName` = 'org_admin') WHERE RoleId = 'Karim-eab1a78f-975d-11e5-8e75-90489af90557'; """
sql3 = """ UPDATE `PrivilegeRole` SET `RoleId` = (SELECT `RoleId` FROM `Role` WHERE `RoleName` = 'supervisor') WHERE RoleId = 'Karim-eab1a78f-975d-11e5-8e75-90489af90558'; """

resultset = []
try:
    #conn = mdb.connect('192.168.171.159', 'root', 'UrszulabIham1', 'safetypass')
    conndev = mdb.connect('192.168.171.152', 'devuser', 'Ngtgmn', 'SafetyPass')
    try:
        c = conndev.cursor()
        #######################
        c.execute(rep)
        c.execute(sql)
        c.execute(sql2)
        c.execute(sql3)
        conndev.commit()
                          
    except mdb.Error as e:
        print(sql)
        print("Error {0:d}: {1}".format(e.args[0], e.args[1]))

except IOError as ioerr:
    print("Error {0:d}: {1}".format(ioerr.args[0], ioerr.args[1]))
except OSError as oserr:
    print("Error {0:d}: {1}".format(oserr.args[0], oserr.args[1]))
finally:  # we can use with block
    if conndev:
        conndev.close()



        
    
