
import MySQLdb as mdb
import sys


def getValue(val):
    if val is None :
        return 'NULL'

    return str.format("'{}'", str.replace(str(val).strip(), "'", "\\'") )


rep = """ SET FOREIGN_KEY_CHECKS=0; SET @TRIGGER_CHECKS = FALSE; TRUNCATE TABLE `AccountholderRole`; """
sql = """ SELECT * FROM accountholder_role; """

resultset = []
try:
    conn = mdb.connect('192.168.171.159', 'root', 'UrszulabIham1', 'safetypass')
    conndev = mdb.connect('192.168.171.152', 'devuser', 'Ngtgmn', 'SafetyPass')
    try:
        cursor = conn.cursor()
        c = conndev.cursor()
        #######################
        c.execute(rep)
        #######################
        cursor.execute(sql)
        resultset = cursor.fetchall()
        for ROW in resultset:
            #print(row)
            sql = str.format("INSERT INTO `AccountholderRole` select {0}, {1}, {2} from Role where RoleName = {3};",
                          getValue(ROW[1]), 'RoleId', getValue(ROW[2]),  getValue(ROW[0]))
            
            c.execute(sql)
        conndev.commit()
                          
    except mdb.Error as e:
        print(sql)
        print("Error {0:d}: {1}".format(e.args[0], e.args[1]))

except IOError as ioerr:
    print("Error {0:d}: {1}".format(ioerr.args[0], ioerr.args[1]))
except OSError as oserr:
    print("Error {0:d}: {1}".format(oserr.args[0], oserr.args[1]))
finally:  # we can use with block
    if conn:
        conn.close()
    if conndev:
        conndev.close()



        
    
