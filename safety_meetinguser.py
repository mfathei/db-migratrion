
import MySQLdb as mdb
import sys


def getValue(val):
    if val is None :
        return 'NULL'

    return str.format("'{}'", str.replace(str(val).strip(), "'", "\\'") )


rep = """ SET FOREIGN_KEY_CHECKS=0; SET @TRIGGER_CHECKS = FALSE; TRUNCATE TABLE `SafetyMeetingUser`; """
sql = """ SELECT * FROM `safety_meeting_users` GROUP BY meeting_id, accountholder_id; """

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
            sql = str.format("INSERT INTO `SafetyMeetingUser` VALUES({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8});",
                          getValue(ROW[0]), getValue(ROW[1]), getValue(ROW[2]), getValue(ROW[3]), getValue(ROW[4]), getValue(ROW[5]), getValue(ROW[6]), getValue(ROW[10]),  getValue(ROW[10]))
            
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

