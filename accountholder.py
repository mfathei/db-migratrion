
import MySQLdb as mdb
import sys


def getValue(val):
    if val is None :
        return 'NULL'
		
    return str.format("'{}'", str.replace(str.replace(str(val).strip(), "\\", ""), "'", "''") )

rep = """ SET FOREIGN_KEY_CHECKS=0; SET @TRIGGER_CHECKS = FALSE; TRUNCATE TABLE `Accountholder`; """
sql = """ SELECT a.*,cd.`card_id`,cd.`creation_date`,cd.`expiry_date`,(CASE cd.`is_valid` WHEN 1 THEN 'Valid' ELSE 'Expired' END),cd.`issue_date`,ao.`organization_id` FROM accountholder a JOIN card cd ON(a.`accountholder_id` = cd.`accountholder_id`) JOIN holders h ON (h.id = cd.`card_id`) LEFT JOIN `accountholder_organization` ao ON(ao.`accountholder_id` = a.`accountholder_id`) WHERE a.`accountholder_id` NOT IN('dev2-7caf0f3a-55ae-11e5-8275-90489af8fc48', 'dev2-845680af-55ae-11e5-8275-90489af8fc48');  """

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
            sql = str.format("INSERT INTO Accountholder select {0}, {1}, {2}, {3}, {4}, {5}, {6}, (select c.CityId from common_safetypass.City c where CityName = {7}), {8}, {9}, {10}, {11},"
                             "{12}, {13}, {14}, {15}, {16}, {17}, {18}, {19}, {20}, {21}, {22}, {23}, {24}, {25}, {26}, {27}, {28}, {29}, {30} from DUAL",
                          getValue(ROW[0]), getValue(ROW[1]), getValue(ROW[2]), getValue(ROW[4]), getValue(ROW[5]), getValue(ROW[6]), getValue(ROW[7]), getValue(ROW[8]) , getValue(ROW[11]), getValue(ROW[12]), getValue(ROW[13]), getValue(ROW[18]), getValue(ROW[23]), getValue(ROW[24]), getValue(ROW[25]),
                             getValue(ROW[26]), getValue(ROW[27]), getValue(ROW[28]), getValue(ROW[19]), '0', '0', 'NULL', getValue(ROW[22]), 'NULL', 'NULL', 'NULL', 'NULL', '1', 'NULL', 'NULL', getValue(ROW[22]))
            
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
