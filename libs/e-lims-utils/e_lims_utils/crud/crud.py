"""Crud class and the BaseSqlModel class."""
from __future__ import annotations

from typing import TYPE_CHECKING

from sqlmodel import Field, Session, SQLModel, create_engine, select

if TYPE_CHECKING:
    from e_lims_utils.logger.logger import Logger


class BaseSqlModel(SQLModel):
    """Base SQL model with a primary key.

    This class serves as a base for all SQLModel classes in the application.
    It includes a primary key field named 'uid'.

    Attributes:
        uid (int): An integer that represents the primary key. It's the unique identifier for each record in the table.
    """

    __table_args__ = {"extend_existing": True}  # noqa: RUF012
    uid: int = Field(default=None, primary_key=True)


class Crud:
    """A class to perform CRUD operations on a SQLModel.

    This class provides methods to create, read, update, and delete (CRUD) records in a database table.
    It uses SQLAlchemy's Session and Engine to interact with the database.

    Attributes:
        * logger (Logger): The logger used to log messages. It's created from the provided logger class.
        * model (BaseSqlModel): The SQLModel class that represents the table in the database. This is the class that will be used to create, read, update, and delete records.
        * url (str): The URL of the database. This should be a string that SQLAlchemy can recognize as a valid database URL.
        * engine (Engine): The SQLAlchemy Engine used to connect to the database. It's created from the provided database URL.

    Methods:
        * __init__(logger: Logger, model: BaseSqlModel, url: str): Initializes the Crud object with a model and a database URL.
        * create(data: BaseSqlModel): Creates a new record in the database.
        * read(primary_key: int): Reads a record from the database by primary key.
        * update(data: BaseSqlModel): Updates a record in the database.
        * delete(primary_key: int): Deletes a record from the database by primary key.
        * creates(data: list[BaseSqlModel]): Creates multiple new records in the database.
        * reads(): Reads all records from the database.
        * read_by_ids(primary_keys: list[int]): Reads multiple records from the database by their primary keys.
        * read_by_field(field: str, value: str): Reads records from the database by a specific field value.
        * delete_by_ids(ids: list[int]): Deletes multiple records from the database by their primary keys.
        * delete_by_field(field: str, value: str): Deletes records from the database by a specific field value.
    """

    def __init__(self, logger: Logger, model: BaseSqlModel, url: str) -> None:
        """Initializes the Crud object with a model and a database URL.

        This method creates an SQLAlchemy Engine from the provided database URL and assigns it to the 'engine' attribute.
        It also assigns the provided model to the 'model' attribute.

        Args:
            logger (Logger): The logger used to log messages. It's created from the provided logger class.
            model (BaseSqlModel): The SQLModel class that represents the table in the database. This is the class that will be used to create, read, update, and delete records.
            url (str): The URL of the database. This should be a string that SQLAlchemy can recognize as a valid database URL.
        """
        self.logger = logger
        self.model = model
        self.url = url
        self.engine = create_engine(self.url)

    def create_table(self) -> None:
        """Creates a table for the model in the database.

        This method uses the 'metadata.create_all' method of the model class to create a table in the database.
        The table will have columns that correspond to the fields of the model class.
        """
        self.model.metadata.create_all(self.engine)
        self.logger.debug("Create table.")

    def drop_table(self) -> None:
        """Drops the table for the model in the database.

        This method uses the 'metadata.drop_all' method of the model class to drop the table from the database.
        All data in the table will be lost.
        """
        self.model.metadata.drop_all(self.engine)
        self.logger.debug("Drop table.")

    def create(self, data: BaseSqlModel) -> None:
        """Creates a new record in the database.

        This method takes an instance of the model class, adds it to the current session,
        and commits the session to add the record to the database. After committing, it refreshes
        the instance to update any fields that were automatically set by the database, such as auto-incrementing primary keys.

        Args:
            data (BaseSqlModel): An instance of the model class with the data for the new record. This instance will be added to the session and committed to the database.
        """
        with Session(self.engine) as session:
            session.add(data)
            session.commit()
            session.refresh(data)
        self.logger.debug("Create record.")

    def creates(self, data: list[BaseSqlModel]) -> None:
        """Creates multiple new records in the database.

        This method takes a list of instances of the model class, adds each of them to the current session,
        and commits the session to add the records to the database.

        Args:
            data (list[BaseSqlModel]): A list of instances of the model class with the data for the new records.
        """
        with Session(self.engine) as session:
            for record in data:
                session.add(record)
            session.commit()
        self.logger.debug("Create records.")

    def read(self, primary_key: int) -> BaseSqlModel:
        """Reads a record from the database by primary key.

        This method executes a SELECT statement on the table represented by the model class,
        filtering by the primary key. It returns the first result.

        Args:
            primary_key (int): The primary key of the record to read.

        Returns:
            BaseSqlModel: The record read from the database, or None if no record was found.
        """
        with Session(self.engine) as session:
            read = session.exec(select(self.model).where(self.model.uid == primary_key)).first()
            self.logger.debug("Read record.")
            return read

    def reads(self) -> list[BaseSqlModel]:
        """Reads all records from the database.

        This method executes a SELECT statement on the table represented by the model class without any filters.
        It returns all results.

        Returns:
            list[BaseSqlModel]: A list of all records from the database.
        """
        with Session(self.engine) as session:
            reads = session.exec(select(self.model)).all()
            self.logger.debug("Read records.")
            return reads

    def read_by_ids(self, primary_keys: list[int]) -> list[BaseSqlModel]:
        """Reads multiple records from the database by their primary keys.

        This method executes a SELECT statement on the table represented by the model class,
        filtering by the primary keys. It returns all matching results.

        Args:
            primary_keys (list[int]): The primary keys of the records to read.

        Returns:
            list[BaseSqlModel]: A list of the records read from the database.
        """
        with Session(self.engine) as session:
            reads = session.exec(select(self.model).filter(self.model.uid.in_(primary_keys))).all()
            self.logger.debug("Read records by primary_keys.")
            return reads

    def read_by_field(self, field: str, value: str) -> list[BaseSqlModel]:
        """Reads records from the database by a specific field value.

        This method executes a SELECT statement on the table represented by the model class,
        filtering by the value of a specific field. It returns all matching results.

        Args:
            field (str): The field to filter records by.
            value (str): The value to filter records by.

        Returns:
            list[BaseSqlModel]: A list of the records read from the database.
        """
        with Session(self.engine) as session:
            reads = session.exec(select(self.model).filter(getattr(self.model, field) == value)).all()
            self.logger.debug("Records read by field.")
            return reads

    def update(self, data: BaseSqlModel) -> None:
        """Updates a record in the database.

        This method reads a record from the database by its primary key, updates its fields with the data from the provided instance of the model class,
        adds the updated record to the current session, and commits the session to update the record in the database.

        Args:
            data (BaseSqlModel): An instance of the model class with the updated data for the record.
        """
        with Session(self.engine) as session:
            record = self.read(data.uid)
            for field, _ in data:
                if field != "uid":
                    setattr(record, field, getattr(data, field))
            session.add(record)
            session.commit()
            session.refresh(record)
            self.logger.debug("Update record")

    def delete(self, primary_key: int) -> None:
        """Deletes a record from the database by primary key.

        This method reads a record from the database by its primary key, deletes it from the current session, and commits the session to delete the record from the database.

        Args:
            primary_key (int): The primary key of the record to delete.
        """
        with Session(self.engine) as session:
            record = self.read(primary_key)
            session.delete(record)
            session.commit()
            self.logger.debug("Delete record.")

    def delete_by_ids(self, ids: list[int]) -> None:
        """Deletes multiple records from the database by their primary keys.

        This method reads multiple records from the database by their primary keys, deletes them from the current session, and commits the session to delete the records from the database.

        Args:
            ids (list[int]): The primary keys of the records to delete.
        """
        with Session(self.engine) as session:
            records = self.read_by_ids(ids)
            for record in records:
                session.delete(record)
            session.commit()
        self.logger.debug("Delete records by primary_keys.")

    def delete_by_field(self, field: str, value: str) -> None:
        """Deletes records from the database by a specific field value.

        This method reads records from the database by the value of a specific field, deletes them from the current session, and commits the session to delete the records from the database.

        Args:
            field (str): The field to filter records by.
            value (str): The value to filter records by.
        """
        with Session(self.engine) as session:
            records = self.read_by_field(field, value)
            for record in records:
                session.delete(record)
            session.commit()
        self.logger.debug("Delete records by field.")
