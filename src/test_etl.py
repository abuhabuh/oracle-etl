import cx_Oracle

con = cx_Oracle.connect('jwang/password@192.168.0.14:1521/pdborcl')
print con.version
con.close()

print 'asgasdfadsf'

