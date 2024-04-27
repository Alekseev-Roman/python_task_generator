import click
import pandas as pd
from click import Context, HelpFormatter
from typing import Optional

from dbConnector import DbConnector


class DynamicHelp(click.Command):
    def __init__(self, name: Optional[str], callback='', params='', help=''):
        super().__init__(name=name, callback=callback, params=params, help=help)
        self._name = name
        self._help = help
        self._callback = callback
        self._params = params

        self._topics_dict = None
        self._types_dict = None
        self._topics_list = []
        self._types_list = []

        self.__connector = DbConnector(params)
        self.__conn = DbConnector().connecting_to_db()

        self._max_len = 0

        self.get_max_len()
        self.get_data()

    def get_max_len(self):
        for param in self._params:
            if len("".join(param.opts)) > self._max_len:
                self._max_len = len("".join(param.opts)) + 2
            if len(str(param.type)) > self._max_len:
                self._max_len = len(str(param.type)) + 2

    def get_data(self):
        self._types_dict = pd.read_sql(
            f"SELECT * "
            f"FROM type;",
            self.__conn
        ).to_dict()
        for i in range(len(self._types_dict['type_id'])):
            self._types_list.append(f"{self._types_dict['type_id'][i]} - {self._types_dict['type_name'][i]}")

        self._topics_dict = pd.read_sql(
            f"SELECT * "
            f"FROM topic;",
            self.__conn
        ).to_dict()
        for i in range(len(self._topics_dict['topic_id'])):
            self._topics_list.append(f"{self._topics_dict['topic_id'][i]} - {self._topics_dict['topic_name'][i]}")

    def format_help(self, ctx: Context, formatter: HelpFormatter):
        echo_str = f'Usage: {self._name}\n' \
                   f'{self._help}\n' \
                   f'Options: \n' \

        echo_str += ''.join(
            el.ljust(self._max_len)
            for el in [
                f'{"  ".join(self._params[0].opts)}',
                str(self._params[0].type),
                f'{self._params[0].help}'
            ]
        ) + '\n'
        for topic in self._topics_list:
            echo_str += ''.join(el.ljust(self._max_len) for el in ['', '', topic]) + '\n'
        echo_str += '\n'

        echo_str += ''.join(
            el.ljust(self._max_len)
            for el in [
                f'{"  ".join(self._params[1].opts)}',
                str(self._params[1].type),
                f'{self._params[1].help}'
            ]
        ) + '\n'
        for type in self._types_list:
            echo_str += ''.join(el.ljust(self._max_len) for el in ['', '', type]) + '\n'
        echo_str += '\n'

        echo_str += ''.join(
            el.ljust(self._max_len)
            for el in [
                f'{"  ".join(self._params[2].opts)}',
                str(self._params[2].type),
                f'{self._params[2].help}'
            ]
        ) + '\n\n'
        echo_str += ''.join(
            el.ljust(self._max_len) for el in [
                f'{"  ".join(self._params[3].opts)}',
                str(self._params[3].type),
                f'{self._params[3].help}'
            ]
        )

        click.echo(echo_str)
