from flask import Blueprint

auth_api = Blueprint("auth", __name__, url_prefix="/v1/auth")

from . import register # noqa