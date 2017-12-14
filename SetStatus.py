#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Set status."""
import tweepy
import json
from cerberus import Validator
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


  def setStatus(self):
    """Set status."""
    return "hello"



if __name__ == '__main__':
  s = SetStatus()
  print(s.setStatus())

  schema = {
    'nam': {
        'type': 'string',
        'required': True,
        'empty': True,
        'regex': '',
        },
    'bio': {
        'type': 'string',
        'required': True,
        'empty': True,
        'regex': '',
        },
    'loc': {
        'type': 'string',
        'required': True,
        'empty': True,
        'regex': '',
        },
    'tweet':{
        'type': 'boolean',
        'empty': True,
        },
  }

  sche = {'a': {'type': 'boolean','empty': True,}}
  dict = {'a': True}
  v = Validator(sche)
  print( v.validate(dict) )



