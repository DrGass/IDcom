from flask import Flask, Response, render_template, json
from flask_restful import Api, Resource
import sqlite3
from werkzeug.exceptions import HTTPException

# Sql

# conn = sqlite3.connect("IDcom.db")

# c = conn.cursor()

# conn.commit()
# conn.close()

# Flask


app = Flask(__name__)
api = Api(app)

# Error handling
customErrorDesc = {
    400: "Bad request",
    403: "Forbidden",
    404: "Not Found",
    500: "Internal server error",
}


@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps(
        {
            "code": e.code,
            "type": e.name,
            "description": customErrorDesc[e.code],
        }
    )
    response.content_type = "application/json"
    return response

# ping
class Ping(Resource):
    def get(self):
        return {"response": "pong"}


api.add_resource(Ping, "/ping")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
