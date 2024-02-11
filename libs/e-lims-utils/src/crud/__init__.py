"""This module contains the Crud class and the BaseSqlModel class.

The Crud class provides methods to create, read, update, and delete (CRUD) records in a database table.
It uses SQLAlchemy's Session and Engine to interact with the database.

The BaseSqlModel class serves as a base for all SQLModel classes in the application.
It includes a primary key field named 'uid'.

Classes:
    BaseSqlModel: A base class for all SQLModel classes in the application.
    Crud: A class to perform CRUD operations on a SQLModel.
"""
