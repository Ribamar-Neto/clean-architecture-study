from sqlalchemy import create_engine

class DBConnectionHandler:

	def __init__(self) -> None:
		self.__connection_string = "mysql+pymysql://{}:{}@{}:{}".format(
			"root",
			"root",
			"localhost",
			"3306"
		)
		self.engine = self.create_database_engine()

	def create_database_engine(self):
		engine = create_engine(self.__connection_string)
		return engine

	def get_engine(self):
		return self.engine
