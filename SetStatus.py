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
    c = Consumer(*args)
    t = Token(*args)
    auth = tweepy.OAuthHandler(c.key, c.secret)
    auth.set_access_token(t.key, t.secret)
    self.__api = tweepy.API(auth)


  def setStatus(self, name, description, location, tweet):
    """Set status."""
    print(f'n: {name}')
    print(f'd: {description}')
    print(f'l: {location}')
    print(f't: {tweet}')

    # if (name is not None) or (description is not None) or (location is not None):
    if (name is not None):
      self.__api.update_profile( name = name )
    if (description is not None):
      self.__api.update_profile( description = description )
    if (location is not None):
      self.__api.update_profile( location = location )

    if tweet is True:
      now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
      msg = f'{now}に@sakudenのプロフィールを変更しました?'
      self.__api.update_status(msg)

    return 0



# if __name__ == '__main__':
  # c = Consumer()
  # t = Token()
  # auth = tweepy.OAuthHandler(c.key, c.secret)
  # auth.set_access_token(t.key, t.secret)
  # api = tweepy.API(auth)
  # print(dir(api.me()))
  # s = SetStatus()
  # s.setStatus('name', 'description', 'location', true)
