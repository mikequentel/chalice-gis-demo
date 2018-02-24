import urllib
import cgi
import sys
import json
import psycopg2
from psycopg2.extras import RealDictCursor
from chalice import Chalice
app = Chalice(app_name='chalice-gis-demo')
conn_string = "host='localhost' dbname='businesses' user='postgres' password='postgres'"
conn = psycopg2.connect(conn_string)
cursor = conn.cursor(cursor_factory=RealDictCursor)

@app.route('/restaurants')
def restaurants():
  cursor.execute('SELECT * FROM public.restaurants LIMIT 100')
  records = cursor.fetchall()
  return {'results':str(records)}

@app.route('/restaurants/facility/{facility}')
def facility(facility):
  facility = urllib.unquote(facility)
  sql = "SELECT * FROM public.restaurants WHERE facility = %s"
  query = cursor.mogrify(sql, (facility,))
  print query
  cursor.execute(query)
  records = cursor.fetchall()
  return {'results':str(records)}

@app.route('/restaurants/oid/{oid}')
def oid(oid):
  oid = urllib.unquote(oid)
  sql = "SELECT * FROM public.restaurants WHERE oid = %s"
  query = cursor.mogrify(sql, (oid,))
  print query
  cursor.execute(query)
  records = cursor.fetchall()
  return {'results':str(records)}

