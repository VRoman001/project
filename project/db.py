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
