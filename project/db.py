import sqlite3
import os

DB_NAME = "blog.db"
DB_PATH = os.path.join(os.path.dirname(__file__), DB_NAME)

def _get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # за бажанням: доступ по іменах полів
    return conn

def get_categories():
    with _get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM category")
        return cur.fetchall()

def get_posts():
    with _get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM post ORDER BY date DESC")
        return cur.fetchall()

def get_posts_by_category(category_id):
    with _get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM post WHERE category_id = ? ORDER BY datetime DESC", (category_id,))
        return cur.fetchall()

def get_post(post_id):
    with _get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM post WHERE post_id = ?", (post_id,))
        return cur.fetchone()

def get_category(category_id):
    with _get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM category WHERE category_id = ?", (category_id,))
        return cur.fetchone()

def add_post(category_id, text):
    with _get_connection() as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO post (category_id, text) VALUES (?, ?)", (category_id, text))
        conn.commit()
        return cur.lastrowid
    
def add_category(name):
    with _get_connection() as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO category (category_name) VALUES (?)", (name,))
        conn.commit()


def delete_post(post_id):
    with _get_connection() as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM post WHERE post_id = ?", (post_id,))
        conn.commit()
        return cur.rowcount

def get_last_posts_by_category(limit=3):
    with _get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM category")
        categories = cur.fetchall()

        result = []
        for cat in categories:
            # prefer named access provided by sqlite3.Row, fall back to index
            try:
                cat_id = cat["category_id"]
            except Exception:
                cat_id = cat[0]
            cur.execute(
                "SELECT * FROM post WHERE category_id = ? ORDER BY post_id DESC LIMIT ?",
                (cat_id, limit)
            )
            posts = cur.fetchall()
            result.append((cat, posts))  # кортеж: (категорія, список постів)
        return result

def get_data():
    with _get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT slovnyk_photo, slovnyk_text FROM slovnyk")
        data = cur.fetchall()
        return data
    
def get_slovnyk_categories():
    with _get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT slovnyk_category, COUNT(*) as count 
            FROM slovnyk
            GROUP BY slovnyk_category
            ORDER BY slovnyk_category
        """)
        return cur.fetchall()


def get_slovnyk_by_category(category):
    with _get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT * FROM slovnyk
            WHERE slovnyk_category = ?
            ORDER BY slovnyk_id DESC
        """, (category,))
        return cur.fetchall()
    
# ------------------- АУТЕНТИФІКАЦІЯ -------------------
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def init_auth(app):
    bcrypt.init_app(app)

# Реєстрація нового користувача
def register_user(username: str, password: str):
    hashed = bcrypt.generate_password_hash(password).decode('utf-8')
    try:
        with _get_connection() as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed))
            conn.commit()
            return True
    except sqlite3.IntegrityError:
        return False  # користувач вже існує

# Перевірка логіна
def verify_user(username: str, password: str):
    with _get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT password FROM users WHERE username = ?", (username,))
        row = cur.fetchone()
        if row and bcrypt.check_password_hash(row[0], password):
            return True
        return False

# Отримання ID користувача (для сесії)
def get_user_id(username: str):
    with _get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT id FROM users WHERE username = ?", (username,))
        row = cur.fetchone()
        return row[0] if row else None

# НОВІ ФУНКЦІЇ

def add_post(category_id, text, user_id):
    with _get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO post (category_id, text, user_id) VALUES (?, ?, ?)",
            (category_id, text, user_id)
        )
        conn.commit()
        return cur.lastrowid

def get_comments(post_id):
    with _get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT c.*, u.username 
            FROM comment c 
            JOIN users u ON c.user_id = u.id 
            WHERE post_id = ? 
            ORDER BY date
        """, (post_id,))
        return cur.fetchall()

def add_comment(post_id, user_id, text):
    with _get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO comment (post_id, user_id, text) VALUES (?, ?, ?)",
            (post_id, user_id, text)
        )
        conn.commit()

def delete_comment(comment_id, user_id):
    with _get_connection() as conn:
        cur = conn.cursor()
        # Адмін може все, звичайний користувач — тільки свої
        cur.execute("""
            DELETE FROM comment 
            WHERE id = ? AND (user_id = ? OR EXISTS (SELECT 1 FROM users WHERE id = ? AND is_admin = 1))
        """, (comment_id, user_id, user_id))
        conn.commit()

def get_user_by_id(user_id):
    with _get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT username, is_admin FROM users WHERE id = ?", (user_id,))
        return cur.fetchone()

def make_admin(user_id):
    with _get_connection() as conn:
        conn.execute("UPDATE users SET is_admin = 1 WHERE id = ?", (user_id,))
        conn.commit()


# === ІНТЕРАКТИВНІ ЗАВДАННЯ З ЛІНІЙНИМ РОЗБЛОКУВАННЯМ ===

def get_all_tasks():
    with _get_connection() as conn:
        return conn.execute("SELECT * FROM tasks ORDER BY id").fetchall()

def get_task(task_id):
    with _get_connection() as conn:
        return conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()

def save_solution(user_id, task_id, passed):
    """Зберігає результат (passed = 1 або 0)"""
    with _get_connection() as conn:
        conn.execute("""
            INSERT INTO user_solutions (user_id, task_id, passed, solved_at)
            VALUES (?, ?, ?, CURRENT_TIMESTAMP)
            ON CONFLICT(user_id, task_id) DO UPDATE SET
                passed = excluded.passed,
                solved_at = CURRENT_TIMESTAMP
        """, (user_id, task_id, 1 if passed else 0))
        conn.commit()

def get_solved_task_ids(user_id):
    """Повертає список ID успішно пройдених завдань (відсортованих)"""
    with _get_connection() as conn:
        rows = conn.execute("""
            SELECT task_id FROM user_solutions
            WHERE user_id = ? AND passed = 1
            ORDER BY task_id
        """, (user_id,)).fetchall()
        return [row["task_id"] for row in rows]

def get_max_unlocked_task_id(user_id):
    """Повертає ID останнього доступного завдання (пройдені + наступне)"""
    solved = get_solved_task_ids(user_id)
    if not solved:
        # Якщо нічого не пройдено — відкриваємо перше завдання
        first = _get_connection().execute("SELECT id FROM tasks ORDER BY id LIMIT 1").fetchone()
        return first["id"] if first else None
    
    # Відкриваємо всі пройдені + наступне після останнього
    last_solved = max(solved)
    next_task = _get_connection().execute("SELECT id FROM tasks WHERE id > ? ORDER BY id LIMIT 1", (last_solved,)).fetchone()
    return (next_task["id"] if next_task else last_solved)

# === УРОКИ ===
def get_all_lessons():
    with _get_connection() as conn:
        return conn.execute("SELECT * FROM lessons ORDER BY id").fetchall()

def get_lesson(lesson_id):
    with _get_connection() as conn:
        return conn.execute("SELECT * FROM lessons WHERE id = ?", (lesson_id,)).fetchone()

def get_next_lesson_id(current_id):
    with _get_connection() as conn:
        row = conn.execute("SELECT id FROM lessons WHERE id > ? ORDER BY id LIMIT 1", (current_id,)).fetchone()
        return row["id"] if row else None

def mark_lesson_read(user_id, lesson_id):
    if not user_id:
        return
    with _get_connection() as conn:
        conn.execute("""
            INSERT INTO user_lessons (user_id, lesson_id, read_at)
            VALUES (?, ?, CURRENT_TIMESTAMP)
            ON CONFLICT(user_id, lesson_id) DO UPDATE SET read_at = CURRENT_TIMESTAMP
        """, (user_id, lesson_id))
        conn.commit()

def get_read_lessons(user_id):
    if not user_id:
        return set()
    with _get_connection() as conn:
        rows = conn.execute("SELECT lesson_id FROM user_lessons WHERE user_id = ?", (user_id,)).fetchall()
        return {row["lesson_id"] for row in rows}