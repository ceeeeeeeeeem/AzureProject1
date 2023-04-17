from flask import Flask, render_template
import pyodbc

server = 'miyavserver.database.windows.net'
database = 'miyavDB'
username = 'miyavAdmin'
password = '{PisiPisi1}'
driver= '{ODBC Driver 18 for SQL Server}'

data = []

class CatData:
    def __init__(self,cat_name, min_life_expectancy, max_life_expectancy):
        self.max_life_expectancy = max_life_expectancy
        self.cat_name = cat_name
        self.min_life_expectancy = min_life_expectancy
        pass

with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM Cat_Data")
        row = cursor.fetchone()
        while row:
            data.append(CatData(str(row[0]),str(row[3]),str(row[4])))
            row = cursor.fetchone()

print (data)
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('hello.html', data=data)