from flask import Flask, request, g

from dal.item_controller_factory import get_item_controller

app = Flask(__name__)

g.item_controller = get_item_controller("excel")


@app.route("/item", methods=["POST", "GET"])
def generic_item_action():
    if request.method == "POST":


@app.route("/item/<item_id>", methods=["PATCH", "DELETE", "GET"])
def specific_item_action(item_id):
    pass


if __name__ == '__main__':
    app.run("0.0.0.0", 5000, True, threaded=False, processes=1)
