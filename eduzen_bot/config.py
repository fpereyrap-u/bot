import os
from pathlib import Path

PATH = os.path.dirname(os.path.abspath(__file__))
DATABASE = "my_database.db"

DB_PATH = Path(os.path.join(PATH, DATABASE))
