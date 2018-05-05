
import MySQLdb as mdb
import sys


def getValue(val):
    if val is None :
        return 'NULL'        
    
    return str.format("'{}'", str.replace(str(val).strip(), "'", "\\'") )

sql0 = """ SET FOREIGN_KEY_CHECKS=0, @TRIGGER_CHECKS = FALSE; TRUNCATE TABLE OrgContact; """
sql = """ SELECT * FROM organization; """
sql2 = """ SELECT * FROM common_safetypass.ContactType WHERE `ContactTypeName` = 'Mailing'; """
sql3 = """ SELECT * FROM common_safetypass.ContactType WHERE `ContactTypeName` = 'Billing'; """

resultset = []
try:
    conn = mdb.connect('192.168.171.159', 'root', 'UrszulabIham1', 'safetypass')
    conndev = mdb.connect('192.168.171.152', 'devuser', 'Ngtgmn', 'SafetyPass')
    try:
        # sql = line.replace(un, "")
        cursor = conn.cursor()
        c = conndev.cursor()
        c.execute(sql0)
        #########
        c.execute(sql2)
        mailing = c.fetchone()[0]
        c.execute(sql3)
        billing = c.fetchone()[0]
        #########
        cursor.execute(sql)
        resultset = cursor.fetchall()
        for ROW in resultset:
            #print(row)
            if ROW[1] == ' FMC Technologies - Completions' :
                continue
            # mailing
            sql = str.format("INSERT INTO OrgContact values( {0}, {1}, {2}, IFNULL((SELECT `CityId` FROM `common_safetypass`.`City` WHERE `CityName` = {3}), '879d07ec-49ba-11e6-b517-525400a5e0b3') , {4}, {5}, {6}, {7}, {8} ) ;",
                          'UUID()', getValue(ROW[0]), getValue(ROW[8]), getValue(ROW[9]), getValue(ROW[12]), getValue(ROW[13]), getValue(ROW[14]), getValue(mailing), getValue(ROW[19]))
            # billing
            sql2 = str.format("INSERT INTO OrgContact values( {0}, {1}, {2}, IFNULL((SELECT `CityId` FROM `common_safetypass`.`City` WHERE `CityName` = {3}), '879d07ec-49ba-11e6-b517-525400a5e0b3') , {4}, {5}, {6}, {7}, {8} ) ;",
                          'UUID()', getValue(ROW[0]), getValue(ROW[3]), getValue(ROW[4]), getValue(ROW[7]), getValue(ROW[13]), getValue(ROW[14]), getValue(billing), getValue(ROW[19]))

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



        
    
