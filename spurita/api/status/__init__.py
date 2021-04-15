from flask import Blueprint

status_api = Blueprint("status", __name__, url_prefix="/v1/status")

from . import status # noqa