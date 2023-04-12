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


# @app.route("/")
# def index():
#     return "Start"


# @app.route("/ping")
# def ping():
#     return "pong"


def restOfShit():
    # @app.route('/site/{site_id}/module/gallery')
    # def gallery(site_id):
    #     return 'gallery'

    # @app.route('/site/{site_id}/module/gallery/{gallery_id}')
    # def galleryChoice(site_id,gallery_id):
    #     return 'galleryChoice'

    # @app.route('/site/{site_id}/module/gallery/{gallery_id}/move_up')
    # def galleryMoveUp(site_id,gallery_id):
    #     return 'galleryMoveUp'

    # @app.route('/site/{site_id}/module/gallery/{gallery_id}/move_down')
    # def galleryMoveDown(site_id,gallery_id):
    #     return 'galleryMoveDown'

    # @app.route('/site/{site_id}/module/gallery/{gallery_id}/photos/update')
    # def galleryUpdate(site_id,gallery_id):
    #     return 'galleryUpdate'

    # @app.route('/site/{site_id}/module/gallery/{gallery_id}/photo/{photo_id}')
    # def photoChoice(site_id,gallery_id,photo_id):
    #     return 'photoChoice'

    # @app.route('/site/{site_id}/module/gallery/{gallery_id}/photo/{photo_id}/update')
    # def photoUpdate(site_id,gallery_id,photo_id):
    #     return 'photoUpdate'

    # @app.route('/site/{site_id}/module/gallery/{gallery_id}/photo/{photo_id}/move_up')
    # def photoMoveUp(site_id,gallery_id,photo_id):
    #     return 'photoMoveUp'

    # @app.route('/site/{site_id}/module/gallery/{gallery_id}/photo/{photo_id}/move_down')
    # def photoMoveDown(site_id,gallery_id,photo_id):
    #     return 'photoMoveUp'

    # @app.route('/site/{site_id}/module/subject')
    # def siteList(site_id):
    #     return 'siteList'

    # @app.route('/site/{site_id}/module/subject/{subject_id}')
    # def siteListSubject(site_id,subject_id):
    #     return 'stieListSubject'

    # @app.route('/site/{site_id}/module/subject/{row_prefix}/{row_id}')
    # def siteListRow(site_id,subject_id,row_prefix,row_id):
    #     return 'siteListRow'
    pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
