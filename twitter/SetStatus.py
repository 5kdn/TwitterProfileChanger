#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Set status."""
import datetime
import json

import tweepy
import pytz
# from cerberus import Validator

from keys import Consumer, Token


class SetStatus(object):
  """Set status."""

  def __init__(self, *args, **kwargs):
    """Init."""
    c = Consumer()
    t = Token(*args)
    auth = tweepy.OAuthHandler(c.key, c.secret)
    auth.set_access_token(t.key, t.secret)
    self.__api = tweepy.API(auth)


  def setStatus(self, newname, newdescription, newlocation, tweet):
    """Set status."""
    print(f'n: {newname}')
    print(f'd: {newdescription}')
    print(f'l: {newlocation}')
    print(f't: {tweet}')

    try:
      if (len(newname       ) > 0): self.__api.update_profile( name        = newname )
      if (len(newdescription) > 0): self.__api.update_profile( description = newdescription )
      if (len(newlocation   ) > 0): self.__api.update_profile( location    = newlocation )
    except :
      print("error has occured; in SetStatus.py:34~39")

    try:
      if tweet is True:
        now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
        msg = f'{now}に@5kdnのプロフィールを変更しました? from 5kdnのプロフィール変更するやつ : https://5kdn.red/twitter/↓'
        self.__api.update_status(msg)
    except :
      print("error has occured; in SetStatus.py;44~")
      raise ValueError("error has occurred")
    finally:
      return

# if __name__ == '__main__':
  # c = Consumer()
  # t = Token()
  # auth = tweepy.OAuthHandler(c.key, c.secret)
  # auth.set_access_token(t.key, t.secret)
  # api = tweepy.API(auth)
  # print(dir(api.me()))
  # s = SetStatus()
  # s.setStatus('name', 'description', 'location', true)
