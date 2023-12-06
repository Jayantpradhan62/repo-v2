import sqlalchemy

from sqlalchemy import text

import pymysql


from sqlalchemy import create_engine



da =  "mysql+pymysql://ie1qyx7zcv465r6m3zeb:pscale_pw_slwVmHGWUlvrITlsNAxHpb5J0EudJS7iGIabukZxAXY@aws.connect.psdb.cloud/careerboost?charset=utf8mb4"

engine = create_engine(da,connect_args = {
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
    y.append(u_as_dict)

  return y


