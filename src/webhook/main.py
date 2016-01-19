# -*- coding: utf-8 -*-

import os

from flask import Flask

application = Flask(__name__)
route = application.route
application.debug = True

@route('/qps/caiyun-backend-wrapper-new')
def index():
    cmd = "cd caiyun-backend-wrapper-new; source $HOME/bin/develop; $PRJ_HOME/bin/pref-test"
    os.system("ssh caiyun@inner.bench.caiyunapp.com '%s'" % cmd)
    return "OK"

def main():
    application.debug = True
    application.run()

if __name__ == "__main__":
    main()
