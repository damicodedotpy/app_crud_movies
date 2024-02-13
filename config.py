# ******************************PYTHON LIBRARIES******************************
import os
# ******************************EXTERNAL LIBRARIES****************************

# ******************************OWN LIBRARIES*********************************

# ***********************************CODE*************************************
class AppConfiguration(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE", "sqlite:///data.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False