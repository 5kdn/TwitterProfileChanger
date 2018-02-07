#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Log to db and send discord."""

import os
import sqlite3
import datetime
from contextlib import closing
import json
import requests


class Log(object):
  """Log to db and discord."""

  __dbname = 'updatelog.db'

  def __init__(self, *args, **kwargs):
    """Create table if db is NOT exists."""
    if not os.path.exists(self.__dbname):
      print('db created')
      with closing(sqlite3.connect(self.__dbname)) as conn:
        c = conn.cursor()
        sql = '''create table updates (
                  id integer PRIMARY KEY AUTOINCREMENT,
                  name text,
                  description text ,
                  location text,
                  updated default CURRENT_TIMESTAMP
                );'''
        c.execute(sql)
        conn.commit()

  def __addDB(self, name, description, location):
    """Add updates for db."""
    with closing(sqlite3.connect(self.__dbname)) as conn:
      c = conn.cursor()
      sql = """insert into
                updates(name, description, location)
                values (?,    ?,           ?);
            """
      c.execute(sql , (name, description, location))
      conn.commit()
      print('db updated')

  def __sendDiscord(self, name, description, location):
    """Send updates for discord."""

    url     = 'https://discordapp.com/api/webhooks/410690057784131584/r22pmh6d0ud9J4FukETrPyrj8tn5piknnjEdvx03XhNPmoiHJvV8Rmr9HROZ1nBCHERg'
    headers = {"Content-Type" : "application/json"}
    data   = {"content": f"@5kdn's twitter profile has changed.\n[name]\n{name}\n[description]\n{description}\n[location]\n{location}"}
    data    = json.dumps(data).encode('utf-8')
    requests.post(url, data=data, headers=headers)




  def add(self, name, description, location):
    """Add updates for db and send for discord."""
    try:
      self.__addDB(name, description, location)
    except:
      print('failed to add db.')
    try:
      self.__sendDiscord(name, description, location)
    except:
      print('failed to send discord.')

  def getAll(self):
    """Return all updated log."""
    with closing(sqlite3.connect(self.__dbname)) as conn:
      c = conn.cursor()
      sql = 'select id, name, description, location, updated from updates order by id;'
      items = {}
      for row in c.execute(sql).fetchall():
        item = {}
        item['name']        = row[1]
        item['description'] = row[2]
        item['location']    = row[3]
        item['update']      = row[4]
        items[row[0]] = item
    return items

  def getRecent(self):
    """Return recentry updated log."""
    with closing(sqlite3.connect(self.__dbname)) as conn:
      c = conn.cursor()
      sql = 'select id, name, description, location from updates order by id desc;'
      ret = c.execute(sql).fetchone()
      item = {}
      item['name'] = ret[0]
      item['description'] = ret[1]
      item['location'] = ret[2]
    return item

def main():
  print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
  changeItem = { "name": "ensakud",
                 "location": "\u3042\u306e\u3001\u3053\u3053\u30c4\u30a4\u30fc\u30c8\u6b04\u3058\u3083\u306a\u3044\u3067\u3059\u3002\u3002\u3002",
                 "description": "\u6700\u8fd1\u540d\u524d\u5909\u3048\u3089\u308c\u306a\u304f\u306a\u3044\uff1f\u2193\u2190\u305d\u308cis\u3042\u308b"
                }
  l = Log()
  l.add(changeItem["name"], changeItem["location"], changeItem["description"])
  # =====================
  print('= getall ========================')
  for item in l.getAll():
    print(item)
  print('= get recent ====================')
  print(l.getRecent())

if __name__ == '__main__':
  main()
