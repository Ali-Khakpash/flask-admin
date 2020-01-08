from flask_authorize import Authorize
from flask_login import current_user
authorize = Authorize(current_user = current_user)