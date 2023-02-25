import sqlite3

try:
    con = sqlite3.connect("test.db")
    print("Got the connection.")
    # query = '''
    # CREATE TABLE Emp(eno INT Primary Key Not Null, ename text, desg text,
    # salary float)
    # '''

    # query = '''INSERT INTO Emp values(2,'XYZ','Officer',50000.0)'''

    con.execute("UPDATE Emp set ename='Saksham' where eno=%d"%(2))
    con.commit()
    print("Total records changed: ",con.total_changes)

    query = '''SELECT * FROM Emp'''

    cursor=con.execute(query)

    for row in cursor:
        print(row)


    # con.commit()
    con.close()
except Exception as e:
    print("Error", e)
