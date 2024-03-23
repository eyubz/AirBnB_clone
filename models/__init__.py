#!/usr/bin/python3
""" Init module """
from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
