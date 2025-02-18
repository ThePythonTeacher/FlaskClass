
from abc import ABC, abstractmethod


class DB(ABC):
    @abstractmethod
    def connect_db(self):
        pass


class ConnectMySQL(DB):
    def connect_db(self):
        self.user_name = "bala"
        self.password = "Admin@123"


call_cls = ConnectMySQL()
call_cls.connect_db()
