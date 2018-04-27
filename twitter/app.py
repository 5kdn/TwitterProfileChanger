#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Flask."""

import json

from flask import Flask, jsonify, redirect, render_template, request

from GetStatus import GetStatus
from Log import Log
from SetStatus import SetStatus

app = Flask(__name__, static_url_path='/twitter/static')

# if DEBUG is True, use @sakuden account
DEBUG = False


# static files
@app.route('/twitter/')
def index():
  """Index."""
  g = GetStatus(DEBUG=DEBUG)
  data = g.get_status()
  log = Log()
  # maxval : 最大文字数
  maxval = {
    "name"        : 50,
    "description" : 160,
    "location"    : 100,
  }
  return render_template('index.html', data=data, logs=log.get_all(), maxval=maxval)


@app.route('/twitter/css/<name>.css')
def main_css(name='main'):
  """Stylesheet."""
  return render_template(f'/css/{name}.css'), 200, {"Content-Type": 'text/css; charset=utf-8'}


@app.route('/twitter/js/<script>.js')
def script_js(script='script'):
  """Javascript."""
  return render_template(f'/js/{script}.js'), 200, {"Content-Type": 'text/javascript; charset=utf-8'}


@app.route('/twitter/static/edge-icons-Regular.woff')
def font_file():
  """Fontfile."""
  return redirect('/twitter/static/edge-icons-Regular.woff')


# ==============================================================================

@app.route('/twitter/getStatus')
def get_status():
  """Get Status."""
  g = GetStatus(DEBUG=DEBUG)
  return json.dumps( g.get_status() )


@app.route('/twitter/setStatus', methods=['POST'])
def set_status():
  """Set Status."""
  if request.headers['Content-Type'] != 'application/json; charset=UTF-8':
    print(request.headers['Content-Type'])
    return jsonify(res='error'), 400

  if 'name' in request.json.keys(): name = request.json['name']
  else: name = None

  if 'description' in request.json.keys(): description = request.json['description']
  else: description = None

  if 'location' in request.json.keys(): location = request.json['location']
  else: location = None

  if 'tweet' not in request.json.keys() or request.json['tweet'] is not True:
    tweet = False
  else: tweet = True

  try:
    s = SetStatus(DEBUG=DEBUG)
    s.set_status(name, description, location, tweet)
    g = GetStatus(DEBUG=DEBUG)
    new_prof = g.get_status()

    # Logging
    log = Log()
    log.add(name, description, location)

    return json.dumps( new_prof )
  except ValueError as err:
    print(err)
    return jsonify(res='error'), 500
  except Exception as err:
    print(err)
    return jsonify(res='error'), 501


@app.route('/twitter/getLogs')
def get_logs():
  """Get All logs."""
  log = Log()
  return jsonify(log.get_all())


@app.route('/twitter/getRecentLog')
def get_log():
  """Get All logs."""
  log = Log()
  return jsonify(log.get_recent())


if __name__ == '__main__':
  app.run()
