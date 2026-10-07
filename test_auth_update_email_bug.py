from test4 import UserRepository, TokenService, AuthService, UserService, User

def test_update_email_duplicate():
    repo = UserRepository()
    tokens = TokenService()
    auth = AuthService(repo, tokens)
    users = UserService(repo)
    u1 = auth.register("Alice", "alice@example.com", "Password123")
    u2 = auth.register(
        "Bob", "bob@example.com", "Password123"
    )
    try:
        users.update_email(u2.id, "alice@example.com")
        assert False, "Expected ValueError for duplicate email"
    except ValueError as e:
        assert str(e) == "Email already registered"
