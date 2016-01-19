# -*- coding: utf-8 -*-

import os

from flask import Flask

application = Flask(__name__)
route = application.route
application.debug = True

@route('/qps/caiyun-backend-wrapper-new')
def index():
    cwd = os.getcwd()
    cmd = "%s/bin/perf-test" % cwd
    os.system("ssh caiyun@inner.bench.caiyunapp.com '%s'" % cmd)
    return "OK"

def main():
    application.debug = True
    application.run()

if __name__ == "__main__":
    main()
