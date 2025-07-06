def get_active_users(users):
    return [name for name, info in users.items() if info.get("active")]