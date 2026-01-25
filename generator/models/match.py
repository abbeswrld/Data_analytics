import random
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class Match:
    id: int = None
    duration: int = 0
    winning_side: str = ""
    created_at: datetime = None
    
    @staticmethod
    def generate_one():
        duration = random.randint(900, 2700)
        winning_side = random.choice(['Blue', 'Red'])
        
        days_ago = random.randint(0, 365)
        created_at = datetime.now() - timedelta(days=days_ago)
        
        return Match(
            duration=duration,
            winning_side=winning_side,
            created_at=created_at
        )
    
    def to_tuple(self) -> tuple:
        return (
            self.duration,
            self.winning_side,
            self.created_at
        )