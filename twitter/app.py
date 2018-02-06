#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Flask."""

from flask import Flask, render_template, request, redirect, url_for, jsonify
import json

from GetStatus import GetStatus
from SetStatus import SetStatus


app = Flask(__name__, static_url_path='/twitter/static')


# static files
@app.route('/twitter/')
def index():
  """Index."""
  status = json.loads(getStatus())
  print(status['name'])
  data = {
      'screen': status['name'],
      'description': status['description'],
      'location': status['location'],
    }
  return render_template('index.html', data=data)


@app.route('/twitter/css/<name>.css')
def main_css(name='main'):
  """Stylesheet."""
  return render_template(f'/css/{name}.css'), 200, {"Content-Type": 'text/css; charset=utf-8'}


@app.route('/twitter/js/<script>.js')
def script_js(script='script'):
  """Javascript."""
  return render_template(f'/js/{script}.js'), 200, {"Content-Type": 'text/javascript; charset=utf-8'}


@app.route('/twitter/static/skdn.jpg')
def skdn_jpg():
  """Icon."""
  return redirect('/twitter/static/skdn.jpg')

@app.route('/twitter/static/edge-icons-Regular.woff')
def font_file():
  """Fontfile."""
  return redirect('/twitter/static/edge-icons-Regular.woff')


# ==============================================================================

@app.route('/twitter/getStatus')
def getStatus():
  """Get Status."""
  g = GetStatus()
  return g.getStatus()


@app.route('/twitter/setStatus', methods=['POST'])
def setStatus():
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

  # print(f"send request : {request.json}")
  try:
    s = SetStatus()
    s.setStatus(name, description, location, tweet)
    g = GetStatus()
    newProf = g.getStatus()
    # ToDo:logging
    return newProf
  except ValueError as e:
    print(e)
    return jsonify(res='error'), 500
  except:
    return jsonify(res='error'), 501


if __name__ == '__main__':
  app.run()

