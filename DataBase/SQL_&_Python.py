import os
import sqlite3

conn = sqlite3.connect('data-2.db')



fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Storage( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileList TEXT, \
        col_Time\
        )")
    conn.commit()
conn.close()

#========================================================

for data in fileList:
    suffix = '.txt'
    textFile = data.endswith(suffix)
    if textFile == True:
         print(data)

    

#=========================================================


conn = sqlite3.connect('data-2.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO Storage(col_fileList, col_Time) VALUES(?,?)", \
                (data,'87'))
    conn.commit()
conn.close()






"""
conn = sqlite3.connect('data-2.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_fileList,col_time FROM Storage WHERE col_fileList = 'Bob'")
    varPerson = cur.fetchall()
    for item in varPerson:
        msg = "First name: {} \nTime of edit: {} \n".format(item[0], item[1])
    print(msg)
"""


