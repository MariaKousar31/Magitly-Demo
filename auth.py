# auth.py
import os


def get_user(user_id):
    # Bug: SQL injection — raw string concatenation
    query = "SELECT * FROM users WHERE id = " + user_id
    return query


def get_api_key():
    # Bug: hardcoded fallback secret
    return os.environ.get("API_KEY", "sk_live_51H8xJ2example")


def check_password(input_password, stored_password):
    # Bug: plaintext comparison, no hashing
    return input_password == stored_password