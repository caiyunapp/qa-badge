# -*- coding: utf-8 -*-

import os

from flask import Flask, send_from_directory
from werkzeug.contrib.cache import FileSystemCache
from flask.ext.webcache import easy_setup, modifiers

application = Flask(__name__)
route = application.route
application.debug = True

werkzeug_cache = FileSystemCache('/tmp/.sleepycalc')
easy_setup(application, werkzeug_cache)


@route('/')
def index():
    return "Hello World"


@route('/curtime')
def curtime():
    return '{"time": "2015-06-22 12:00"}'


@route('/badges/<string:repo>/<string:branch>/<string:badge>.svg')
@modifiers.cache_for(seconds=0)
def send_badges(repo, branch, badge):
    base_path = os.path.join(os.getcwd(), 'static', 'badges', repo, branch)
    print base_path
    return send_from_directory(base_path, '%s.svg' % badge)


def main():
    application.debug = True
    application.run()


if __name__ == "__main__":
    main()
