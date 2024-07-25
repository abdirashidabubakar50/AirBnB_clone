#!/usr/bin/python3

# models/__init__.py

"""
models package initialization file.

This file allows the models package to be imported and initializes the package.
"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
