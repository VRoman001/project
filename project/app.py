from flask import Flask, redirect, render_template, request
import db

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/learn")
def learn():
    return render_template("learn.html")

@app.route("/posts", methods=["GET", "POST"])
def post_list():
    if request.method == "POST":
        category_id = request.form.get("category_id")
        text = request.form.get("text", "").strip()
        try:
            category_id = int(category_id) if category_id not in (None, "") else None
        except ValueError:
            category_id = None
        if text:
            db.add_post(category_id, text)
        return redirect("/posts")

    return render_template("posts_lists.html", post_list=db.get_posts(), category=db.get_category())

@app.route("/category/add", methods=["POST"])
def add_category():
    name = request.form.get("name")
    if name:
        db.add_category(name)
    return redirect("/categories_posts")

@app.route("/categories")
def category_list():
    return render_template("category_lists.html", category_list=db.get_categories())

@app.route("/categories_posts")
def categories_posts():
    data = db.get_last_posts_by_category()
    return render_template("categories_posts.html", data=data)

@app.route("/category/<id>", methods=["GET", "POST"])
def PosByCategory(id):
    if request.method == "POST":
        category_id = request.form.get("category_id")
        text = request.form.get("text")
        db.add_post(category_id, text)
        return redirect(f"/category/{id}")

    return render_template("posts_lists.html", post_list=db.get_posts_by_category(id),
                           category_page=True,
                           category_id=id, category=db.get_category(id))

@app.route("/post/delete/<id>")
@app.route("/post/delete/<id>/<category_id>")
def delete_post(id, category_id=None):

    db.delete_post(id)

    if category_id:
        return redirect(f"/category/{category_id}")

    return redirect("/posts")

if __name__ == "__main__":
    app.run(debug=True)
