"""e-lims-utils crud tests."""
from __future__ import annotations

from crud import Crud
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import Field, SQLModel


# Define a test model
class TestModel(SQLModel, table=True):
    """A test model."""

    id: int | None = Field(default=None, primary_key=True)
    name: str


# Create a test database
engine = create_engine("sqlite:///:memory:")
SQLModel.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)

# Initialize the Crud class
crud = Crud(TestModel)


def test_create() -> None:
    """Test the create method of the Crud class.

    This test creates a new record and asserts that the ID is not None and the name is "Test".
    """
    # Create a new session
    with SessionLocal() as session:
        # Create a new record
        data = {"name": "Test"}
        record = crud.create(session, data)
        assert record.id is not None
        assert record.name == "Test"


def test_read() -> None:
    """Test the read method of the Crud class.

    This test reads a record with ID 1 and asserts that the ID is 1 and the name is "Test".
    """
    # Create a new session
    with SessionLocal() as session:
        # Read the record
        record = crud.read(session, 1)
        assert record.id == 1
        assert record.name == "Test"


def test_update() -> None:
    """Test the update method of the Crud class.

    This test updates a record with ID 1 and asserts that the ID is 1 and the name is "Updated Test".
    """
    # Create a new session
    with SessionLocal() as session:
        # Update the record
        data = {"name": "Updated Test"}
        record = crud.update(session, 1, data)
        assert record.id == 1
        assert record.name == "Updated Test"


def test_delete() -> None:
    """Test the delete method of the Crud class.

    This test deletes a record with ID 1 and asserts that the record is None.
    """
    # Create a new session
    with SessionLocal() as session:
        # Delete the record
        crud.delete(session, 1)
        record = crud.read(session, 1)
        assert record is None
