from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of the web server """
    return jsonify({"status": "OK"})
