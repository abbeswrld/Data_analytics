import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DB_HOST = os.getenv('POSTGRES_HOST', 'localhost')
    DB_PORT = os.getenv('POSTGRES_PORT', '5432')
    DB_NAME = os.getenv('POSTGRES_DB', 'db_name')
    DB_USER = os.getenv('POSTGRES_USER', 'postgres')
    DB_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'password')
    
    CHAMPIONS = [
        'Aatrox', 'Ahri', 'Akali', 'Alistar', 'Amumu',
        'Anivia', 'Annie', 'Aphelios', 'Ashe', 'Aurelion Sol',
        'Azir', 'Bard', 'Blitzcrank', 'Brand', 'Braum',
        'Caitlyn', 'Camille', 'Cassiopeia', 'Cho Gath', 'Corki',
        'Darius', 'Diana', 'Draven', 'Dr. Mundo', 'Ekko',
        'Elise', 'Evelynn', 'Ezreal', 'Fiddlesticks', 'Fiora',
        'Fizz', 'Galio', 'Gangplank', 'Garen', 'Gnar',
        'Gragas', 'Graves', 'Gwen', 'Hecarim', 'Heimerdinger',
        'Illaoi', 'Irelia', 'Ivern', 'Janna', 'Jarvan IV',
        'Jax', 'Jayce', 'Jhin', 'Jinx', 'Kai\'Sa'
    ]
    
    DELAY = .5
    
config = Config()