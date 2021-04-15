from . import status_api as app


@app.route("/", methods=["GET"])
def basic_status():
    return {}
