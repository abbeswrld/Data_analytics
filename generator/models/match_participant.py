import random
from dataclasses import dataclass

@dataclass
class MatchParticipant:
    id: int = None
    match_id: int = 0
    user_id: int = 0
    champion_id: int = 0
    team_side: str = ""
    kills: int = 0
    deaths: int = 0
    assists: int = 0
    win: bool = False
    
    @staticmethod
    def generate_one(match_id: int, user_id: int, champion_id: int, 
                    team_side: str, winning_side: str):
        kills = random.randint(0, 25)
        deaths = random.randint(0, 15)
        assists = random.randint(0, 40)
        win = (team_side == winning_side)
        
        return MatchParticipant(
            match_id=match_id,
            user_id=user_id,
            champion_id=champion_id,
            team_side=team_side,
            kills=kills,
            deaths=deaths,
            assists=assists,
            win=win
        )
    
    def to_tuple(self) -> tuple:
        return (
            self.match_id,
            self.user_id,
            self.champion_id,
            self.team_side,
            self.kills,
            self.deaths,
            self.assists,
            self.win
        )