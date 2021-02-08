#! /usr/bin/python3

import sqlite3

out = []
from question import Question

# db_prompt= []
# db_options=[]
# db_answers=[]
# db_topic_name=[]
# db_difficulty_level=[]
# def extend():
#     db_prompt.extend(Question.prompt)
#     db_options.extend(Question.options)
#     db_answers.extend(Question.answers)
#     db_topic_name.extend(Question.topic_name)
#     db_difficulty_level.extend(Question.difficulty_level)

# c.execute("""CREATE TABLE Question(
#     question text,
#     options text,
#     answer text,
#     topic text,
#     d_level text
#     ) """)
# conn = sqlite3.connect("quiz.db")
# c = conn.cursor()
# c.execute("DELETE FROM Question")
# conn.commit()
# conn.close()

def execute():
    conn = sqlite3.connect("quiz.db")
    c = conn.cursor()
    c.execute("INSERT INTO Question VALUES(?,?,?,?,?)", (str(Question.prompt),str(Question.options),str(Question.answers),str(Question.topic_name),str(Question.difficulty_level)))
    
    # c.execute("SELECT * FROM Question")
    # print(c.fetchall())
    conn.commit()
    conn.close()
def fetch():
    conn = sqlite3.connect("quiz.db")
    c = conn.cursor()
    out = c.execute("SELECT * FROM Question").fetchall()
    conn.commit()
    conn.close()
    return out

