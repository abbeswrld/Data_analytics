CREATE DATABASE redash_metadata; 

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    summoner_name VARCHAR(50) UNIQUE
);

CREATE TABLE champions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE matches (
    id SERIAL PRIMARY KEY,
    duration INTEGER NOT NULL, 
    winning_side VARCHAR(10) NOT NULL CHECK (winning_side IN ('Blue', 'Red')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE match_participants (
    id SERIAL PRIMARY KEY,
    match_id INTEGER NOT NULL REFERENCES matches(id) ON DELETE CASCADE,
    user_id INTEGER REFERENCES users(id) ON DELETE SET NULL,
    champion_id INTEGER NOT NULL REFERENCES champions(id),
    team_side VARCHAR(10) NOT NULL CHECK (team_side IN ('Blue', 'Red')),
    
    kills INTEGER DEFAULT 0,
    deaths INTEGER DEFAULT 0,
    assists INTEGER DEFAULT 0,
    
    win BOOLEAN NOT NULL
);