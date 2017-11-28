#!/bin/env python
"""
Author: Lucas Fonseca
Version: 1.0.0

"""
from app import create_app, socketio

app = create_app(debug=True)

if __name__ == '__main__':
    socketio.run(app)
