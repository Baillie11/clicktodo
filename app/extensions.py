from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
mail = Mail()
migrate = Migrate()
csrf_protect = CSRFProtect()
login_manager = LoginManager()
