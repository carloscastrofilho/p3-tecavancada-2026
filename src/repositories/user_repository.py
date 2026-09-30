from src.databases.connection import Database
from src.models.user_model import User
from typing import List, Optional

class UserRepository:
    def __init__(self):
        self.db = Database()

    def get_all(self) -> List[User]:
        with self.db.get_connection() as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM users")
            rows = cursor.fetchall()
            cursor.close()
            return [User.from_dict(row) for row in rows]

    def get_by_id(self, id_User: int) -> Optional[User]:
        with self.db.get_connection() as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM users WHERE id = %s", (id_User,))
            row = cursor.fetchone()
            cursor.close()
            return User.from_dict(row) if row else None
        
    def get_by_Login(self, login: str) -> Optional[User]:
        with self.db.get_connection() as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM users WHERE login = %s", (login,))
            row = cursor.fetchone()
            cursor.close()
            return User.from_dict(row) if row else None

    def create(self, user: User) -> int:
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            query = "INSERT INTO users ( login, password ) VALUES (%s, %s)"
            cursor.execute(query, (user.login, user.password))
            conn.commit()
            new_id = cursor.lastrowid
            cursor.close()
            return new_id

    def update(self, id_User: int, user: User) -> bool:
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            query = "UPDATE users SET login = %s, password = %s WHERE id = %s"
            cursor.execute(query, (user.login, user.password, id_User))
            conn.commit()
            affected = cursor.rowcount
            cursor.close()
            return affected > 0

    def delete(self, id_User: int) -> bool:
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM users WHERE id = %s", (id_User,))
            conn.commit()
            affected = cursor.rowcount
            cursor.close()
            return affected > 0