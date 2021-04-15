from flask import request

from . import auth_api as app

from marshmallow import Schema, fields, validate


class RegisterSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1))
    email = fields.Email(required=True, validate=validate.Length(min=1))
    password = fields.Str(required=True, validate=validate.Length(min=8))
    passwordConfirmation = fields.Str(required=True, validate=validate.Equal(password))


@app.route("/register", methods=["POST"])
def register():
    form = RegisterSchema().load(request.json)
    return {}
