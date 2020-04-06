from __init__ import *
from config import Config


app = create_app(Config).run(port=1861, debug=Config.DEBUG)
