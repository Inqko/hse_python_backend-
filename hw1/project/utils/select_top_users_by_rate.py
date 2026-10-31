from models.user import User


def select_top_users_by_rate(
    users: list[User],
    top_size: int,
) -> list[User]:
    ordered_users = sorted(users, key=lambda user: user.rate, reverse=True)
    return ordered_users[:top_size]
