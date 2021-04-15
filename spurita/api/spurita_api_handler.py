import marshmallow
import werkzeug
from flask import jsonify

BAD_REQUEST = "error.validation.badRequest"
INTERNAL_SERVER_ERROR = "error.internalServerError"
NOT_FOUND = "error.notFound"


def error_handler(app):

    @app.errorhandler(marshmallow.exceptions.ValidationError)
    def handle_bad_request(e):
        app.logger.debug(e)
        return jsonify({"msg": BAD_REQUEST}), 400

    @app.errorhandler(werkzeug.exceptions.BadRequest)
    def handle_bad_request(e):
        app.logger.debug(e)
        return jsonify({"msg": BAD_REQUEST}), 400

    @app.errorhandler(werkzeug.exceptions.NotFound)
    def handle_bad_request(e):
        app.logger.debug(e)
        return jsonify({"msg": NOT_FOUND}), 404

    @app.errorhandler(Exception)
    def handle_exception(e):
        app.logger.exception(e)
        return jsonify({"msg": INTERNAL_SERVER_ERROR}), 500
