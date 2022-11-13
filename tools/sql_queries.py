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
    from all_info;
    """
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def get_lines_from_char ():
    query = """SELECT character_name, line
    from all_info;
    """
    df = pd.read_sql_query(query, engine)
    list_all_lines = df.to_dict(orient="records")
    
    lines_dict={}
    for line in list_all_lines:
        char = line["character_name"]
        diu = line["line"]
        if char not in lines_dict:
            list_lines=[]
            list_lines.append(diu)
            lines_dict[char]=list_lines
        else:
            lines_dict[char].append(diu)
    return lines_dict

'''def return_episodes_and_seasons(): -- # NO FUNCIONA COM VULL
    query = """SELECT season_no, episode_no, DISTINCT(episode_name)
    from all_info
    """
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")'''

def insert_one_row (season_no, episode_no, episode_name, character_name, line):
    query = f"""INSERT INTO all_info
     (scene, character_name, dialogue) 
        VALUES ({season_no}, {episode_no},'{episode_name}', '{character_name}', '{line}');
    """
    engine.execute(query)
    return f"Correctly introduced!"
