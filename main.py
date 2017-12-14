#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Flask."""

from flask import Flask
from GetStatus import GetStatus
from SetStatus import SetStatus


app = Flask(__name__)


@app.route('/')
def index():
  """Index."""
  return "Hello, World!"

@app.route('/getStatus')
def getStatus():
  """Get Status."""
  g = GetStatus()
  return g.getStatus()

@app.route('/setStatus')
def setStatus():
  """Set Status."""
  s = SetStatus()
  return s.setStatus()


if __name__ == '__main__':
  app.run(debug=True)
