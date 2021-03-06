"""Restaurant model to access DB. """

from enum import Enum

from pyframework.models.mysql_model import MySQLModel


class Column(Enum):
    """Columns of table. """

    ID = 'id'
    NAME = 'name'
    URL = 'url'
    ENABLED = 'enabled'
    PRIORITY = 'priority'
    CREATED_AT = 'created_at'
    UPDATED_AT = 'updated_at'


class Endpoint(MySQLModel):
    """Column model to access DB. """

    _columns = [column.value for column in Column]
    """List with all columns of table. """

    _database = 'tourism'

    _table = 'endpoint'

    def __init__(self):
        super(Endpoint, self).__init__()

        self._use_db()

    def get_endpoint(self, id_: int) -> dict:
        """Find the city with restaurant ID equals id_.

        :param id_:
        :return:
        """
        sql = 'SELECT {} FROM {} WHERE {}=%s LIMIT 1'.format(
            ', '.join(self._columns),
            self._table,
            Column.ID.value
        )

        result = self.select_one(sql, [id_])

        return {key: value for key, value in zip(self._columns, result)} if result else {}
