from config.sql_connection import engine
import pandas as pd

def get_everything ():
    query = """SELECT * FROM all_info;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def get_everything_from_character (name):
    query = f"""SELECT * 
    FROM all_info
    WHERE character_name = '{name}';"""

    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def get_just_dialogue (name):
    query = f"""SELECT line 
    FROM all_info
    WHERE character_name = '{name}';"""

    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def get_lines_from_all ():
    query = """SELECT character_name, line
    from all_info
    """
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")



def insert_one_row (season_no, episode_no, episode_name, character_name, line):
    query = f"""INSERT INTO all_info
     (scene, character_name, dialogue) 
        VALUES ({season_no}, {episode_no},'{episode_name}', '{character_name}', '{line}');
    """
    engine.execute(query)
    return f"Correctly introduced!"
