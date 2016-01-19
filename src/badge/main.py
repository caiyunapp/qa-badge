# -*- coding: utf-8 -*-

from flask import Flask

application = Flask(__name__, static_url_path='')
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
    return application.send_static_file('static/badges/%s/%s.svg' % (repo, badge))


def main():
    application.debug = True
    application.run()


if __name__ == "__main__":
    main()
