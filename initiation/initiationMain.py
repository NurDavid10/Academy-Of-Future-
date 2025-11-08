import sys
import dotenv
import os
dotenv.load_dotenv()
sys.path.append(os.environ["path"])
from databaseManager.database_manager import DatabaseManager
from initiation.insertData import insert_data_from_json
from initiation.tables_structure import tables
# from databaseManager.databaseManager import connect_to_database,initialize_database,create_tables,DATABASE_NAME,tables



# Initializes the database environment:
# - Creates a DatabaseManager instance and initializes the database.
# - Creates necessary tables and populates them with dummy data from a JSON file.
# Handles exceptions to provide error feedback during initialization.
def initiationMain():
    try:
        db_manager = DatabaseManager(to_use_database=False)
        db_manager.initialize_database()
        db_manager.create_tables(tables)
        insert_data_from_json(db_manager,f"{os.environ['path']}\\initiation\\dummy-data.json")

    except Exception as e:
        print(e)    

