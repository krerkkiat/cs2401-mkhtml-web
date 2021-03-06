# A simple server that parse the CS2401's Project 4 output file.
import os
import re

from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

from mkhtml import parse_swatches

ALLOWED_EXTENSIONS = {"txt"}

app = Flask(__name__)
# file size is limitted at 16 MB
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1] in ALLOWED_EXTENSIONS


def get_result(file):
    filename = secure_filename(file.filename)
    html = ""

    # Set up all variables and template.
    title = "Swatches from " + file.filename
    style = "div{margin:auto;} table{padding-bottom:60px;}"
    header = (
        "<html><head><title>"
        + title
        + '</title><style type="text/css">'
        + style
        + '</style></head><body><a href="'
        + url_for("upload_file")
        + '">back</a>'
    )
    swatch_template = '<td><div style="background-color:#{color};width:{width}px;height:{height}px;"></div></td>'
    footer = "</body></html>"

    html = html + header

    try:
        raw_data = file.stream.read()
        data = raw_data.decode("ascii")
    except Exception:
        redirect(
            url_for(
                "show_error",
                tetx="Error is encountered while decode the content of the file. Please use ASCII file instead.",
            )
        )

    body = parse_swatches(data.split("\n"))

    html = html + body + footer

    return html


@app.route("/disclaimer")
def show_disclaimer():
    return render_template("disclaimer.html")


@app.route("/error")
def show_error(text):
    return """
    <!doctype html>
    <title>Make HTML (CS2401 - Project 4)</title>
    <h3 style="color: red;">{text}</h3>
    """.format(
        text=text
    )


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["file"]
        if file and allowed_file(file.filename):
            return get_result(file)

    return render_template("home.html")


if __name__ == "__main__":
    app.debug = False
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
