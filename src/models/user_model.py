class User:
    
    def __init__(self, id: int = None, login: str = "", password: str = ""):
        self.id = id
        self.login = login
        self.password = password

    def to_dict(self):
        return {
            "id": self.id,
            "login": self.login,
            "password": self.password
        }

    @staticmethod
    def from_dict(data: dict):
        return User(
            id=data.get("id"),
            login=data.get("login"),
            password=data.get("password")
        )