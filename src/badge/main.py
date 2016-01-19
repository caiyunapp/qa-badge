# -*- coding: utf-8 -*-

import os

from flask import Flask, send_from_directory

application = Flask(__name__)
route = application.route
application.debug = True


@route('/')
def index():
    return "Hello World"


@route('/curtime')
def curtime():
    return '{"time": "2015-06-22 12:00"}'


@route('/badges/<string:repo>/<string:badge>.svg')
def send_badges(repo, badge):
    base_path = os.path.join(os.getcwd(), 'static', 'badges', repo)
    return send_from_directory(base_path, '%s.svg' % badge)

def main():
    application.debug = True
    application.run()


if __name__ == "__main__":
    main()
