"""
DATABASES = {
    'default': {
        'ENGINE': 'django_hana',           # or as per your python path
        'NAME': 'DEESAW',           # The schema to use. It will be created if doesn't exist
        'USER': 'DEESAW',
        'PASSWORD': 'Deepa1234',
        'HOST': 'ussltcsnl1120.solutions.glbsnet.com',
        'PORT': '30015',
    }
}
"""
"""
from hdbcli import dbapi
connection = dbapi.connect(
    host="ussltcsnl1120.solutions.glbsnet.com",
    port='30015',
    user="DEESAW",
    password="Deepa1234"
)
"""
"""
import pyodbc 
conn = pyodbc.connect(Driver='{SQL Server}',
                      Server='D-DASH_Phase0_DQ',
                      Database='D-DASH_Phase0_DQ',
                      Trusted_Connection='yes')

cursor = connection.cursor()
a=cursor.execute("select count(*) from DEESAW.MARA")
print(a)
cursor.fetchone()
#Print("HELLO")
connection.close()"""

import pyodbc 
conn = pyodbc.connect("Driver={SQL Server};"               
                      "Server=10.118.23.78;"
                      "Database=D-DASH_Phase0_DQ;"
                      "UID=dsuser;"
                      "PWD=Password.1;"
                      #"Trusted_Connection=yes;"
                      )
                      #'user=dsuser;'
                      #'password=Password.1')
a="SELECT top 1 * from dbo.mara"
cursor = conn.cursor()
cursor.execute(a)
names = list(map(lambda x: x[0], cursor.description)) 
print(names)
#for row in cursor:
#    print(row)
conn.close()