"""e-lims-utils tests crud."""
from __future__ import annotations

from typing import Generator, Sequence

import pytest
from sqlalchemy import inspect
from sqlmodel import Field

from src.crud.crud import BaseSqlModel, Crud


@pytest.fixture()
def fx_database_url() -> str:
    """Return the database URL.

    Returns:
        str: The database URL.
    """
    return "sqlite:///:memory:"


@pytest.fixture()
def fx_model() -> BaseSqlModel:
    """Return the SQLModel on which to perform CRUD operations.

    Returns:
        Model: The SQLModel on which to perform CRUD operations.
    """

    class Model(BaseSqlModel, table=True):
        """The SQLModel representing a model.

        Attributes:
            uid (int): The unique identifier.
            name (str): The name of the model.
            age (int): The age of the model.
        """

        uid: int = Field(default=None, primary_key=True)
        name: str
        age: int

    return Model


@pytest.fixture()
def fx_crud_instance(
    fx_model: BaseSqlModel,
    fx_database_url: str,
) -> Generator[Crud, None, None]:
    """Return the Crud object.

    Args:
        fx_model (SQLModel): The SQLModel on which to perform CRUD operations.
        fx_database_url (str): The database URL.

    Returns:
        Crud: The Crud object.
    """
    crud = Crud(fx_model, fx_database_url)
    crud.create_table()
    yield crud
    crud.drop_table()


@pytest.fixture()
def fx_data_to_write_and_check(fx_model: BaseSqlModel) -> tuple[Sequence[BaseSqlModel], Sequence[BaseSqlModel]]:
    """Return the data to write and the data to check.

    Args:
        fx_model: tuple[Sequence[BaseSqlModel], Sequence[BaseSqlModel]]: The SQLModel on which to perform CRUD operations.

    Returns:
        Tuple[List[Model], List[Model]]: The data to write and the data to check.
    """
    data_to_write = [fx_model(name="John", age=25), fx_model(name="Jane", age=22)]
    data_to_check = [fx_model(uid=1, name="John", age=25), fx_model(uid=2, name="Jane", age=22)]
    return data_to_write, data_to_check


def test_create_table(fx_crud_instance: Crud) -> None:
    """Test the create_table() method.

    Args:
        fx_crud_instance (Crud): The Crud object.
    """
    fx_crud_instance.create_table()
    assert fx_crud_instance.model.__tablename__ in inspect(fx_crud_instance.engine).get_table_names()  # nosec B101


def test_drop_table(fx_crud_instance: Crud) -> None:
    """Test the drop_table() method.

    Args:
        fx_crud_instance (Crud): The Crud object.
    """
    fx_crud_instance.drop_table()
    assert fx_crud_instance.model.__tablename__ not in inspect(fx_crud_instance.engine).get_table_names()  # nosec B101


def test_create(fx_crud_instance: Crud, fx_data_to_write_and_check: tuple[Sequence[BaseSqlModel], Sequence[BaseSqlModel]]) -> None:
    """Test the create() method.

    Args:
        fx_crud_instance (Crud): The Crud object.
        fx_data_to_write_and_check: tuple[Sequence[BaseSqlModel], Sequence[BaseSqlModel]]: The SQLModel on which to perform CRUD operations.
    """
    data_to_write, _ = fx_data_to_write_and_check
    fx_crud_instance.create(data_to_write[0])
    data_to_check: Sequence[BaseSqlModel] = fx_crud_instance.read(data_to_write[0].uid)
    assert data_to_check.uid == data_to_write[0].uid  # nosec B101
    assert data_to_check.name == data_to_write[0].name  # nosec B101
    assert data_to_check.age == data_to_write[0].age  # nosec B101


def test_read(fx_crud_instance: Crud, fx_data_to_write_and_check: tuple[Sequence[BaseSqlModel], Sequence[BaseSqlModel]]) -> None:
    """Test the read() method.

    Args:
        fx_crud_instance (Crud): The Crud object.
        fx_data_to_write_and_check: tuple[Sequence[BaseSqlModel], Sequence[BaseSqlModel]]: The SQLModel on which to perform CRUD operations.
    """
    data_to_write, data_to_check = fx_data_to_write_and_check
    fx_crud_instance.create(data_to_write[0])
    read_data = fx_crud_instance.read(data_to_check[0].uid)
    assert read_data.uid == data_to_check[0].uid  # nosec B101
    assert read_data.name == data_to_check[0].name  # nosec B101
    assert read_data.age == data_to_check[0].age  # nosec B101


def test_creates(fx_crud_instance: Crud, fx_data_to_write_and_check: tuple[Sequence[BaseSqlModel], Sequence[BaseSqlModel]]) -> None:
    """Test the creates() method.

    Args:
        fx_crud_instance (Crud): The Crud object.
        fx_data_to_write_and_check: tuple[Sequence[BaseSqlModel], Sequence[BaseSqlModel]]: The SQLModel on which to perform CRUD operations.
    """
    data_to_write, _ = fx_data_to_write_and_check
    fx_crud_instance.creates(data_to_write)
    data_to_check = fx_crud_instance.reads()
    assert len(data_to_check) == len(data_to_write)  # nosec B101
    for index, data in enumerate(data_to_check):
        assert data.uid == data_to_check[index].uid  # nosec B101
        assert data.name == data_to_check[index].name  # nosec B101
        assert data.age == data_to_check[index].age  # nosec B101


def test_reads(fx_crud_instance: Crud, fx_data_to_write_and_check: tuple[Sequence[BaseSqlModel], Sequence[BaseSqlModel]]) -> None:
    """Test the reads() method.

    Args:
        fx_crud_instance (Crud): The Crud object.
        fx_data_to_write_and_check: tuple[Sequence[BaseSqlModel], Sequence[BaseSqlModel]]: The SQLModel on which to perform CRUD operations.
    """
    data_to_write, data_to_check = fx_data_to_write_and_check
    fx_crud_instance.creates(data_to_write)
    read_data = fx_crud_instance.reads()
    assert len(read_data) == len(data_to_check)  # nosec B101
    for index, data in enumerate(read_data):
        assert data.uid == data_to_check[index].uid  # nosec B101
        assert data.name == data_to_check[index].name  # nosec B101
        assert data.age == data_to_check[index].age  # nosec B101


def test_read_by_ids(fx_crud_instance: Crud, fx_data_to_write_and_check: tuple[Sequence[BaseSqlModel], Sequence[BaseSqlModel]]) -> None:
    """Test the read_by_ids() method.

    Args:
        fx_crud_instance (Crud): The Crud object.
        fx_data_to_write_and_check: tuple[Sequence[BaseSqlModel], Sequence[BaseSqlModel]]: The SQLModel on which to perform CRUD operations.
    """
    data_to_write, data_to_check = fx_data_to_write_and_check
    fx_crud_instance.creates(data_to_write)
    read_data = fx_crud_instance.read_by_ids([data_to_check[0].uid, data_to_check[1].uid])
    for index, data in enumerate(read_data):
        assert data.uid == data_to_check[index].uid  # nosec B101
        assert data.name == data_to_check[index].name  # nosec B101
        assert data.age == data_to_check[index].age  # nosec B101


def test_read_by_field(fx_crud_instance: Crud, fx_data_to_write_and_check: tuple[Sequence[BaseSqlModel], Sequence[BaseSqlModel]]) -> None:
    """Test the read_by_field() method.

    Args:
        fx_crud_instance (Crud): The Crud object.
        fx_data_to_write_and_check: tuple[Sequence[BaseSqlModel], Sequence[BaseSqlModel]]: The SQLModel on which to perform CRUD operations.
    """
    data_to_write, data_to_check = fx_data_to_write_and_check
    fx_crud_instance.creates(data_to_write)
    read_data = fx_crud_instance.read_by_field("name", "John")
    assert read_data[0].uid == data_to_check[0].uid  # nosec B101
    assert read_data[0].name == data_to_check[0].name  # nosec B101
    assert read_data[0].age == data_to_check[0].age  # nosec B101


def test_update(fx_crud_instance: Crud, fx_data_to_write_and_check: tuple[Sequence[BaseSqlModel], Sequence[BaseSqlModel]]) -> None:
    """Test the update() method.

    Args:
        fx_crud_instance (Crud): The Crud object.
        fx_data_to_write_and_check: tuple[Sequence[BaseSqlModel], Sequence[BaseSqlModel]]: The SQLModel on which to perform CRUD operations.
    """
    updated_age = 26
    data_to_write, data_to_check = fx_data_to_write_and_check
    fx_crud_instance.create(data_to_write[0])
    updated_data = data_to_write[0].model_copy(update={"age": updated_age})
    fx_crud_instance.update(updated_data)
    data_to_check = fx_crud_instance.read(updated_data.uid)
    assert data_to_check.uid == data_to_check[0].uid  # nosec B101
    assert data_to_check.name == data_to_check[0].name  # nosec B101
    assert data_to_check.age == updated_age  # nosec B101


def test_delete_by_ids(fx_crud_instance: Crud, fx_data_to_write_and_check: tuple[Sequence[BaseSqlModel], Sequence[BaseSqlModel]]) -> None:
    """Test the delete_by_ids() method.

    Args:
        fx_crud_instance (Crud): The Crud object.
        fx_data_to_write_and_check: tuple[Sequence[BaseSqlModel], Sequence[BaseSqlModel]]: The SQLModel on which to perform CRUD operations.
    """
    data_to_write, _ = fx_data_to_write_and_check
    fx_crud_instance.creates(data_to_write)
    fx_crud_instance.delete_by_ids([1])
    assert not fx_crud_instance.read_by_ids([1])  # nosec B101


def test_delete_by_field(fx_crud_instance: Crud, fx_data_to_write_and_check: tuple[Sequence[BaseSqlModel], Sequence[BaseSqlModel]]) -> None:
    """Test the delete_by_field() method.

    Args:
        fx_crud_instance (Crud): The Crud object.
        fx_data_to_write_and_check: tuple[Sequence[BaseSqlModel], Sequence[BaseSqlModel]]: The SQLModel on which to perform CRUD operations.
    """
    data_to_write, _ = fx_data_to_write_and_check
    fx_crud_instance.creates(data_to_write)
    fx_crud_instance.delete_by_field("name", "John")
    assert not fx_crud_instance.read_by_field("name", "John")  # nosec B101
