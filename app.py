from flask import (
    Flask,
    render_template,
    request
)

def get_custom_url():
    import os
    return os.environ.get("CUSTOM_DOMAIN_URL", "")

app = Flask(__name__)

@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    subpath = request.path
    fullpath = f"{get_custom_url()}{subpath}"
    return render_template(
        "index.html",
        url=fullpath,
        justification="center",
    )


@app.route("/about")
def about():
    subpath = request.path
    fullpath = f"{get_custom_url()}{subpath}"
    return render_template(
        "about.html",
        url=fullpath,
        justification="left",
    )

@app.route("/contact")
def contact():
    subpath = request.path
    fullpath = f"{get_custom_url()}{subpath}"
    return render_template(
        "contact.html",
        url=fullpath,
        justification="left",
    )

@app.errorhandler(404)
def error(e):
    fullpath = f"{get_custom_url()}/404"
    return render_template(
        "404.html",
        url=fullpath
    )

if __name__ == "__main__":
    app.run()
