"""e-lims-utils crud."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sqlmodel import SQLModel


class Crud:
    """A class used to perform CRUD operations on a SQLModel.

    ...

    Methods:
        create(data: SQLModel) -> SQLModel:
            Creates a new record in the database.
        read(primary_key: int) -> SQLModel:
            Reads a record by its primary key.
        reads() -> list[SQLModel]:
            Reads all records.
        read_by_ids(ids: list[int]) -> list[SQLModel]:
            Reads records by their IDs.
        read_by_field(field: str, value: str) -> list[SQLModel]:
            Reads records by a specific field and value.
        update(data: SQLModel) -> SQLModel:
            Updates a record.
        delete(primary_key: int) -> SQLModel:
            Deletes a record by its primary key.
    """

    def __init__(self, model: SQLModel, url: str) -> None:
        """Constructs all the necessary attributes for the Crud object.

        Args:
            model (SQLModel): The SQLModel on which to perform CRUD operations.
            url (str): The database URL.
        """

    def create(self, data: SQLModel) -> SQLModel:
        """Creates a new record in the database.

        Args:
            data (SQLModel): The data to create a new record.

        Returns:
            SQLModel: The created record.
        """

    def read(self, primary_key: int) -> SQLModel:
        """Reads a record by its primary key.

        Args:
            primary_key (int): The primary key of the record to read.

        Returns:
            SQLModel: The read record.
        """

    def reads(self) -> list[SQLModel]:
        """Reads all records.

        Returns:
            list[SQLModel]: The list of all records.
        """

    def read_by_ids(self, ids: list[int]) -> list[SQLModel]:
        """Reads records by their IDs.

        Args:
            ids (list[int]): The list of IDs of the records to read.

        Returns:
            list[SQLModel]: The list of read records.
        """

    def read_by_field(self, field: str, value: str) -> list[SQLModel]:
        """Reads records by a specific field and value.

        Args:
            field (str): The field to filter by.
            value (str): The value of the field to filter by.

        Returns:
            list[SQLModel]: The list of read records.
        """

    def update(self, data: SQLModel) -> SQLModel:
        """Updates a record.

        Args:
            data (SQLModel): The data to update the record with.

        Returns:
            SQLModel: The updated record.
        """

    def delete(self, primary_key: int) -> SQLModel:
        """Deletes a record by its primary key.

        Args:
            primary_key (int): The primary key of the record to delete.

        Returns:
            SQLModel: The deleted record.
        """
