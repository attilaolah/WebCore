#!/usr/bin/env python2.5
# encoding: utf-8

from datetime                           import datetime
from web.core                           import Application, Controller


class RootController(Controller):
    def index(self):
        return 'genshi:templates.now', dict(now=datetime.now())


app = Application.factory(root=RootController, debug=False)

if __name__ == '__main__':
    import                                  logging
    from paste                              import httpserver
    
    logging.basicConfig(level=logging.INFO)
    httpserver.serve(app, host='127.0.0.1', port='8080')
