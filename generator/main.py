import random
from psycopg2.extras import execute_batch

from database import Database
from models.user import User
from models.champion import Champion
from models.match import Match
from models.match_participant import MatchParticipant
from utils.logging import setup_logging
from config import config
from time import sleep

logger = setup_logging()

def generate_user(db: Database):
    user = User.generate_one()
    
    db.cursor.execute(
        "INSERT INTO users (username, email, password_hash, summoner_name, created_at) VALUES (%s, %s, %s, %s, %s)",
        user.to_tuple()
    )
    
    db.connection.commit()
    logger.info(f"Сгенерирован пользователь {user.username}")

def generate_champions(db: Database):
    db.cursor.execute("SELECT COUNT(*) FROM champions")
    if db.cursor.fetchone()[0] > 0:
        logger.info("Чемпионы уже есть")
        return
    
    champions_data = []
    for name in config.CHAMPIONS:
        champion = Champion.generate_one(name)
        champions_data.append(champion.to_tuple())
    
    execute_batch(
        db.cursor,
        "INSERT INTO champions (name) VALUES (%s)",
        champions_data
    )
    
    db.connection.commit()
    logger.info(f"Сгенерировано {len(config.CHAMPIONS)} чемпионов")

def generate_match(db: Database):
    match = Match.generate_one()
    
    db.cursor.execute(
        "INSERT INTO matches (duration, winning_side, created_at) VALUES (%s, %s, %s) RETURNING id",
        match.to_tuple()
    )
    match_id = db.cursor.fetchone()[0]
    
    db.connection.commit()
    logger.info(f"Сгенерирован матч")
    return match_id

def generate_participants(db: Database, match_id):
    db.cursor.execute("SELECT id FROM users")
    user_ids = [row[0] for row in db.cursor.fetchall()]
    
    db.cursor.execute("SELECT id FROM champions")
    champion_ids = [row[0] for row in db.cursor.fetchall()]
    
    participants_data = []
    
    db.cursor.execute("SELECT winning_side FROM matches WHERE id = %s", (match_id,))
    winning_side = db.cursor.fetchone()[0]
    
    match_users = random.sample(user_ids, 10)
    
    for i in range(10):
        user_id = match_users[i]
        champion_id = random.choice(champion_ids)
        team_side = 'Blue' if i < 5 else 'Red'
        
        participant = MatchParticipant.generate_one(
            match_id=match_id,
            user_id=user_id,
            champion_id=champion_id,
            team_side=team_side,
            winning_side=winning_side
        )
        
        participants_data.append(participant.to_tuple())

    execute_batch(
        db.cursor,
        """INSERT INTO match_participants 
            (match_id, user_id, champion_id, team_side, kills, deaths, assists, win) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
        participants_data
    )
    
    db.connection.commit()
    logger.info(f"Сгенерировано {len(participants_data)} участников матчей")


logger.info("Запуск генератора данных...")

db = Database()
db.connect()
generate_champions(db)
# for i in range(100): 
#     generate_user(db)
try:
    i = 0
    
    while True:        
        match_id = generate_match(db)
        generate_participants(db, match_id)
        if i % 5 == 0: 
            generate_user(db)
        i += 1
        sleep(config.DELAY)
except Exception as e:
    logger.info(f"Ошибка: {e}")
    db.connection.rollback()
finally:
    db.close()