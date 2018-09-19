#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Set status."""
import datetime

import pytz
import tweepy

from Log import Log
from keys import Consumer, Token


class SetStatus(object):
  """Set status."""

  def __init__(self, **kwargs):
    """Init."""
    c = Consumer()
    if 'DEBUG' in kwargs:
      t = Token(DEBUG=kwargs['DEBUG'])
    else:
      t = Token()
    auth = tweepy.OAuthHandler(c.key, c.secret)
    auth.set_access_token(t.key, t.secret)
    self.__api = tweepy.API(auth)

  def set_status(self, newname, newdescription, newlocation, tweet):
    """Set status."""
    print(f'n: {newname}')
    print(f'd: {newdescription}')
    print(f'l: {newlocation}')
    print(f't: {tweet}')

    try:
      if (len(newname       ) > 0): self.__api.update_profile( name        = newname )
      if (len(newdescription) > 0): self.__api.update_profile( description = newdescription )
      if (len(newlocation   ) > 0): self.__api.update_profile( location    = newlocation )
    except Exception as err:
      print("error has occured in SetStatus.py")
      print(err.value)

    try:
      if tweet is True:
        now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
        log = Log()
        url = log.get_recent()
        print(url)
        print(url['updated'])
        url = url['updated'].replace(' ', '-')
        print('A4')
        msg = f'{now}に@5kdnのプロフィールを変更しました? from 5kdnのプロフィール変更するやつ : https://5kdn.red/twitter/#{url} \nhttps://5kdn.red/twitter/'
        self.__api.update_status(msg)
    except Exception as err:
      print("error has occured in SetStatus.py")
      print(err.value)
      raise ValueError("error has occurred")


if __name__ == '__main__':
  s = SetStatus()
  s.set_status('name', 'description', 'location', True)
