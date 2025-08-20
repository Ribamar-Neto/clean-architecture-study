from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler:

	def __init__(self) -> None:
		self.__connection_string = (
				"mysql+pymysql://{user}:{password}@{host}:{port}/{db}"
			).format(
				user="appuser",
				password="minhasenha",
				host="localhost",
				port="3306",
				db="clean_database"
			)
		self.__engine = self.__create_database_engine()
		self.session = None

	def __create_database_engine(self):
		engine = create_engine(self.__connection_string)
		return engine

	def get_engine(self):
		return self.__engine

	def __enter__(self):
		session = sessionmaker(bind=self.get_engine())
		self.session = session()
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.session.close()

	def get_session(self):
		return self.session
