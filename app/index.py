from flask import Blueprint, render_template, request
from app.utils.form import ContentForm

bp = Blueprint("index", __name__)

@bp.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "GET":
        content_form = ContentForm()
        return render_template("index.html", content_form=content_form)
    else:
        content_form = ContentForm(request.form)
        if content_form.validate():
            return render_template("result.html", result=request.form)
        return render_template("index.html", content_form=content_form)

@bp.route("/collection", methods=["GET"])
def collection():
    return render_template("collection.html")

@bp.route("/", methods={"GET"})
def graph():
    return render_template("graph.html")