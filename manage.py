#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: Keruila
@time: 2019/09/21
@file: manage.py
"""
from flaskr import create_app
from flask_script import Manager
from flask_migrate import MigrateCommand


app = create_app()
manager = Manager(app)
manager.add_command("db", MigrateCommand)


if __name__ == '__main__':
    manager.run()

