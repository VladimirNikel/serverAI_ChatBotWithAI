from aioflask import Flask

app = Flask(__name__)

from app import views
from app import logic_db

