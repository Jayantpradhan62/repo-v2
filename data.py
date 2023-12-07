import sqlalchemy

from sqlalchemy import text

import pymysql


from sqlalchemy import create_engine

import os



my_secret = os.environ['DATA_SECRET']

engine = create_engine(my_secret,connect_args = {
  "ssl":{
    "ssl_ca": "/etc/ssl/cert.pem"
    
  }
})

def load_from_database():

  with engine.connect() as con:
    result = con.execute(text("select * from plans"))

  x = result.all()

  y = []


  for u in x:
    u_as_dict = u._mapping
    y.append(dict(u_as_dict))

  return y

def tex(id):
  te = f"select * from plans where id = {id} "
  return te
   


def plan_details(id):
  with engine.connect() as con:
    result = con.execute(
      text(tex(id))
    )
    re = result.all()

    re_dict = re[0]._mapping
    

    return dict(re_dict)

m = plan_details(2)

print(m)

print(type(m))











