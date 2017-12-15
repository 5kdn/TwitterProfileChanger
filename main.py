#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Flask."""

from flask import Flask, render_template, request, redirect, url_for
from GetStatus import GetStatus
from SetStatus import SetStatus


app = Flask(__name__, static_folder='static')


@app.route('/')
def index():
  """Index."""
  return redirect('/static/index.html')

@app.route('/main.css')
def main_css():
  """Index."""
  return redirect('/static/main.css')

@app.route('/script.js')
def script_js():
  """Index."""
  return redirect('/static/script.js')

@app.route('/skdn.jpg')
def skdn_jpg():
  """Index."""
  return redirect('/static/skdn.jpg')

@app.route('/edge-icons-Regular.woff')
def font_file():
  """Index."""
  return redirect('/static/edge-icons-Regular.woff')


@app.route('/getStatus')
def getStatus():
  """Get Status."""
  g = GetStatus()
  return g.getStatus()


@app.route('/setStatus', methods=['POST'])
def setStatus():
  """Set Status."""
  s = SetStatus()
  return s.setStatus()


if __name__ == '__main__':
  app.run(debug=True)
