from flask import render_template, request
from govdata.packages import bp

@bp.get("/")
def search():
    user_inputs = request.args
    # TODO your implementation goes here
    return render_template("packages.html", results = list(i for i in user_inputs.values() if i != "") )