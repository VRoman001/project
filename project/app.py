import json
from flask import Flask, redirect, render_template, request, session, url_for, flash
from functools import wraps
import db
from datetime import datetime

app = Flask(__name__)
app.secret_key = "змінюй-це-на-дуже-довгий-рандомний-рядок-123456789!!!"

# Ініціалізація bcrypt для паролів
db.init_auth(app)

#──────────────────── РОЗУМНИЙ ФІЛЬТР ДАТИ ────────────────────
@app.template_filter('smartdate')
def smartdate_filter(value):
    if not value:
        return ""
    try:
        # SQLite повертає "2025-12-11 15:30:45"
        dt = datetime.strptime(str(value).split('.')[0], "%Y-%m-%d %H:%M:%S")
    except:
        return str(value)[:10]

    now = datetime.now()
    post_date = dt.date()
    today = now.date()

    # Сьогодні — тільки час
    if post_date == today:
        return dt.strftime("%H:%M")

    # Цей рік — ДД.ММ
    if post_date.year == now.year:
        return dt.strftime("%d.%m")

    # Минулі роки — ДД.ММ.РР (дві цифри)
    return dt.strftime("%d.%m.%y")

# Декоратор — тільки для залогінених
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("user_id"):
            flash("Спочатку увійдіть в систему", "warning")
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function

# =========================== АУТЕНТИФІКАЦІЯ ===========================

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password")
        password2 = request.form.get("password2")

        if not username or not password:
            flash("Заповніть усі поля", "danger")
        elif password != password2:
            flash("Паролі не співпадають", "danger")
        elif db.register_user(username, password):
            flash("Реєстрація успішна! Увійдіть", "success")
            return redirect(url_for("login"))
        else:
            flash("Користувач з таким ім'ям вже існує", "danger")
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password")

        if db.verify_user(username, password):
            user_id = db.get_user_id(username)
            user = db.get_user_by_id(user_id)

            session["user_id"] = user_id
            session["username"] = username
            session["is_admin"] = bool(user["is_admin"]) if user else False

            flash(f"Вітаємо, {username}!", "success")
            return redirect(url_for("index"))
        else:
            flash("Невірний логін або пароль", "danger")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    flash("Ви вийшли з системи", "info")
    return redirect(url_for("index"))

# =========================== ГОЛОВНІ СТОРІНКИ ===========================

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/learn")
def learn():
    return render_template("learn.html")

@app.route("/categories_posts")
def categories_posts():
    data = db.get_last_posts_by_category()
    return render_template("categories_posts.html", data=data)

@app.route("/category/add", methods=["POST"])
@login_required
def add_category():
    name = request.form.get("name", "").strip()
    if name:
        db.add_category(name)
        flash("Категорія створена", "success")
    return redirect("/categories_posts")

# =========================== ПОСТИ + КОМЕНТАРІ ===========================

@app.route("/posts", methods=["GET", "POST"])
@login_required
def post_list():
    if request.method == "POST":
        text = request.form.get("text", "").strip()
        category_id = request.form.get("category_id") or None
        if text:
            db.add_post(category_id, text, session["user_id"])
        return redirect("/posts")

    posts = db.get_posts()
    return render_template("posts_lists.html", post_list=_prepare_posts(posts))


@app.route("/category/<int:id>", methods=["GET", "POST"])
@login_required
def category_detail(id):
    if request.method == "POST":
        text = request.form.get("text", "").strip()
        if text:
            db.add_post(id, text, session["user_id"])
        return redirect(f"/category/{id}")

    posts = db.get_posts_by_category(id)
    return render_template(
        "posts_lists.html",
        post_list=_prepare_posts(posts),
        category_page=True,
        category_id=id,
        category=db.get_category(id)
    )

# Допоміжна функція — готує пости + автор + коментарі
def _prepare_posts(posts):
    result = []
    for p in posts:
        user = db.get_user_by_id(p["user_id"]) if p["user_id"] else None
        comments = db.get_comments(p["post_id"])
        result.append({
            "post": p,
            "author": user["username"] if user else "Анонім",
            "is_author": p["user_id"] == session["user_id"],
            "is_admin": session.get("is_admin", False),
            "comments": comments
        })
    return result

# Видалення поста (тільки автор або адмін)
@app.route("/post/delete/<int:post_id>")
@login_required
def delete_post(post_id):
    post = db.get_post(post_id)
    if post and (post["user_id"] == session["user_id"] or session.get("is_admin")):
        db.delete_post(post_id)
        flash("Пост видалено", "success")
    else:
        flash("Немає прав на видалення", "danger")
    return redirect(request.referrer or "/posts")

# Додавання коментаря
@app.route("/comment/add", methods=["POST"])
@login_required
def add_comment():
    post_id = request.form.get("post_id")
    text = request.form.get("text", "").strip()
    if post_id and text:
        db.add_comment(post_id, session["user_id"], text)
    return redirect(request.referrer or "/posts")

# Видалення коментаря (автор або адмін)
@app.route("/comment/delete/<int:comment_id>")
@login_required
def delete_comment(comment_id):
    db.delete_comment(comment_id, session["user_id"])
    return redirect(request.referrer or "/posts")

# =========================== СЛОВНИК ===========================

@app.route("/slovnyk")
def slovnyk():
    categories = db.get_slovnyk_categories()
    return render_template("slovnyk_categories.html", categories=categories)

@app.route("/slovnyk/category/<category>")
def slovnyk_category(category):
    entries = db.get_slovnyk_by_category(category)
    return render_template("slovnyk_by_category.html", category=category, entries=entries)

# =========================== ІНТЕРАКТИВНЕ НАВЧАННЯ ===========================

# Додаємо функції в Jinja, щоб шаблон їх бачив
app.jinja_env.globals.update({
    'get_solved_task_ids': db.get_solved_task_ids,
    'get_max_unlocked_task_id': db.get_max_unlocked_task_id
})

@app.route("/tasks")
@login_required
def tasks_list():
    all_tasks = db.get_all_tasks()
    solved_ids = set(db.get_solved_task_ids(session["user_id"]))
    max_unlocked = db.get_max_unlocked_task_id(session["user_id"])

    return render_template("tasks_list.html",
                         tasks=all_tasks,
                         solved_ids=solved_ids,
                         max_unlocked=max_unlocked)

@app.route("/task/<int:tid>", methods=["GET", "POST"])
@login_required
def task_detail(tid):
    task = db.get_task(tid)
    if not task:
        flash("Завдання не знайдено", "danger")
        return redirect("/tasks")

    # Перевіряємо, чи розблоковано це завдання
    if tid > db.get_max_unlocked_task_id(session["user_id"]):
        flash("Це завдання ще не відкрито! Пройдіть попереднє.", "warning")
        return redirect("/tasks")

    code = task["starter_code"]
    result = None
    errors = []

    if request.method == "POST":
        code = request.form.get("code", "")

        try:
            local_env = {}
            exec(code, {}, local_env)

            # Авто-пошук функції (solution / fib / factorial тощо)
            func = None
            possible_names = ["solution", "fib", "max_of_three", "factorial", "is_palindrome", "sum_two"]
            for name in possible_names:
                if name in local_env:
                    func = local_env[name]
                    break

            if not func:
                result = "Не знайдено потрібну функцію в коді"
            else:
                tests = json.loads(task["test_cases"])
                passed = 0
                total = len(tests)

                for i, test in enumerate(tests, 1):
                    args = test["input"] if isinstance(test["input"], list) else [test["input"]]
                    expected = test["output"]
                    try:
                        got = func(*args)
                        if got == expected:
                            passed += 1
                        else:
                            errors.append(f"Тест {i}: очікувалось {expected}, отримано {got}")
                    except Exception as e:
                        errors.append(f"Тест {i}: помилка — {e}")

                if passed == total:
                    result = "Відмінно! Завдання успішно пройдено!"
                    db.save_solution(session["user_id"], tid, True)
                else:
                    result = f"Пройдено {passed} з {total} тестів"
                    db.save_solution(session["user_id"], tid, False)

        except Exception as e:
            result = f"Помилка у коді: {e}"

    return render_template("task_detail.html",
                         task=task,
                         code=code,
                         result=result,
                         errors=errors)

# =========================== УРОКИ ===========================

# Додаємо в Jinja
app.jinja_env.globals.update({
    'get_read_lessons': db.get_read_lessons,
    'get_next_lesson_id': db.get_next_lesson_id
})

@app.route("/lessons")
def lessons_list():
    lessons = db.get_all_lessons()
    read_lessons = db.get_read_lessons(session.get("user_id"))
    return render_template("lessons_list.html", lessons=lessons, read_lessons=read_lessons)

@app.route("/lesson/<int:lid>", methods=["GET", "POST"])
@login_required
def lesson_detail(lid):
    lesson = db.get_lesson(lid)
    if not lesson:
        flash("Урок не знайдено", "danger")
        return redirect("/lessons")

    # Зберігаємо, що користувач відкрив урок
    db.mark_lesson_read(session["user_id"], lid)

    next_lesson = db.get_next_lesson_id(lid)

    return render_template("lesson_detail.html",
                         lesson=lesson,
                         next_lesson=next_lesson)

# =========================== ЗАПУСК ===========================

if __name__ == "__main__":
    app.run(debug=True)