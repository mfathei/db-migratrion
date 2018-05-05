
import MySQLdb as mdb
import sys


def getValue(val):
    if val is None :
        return 'NULL'        
    
    return str.format("'{}'", str.replace(str(val).strip(), "'", "\\'") )

sql0 = """ SET FOREIGN_KEY_CHECKS=0, @TRIGGER_CHECKS = FALSE; TRUNCATE TABLE SecurityQuestion; """
sql = """ SELECT DISTINCT(`security_question_1`) AS q1 FROM `accountholder` HAVING q1 <> '' UNION  SELECT DISTINCT(`security_question_2`) AS q1 FROM `accountholder` HAVING q1 <> '' """
x = 1;
resultset = []
try:
    conn = mdb.connect('192.168.171.159', 'root', 'UrszulabIham1', 'safetypass')
    conndev = mdb.connect('192.168.171.152', 'devuser', 'Ngtgmn', 'SafetyPass')
    try:
        # sql = line.replace(un, "")
        cursor = conn.cursor()
        c = conndev.cursor()
        c.execute(sql0)
        cursor.execute(sql)
        resultset = cursor.fetchall()
        for ROW in resultset:
            #print(row)
            sql = str.format("INSERT INTO SecurityQuestion values( {0}, {1}, {2}, {3} ) ;",
                          'UUID()', getValue(ROW[0]),  getValue(x), 'CURRENT_TIMESTAMP()')
            x += 1
            #print(sql)
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



        
    
