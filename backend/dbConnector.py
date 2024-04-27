import json
from sqlalchemy import create_engine, URL


class DbConnector:
    def __init__(self, params_path='./params.json'):
        self.__params_path = params_path
        self.__conn = None

    def __read_connect_data(self):
        """
        Read data for connecting to DB from file params.json
        :return: None
        """
        try:
            with open('params.json', 'r') as file:
                params_dic = json.loads(file.read())
            return params_dic
        except FileNotFoundError:
            print("File params.json not found.")

    def connecting_to_db(self):
        """
        Connect to the DataBase and return the connection
        :return conn:
        """
        try:
            params_dic = self.__read_connect_data()
            url_obj = URL.create(**params_dic)
            self.__conn = create_engine(url_obj)
        except Exception as error:
            print("Can't connect to DB")
            print(error)
        return self.__conn

    def get_connection(self):
        """
        Get connection to DB
        :return: connection
        """
        return self.__conn
