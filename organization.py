
import MySQLdb as mdb
import sys


def getValue(val):
    if val is None :
        return 'NULL'        
    
    return str.format("'{}'", str.replace(str(val).strip(), "'", "\\'") )


sql1 = """ SET FOREIGN_KEY_CHECKS=0, @TRIGGER_CHECKS = FALSE;"""
sql = """ SELECT * FROM organization; """
sql2 = """ UPDATE `Organization` SET `ParentOrgId` = 'dev2-30a3928e-55b5-11e5-8275-90489af8fc48' WHERE `OrgId` = 'dev2-2cfd1295-55b5-11e5-8275-90489af8fc48' OR `OrgId` = 'dev2-30660493-55b5-11e5-8275-90489af8fc48' ; """

resultset = []
try:
    conn = mdb.connect('192.168.171.159', 'root', 'UrszulabIham1', 'safetypass')
    conndev = mdb.connect('192.168.171.152', 'devuser', 'Ngtgmn', 'SafetyPass')
    try:
        # sql = line.replace(un, "")
        cursor = conn.cursor()
        c = conndev.cursor()
        c.execute(sql1)
        cursor.execute(sql)
        resultset = cursor.fetchall()
        for ROW in resultset:
            #print(row)
            if ROW[1] == ' FMC Technologies - Completions' :
                continue
            
            sql = str.format("INSERT INTO `Organization` values( {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}) ;",
                          getValue(ROW[0]), getValue(ROW[1]), getValue(ROW[2]), getValue(ROW[13]), getValue(ROW[14]), getValue(ROW[15]), getValue(ROW[16]), 'NULL', getValue(ROW[17]), getValue('organization'), getValue(ROW[19]), getValue(ROW[19]))
            #print(sql)
            c.execute(sql)
        c.execute(sql2)
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



        
    
