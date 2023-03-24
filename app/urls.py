from app import appbuilder
from .view import *


appbuilder.app.add_url_rule("/resister_view", methods=["POST"], view_func=resister_view)

appbuilder.app.add_url_rule("/login_view", methods=["POST"], view_func=login_view)

appbuilder.app.add_url_rule("/ticket_booking/<user_id>", methods=["POST"], view_func=ticket_booking)

appbuilder.app.add_url_rule("/history/<user_id>", methods=["POST"],view_func=history)

appbuilder.app.add_url_rule("/cancel_ticket/<user_id>", methods=["POST"],view_func=cancel_ticket)

appbuilder.app.add_url_rule("/seating_details", methods=["POST"],view_func=seating_details)

############################################ admin ######################################################

appbuilder.app.add_url_rule("/admin_reg", methods=["POST"],view_func=admin_reg)

appbuilder.app.add_url_rule("/theatre_details/<user_id>", methods=["POST"],view_func=theatre_details)

appbuilder.app.add_url_rule("/theatre_details_show/<user_id>", methods=["POST"],view_func=theatre_details_show)

appbuilder.app.add_url_rule("/edit_admin_user/<user_id>", methods=["POST"],view_func=edit_admin_user)

appbuilder.app.add_url_rule("/edit_admin_user/<user_id>/<theatre_id>", methods=["POST"],view_func=edit_admin_user)