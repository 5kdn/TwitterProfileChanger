#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Flask."""

from flask import Flask, render_template, request, redirect, url_for, jsonify
from GetStatus import GetStatus
from SetStatus import SetStatus
import json

from unittest import mock

app = Flask(__name__, static_folder='static')


# static files
@app.route('/')
def index():
  # """Index."""
  status = json.loads(getStatus())
  print(status['name'])
  data = {
      'screen': status['name'],
      'description': status['description'],
      'location': status['location'],
    }
  return render_template('index.html', data=data)


@app.route('/css/<name>.css')
def main_css(name='main'):
  """Stylesheet."""
  return render_template(f'/css/{name}.css'), 200, {"Content-Type": 'text/css; charset=utf-8'}


@app.route('/js/<script>.js')
def script_js(script='script'):
  """Javascript."""
  return render_template(f'/js/{script}.js'), 200, {"Content-Type": 'text/javascript; charset=utf-8'}


  # return redirect('/static/js/{{script}}.js')
# @app.route('/static')
# def index():
#   """Index."""
#   return redirect('/static/index.html')

# @app.route('/css/<name>.css')
# def main_css(name='main'):
#   """Stylesheet."""
#   return redirect('/static/css/{{name}}.css')
# @app.route('/js/<script>.js')
# def script_js(script='script'):
#   """Javascript."""
#   return redirect('/static/js/{{script}}.js')

@app.route('/skdn.jpg')
def skdn_jpg():
  """Icon."""
  return redirect('/static/skdn.jpg')

@app.route('/edge-icons-Regular.woff')
def font_file():
  """Fontfile."""
  return redirect('/static/edge-icons-Regular.woff')


@app.route('/favicon.ico')
def favicon():
  """Favicon."""
  return redirect('/static/favicon.ico')

# ==============================================================================

@app.route('/getStatus')
def getStatus():
  """Get Status."""
  g = GetStatus()
  return g.getStatus()


@app.route('/setStatus', methods=['POST'])
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

  if 'tweet' not in request.json.keys() or inrequest.json['tweet'] is not True:
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
  except:
    return jsonify(res='error'), 500


if __name__ == '__main__':
  app.run(debug=True)

