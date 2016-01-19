# -*- coding: utf-8 -*-

from flask import Flask, send_from_directory

application = Flask(__name__, static_url_path='')
route = application.route
application.debug = True


@route('/')
def index():
    return "Hello World"


@route('/curtime')
def curtime():
    return '{"time": "2015-06-22 12:00"}'


@route('/badges/<path:path>')
def send_badges(path):
    return send_from_directory('static/badges', path)


def main():
    application.debug = True
    application.run()


if __name__ == "__main__":
    main()
