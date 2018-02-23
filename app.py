import json
import psycopg2
from psycopg2.extras import RealDictCursor
import sys
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

# @app.route('/restaurants/facility/(?<facility>.*)')
# @app.route('/restaurants/facility/(?{facility}.*)')
@app.route('/restaurants/facility/{facility}')
# @app.route('/restaurants/facility/zuppa')
def get_facility(facility):
  cursor.execute("SELECT * FROM public.restaurants WHERE facility = %(facility)s", {"facility":facility})
  records = cursor.fetchall()
  return {'results':str(records)}

@app.route('/hello/{name}')
def hello_name(name):
   # '/hello/james' -> {"hello": "james"}
   return {'hello': name}
#
@app.route('/users', methods=['POST'])
def create_user():
    # This is the JSON body the user sent in their POST request.
    user_as_json = app.current_request.json_body
    # We'll echo the json body back to the user in a 'user' key.
    return {'user': user_as_json}
