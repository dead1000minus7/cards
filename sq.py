import sqlite3
from getpass import getuser
from os import remove

path = f"/home/{getuser()}/main.sqlite"

try:

    remove(path)

except Exception:

    pass

with sqlite3.connect(path) as con:

    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS Cards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_card STRING,
    description_card STRING,
    class_card STRING,
    type_card STRING,
    rare_card STRING ,
    attack_card INTEGER,
    mana_card INTEGER,
    life_card INTEGER,
    img STRING
    )""")
