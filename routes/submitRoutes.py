from flask import Blueprint
from controllers.submitController import submit as submit_controller

submitRoutes_blueprint = Blueprint("submitRoutes", __name__)


@submitRoutes_blueprint.route("/submit", methods=["POST"])
def submit():
    return submit_controller()