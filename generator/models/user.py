import random
from dataclasses import dataclass
from datetime import datetime

from faker import Faker

fake = Faker()

@dataclass
class User:
    id: int = None
    username: str = ""
    email: str = ""
    password_hash: str = ""
    created_at: datetime = None
    summoner_name: str = ""
    
    @staticmethod
    def generate_one():
        username = fake.unique.user_name()
        email = fake.unique.email()
        summoner_name = f"{fake.first_name()}{random.randint(1, 999)}"
        return User(
            username=username,
            email=email,
            password_hash=f"hash_{random.randint(1000, 9999)}",
            summoner_name=summoner_name, 
            created_at=datetime.now()
        )
    
    def to_tuple(self) -> tuple:
        return (
            self.username,
            self.email,
            self.password_hash,
            self.summoner_name,
            self.created_at
        )