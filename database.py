from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import json, os

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# SECRET_FILE = os.path.join(BASE_DIR, 'secrets.json')
# secrets = json.loads(open(SECRET_FILE).read())
#
# DB = secrets["DB"]

# DB_URL = f"mysql+pymysql://DB['user']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['database']}?utf8"

DB_URL = "mysql://root:root@127.0.0.1:3306/threat_detection"

engine = create_engine(
    DB_URL, encoding = 'utf-8'
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

