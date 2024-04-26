from commands.command import Command
from state.global_state import GlobalState
from errors import TooManyArguments, TooFewArguments, BadCommandUse, SqlInjection


class ImportCommand(Command):
    """
    imports a csv file into a database table
    >> import <csv_path> <database_path> (<table_name>)
    (table_name is optional, if not provided, the csv file name is used as table name)

    or creates a new db with the csv file as table
    >> import <csv_path>
    """

    csv_path: str
    database_path: str
    table_name: str

    def __init__(self, args: list[str]):
        if len(args) < 1:
            raise TooFewArguments("import <database_path> <csv_path>")
        if len(args) > 3:
            raise TooManyArguments("import <database_path> <csv_path>")
        
        if len(args) == 1:
            self.csv_path = args[0]
            self.database_path = args[0].replace('.csv', '.sqlite3')
            self.table_name = args[0].replace('.csv', '')
        elif len(args) == 2:
            self.csv_path = args[0]
            self.database_path = args[1]
            self.table_name = args[0].replace('.csv', '')
        elif len(args) == 3:
            self.csv_path = args[0]
            self.database_path = args[1]
            self.table_name = args[2]

        # check for sql injection
        if self.table_name != self.table_name.replace('\'', '') or self.table_name != self.table_name.replace('\"', ''):
            raise SqlInjection("Table name cannot contain single or double quotes")

    def execute(self):
        csv = None
        try:
            csv = open(self.csv_path, 'r')
        except FileNotFoundError:
            raise BadCommandUse(f"File {self.csv_path} not found")
        
        if not GlobalState.in_db_mode():
            GlobalState.enter_db_mode(self.database_path)

        self.__table_exists_check()
        GlobalState.cursor.execute(f"CREATE TABLE {self.table_name} (id INTEGER PRIMARY KEY)")

        # read csv file and create table
        columns = csv.readline().strip().split(',')
        print("creating columns: ", columns)
        for column in columns:
            GlobalState.cursor.execute(f"ALTER TABLE {self.table_name} ADD COLUMN {column} TEXT")
        
        # insert data into table
        for id, line in enumerate(csv):
            values = line.strip().split(',')
            GlobalState.cursor.execute(f"INSERT INTO {self.table_name} VALUES ({id}, {', '.join(['?']*len(values))})", values)
            # placeholders are used to prevent sql injection
        
        GlobalState.connection.commit()
        csv.close()

    
    def __table_exists_check(self):
        
        # check if table already exists
        GlobalState.cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{self.table_name}'")
        table = GlobalState.cursor.fetchone()
        if table:
            raise BadCommandUse(f"Table {self.table_name} already exists in database {self.database_path}")