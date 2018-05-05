
import MySQLdb as mdb
import sys

sql = "SELECT 'ABCanTrackV2.tab: ',count(*) as DefCount  FROM ABCanTrackV2.tab  where LanguageId=@LangId AND OrgId IS NULL"
cond = "AND OrgId IS NULL"
un = "UNION "

try:
    conn = mdb.connect('192.168.6.206', 'root', 'UrszulabIham1', 'CommonDB')
    outputfile = open("union.sql", "w")
    with open("TestAddLanguageonML.sql", "r") as f:
        for line in f:
            try:
                sql = line.replace(un, "")
                cursor = conn.cursor()
                cursor.execute(sql)
                outputfile.write(line)
            except mdb.Error as e:
                print("Error {0:d}: {1}".format(e.args[0], e.args[1]))
                if (int(e.args[0]) == 1054):
                    outputfile.write(line.replace(cond,''))
                    # sys.exit(1)
except IOError as ioerr:
    print("Error {0:d}: {1}".format(ioerr.args[0], ioerr.args[1]))
except OSError as oserr:
    print("Error {0:d}: {1}".format(oserr.args[0], oserr.args[1]))
finally:  # we can use with block
    if conn:
        conn.close()
    if outputfile:
        outputfile.close()
