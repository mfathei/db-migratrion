
import MySQLdb as mdb
import sys


def getValue(val):
    if val is None :
        return 'NULL'

    return str.format("'{}'", str.replace(str(val).strip(), "'", "\\'") )


rep = """ SET FOREIGN_KEY_CHECKS=0; SET @TRIGGER_CHECKS = FALSE; TRUNCATE TABLE common_safetypass.`State`; """
sql = """SELECT DISTINCT(state) AS st,(CASE WHEN country IS NULL OR TRIM(country) = "" THEN "test" ELSE country END) AS cntry FROM accountholder GROUP BY st HAVING st <> ""; """

resultset = []
try:
    conn = mdb.connect('192.168.171.159', 'root', 'UrszulabIham1', 'safetypass')
    conndev = mdb.connect('192.168.171.152', 'devuser', 'Ngtgmn', 'common_safetypass')
    try:
        # sql = line.replace(un, "")
        cursor = conn.cursor()
        c = conndev.cursor()
        #######################
        c.execute(rep)
        #######################
        cursor.execute(sql)
        resultset = cursor.fetchall()
        for ROW in resultset:
            #print(row)
            sql = str.format("INSERT INTO `State` select {0}, {1}, {2}, {3} from Country where CountryName = {4};",
                          'UUID()', 'CountryId', getValue(ROW[0]), 'NULL', getValue(ROW[1]))
            
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



        
    
