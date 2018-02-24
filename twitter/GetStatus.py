#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Get status."""
import tweepy
import json
from keys import Consumer, Token


class GetStatus(object):
  """Get status."""

  def getStatus(self, **kwargs):
    """Get status."""
    c = Consumer()
    if 'DEBUG' in kwargs:
      t = Token(DEBUG = kwargs['DEBUG'])
    else:
      t = Token()
    auth = tweepy.OAuthHandler(c.key, c.secret)
    auth.set_access_token(t.key, t.secret)
    api = tweepy.API(auth)

    me = api.me()
    profiles = {}
    profiles['name'] = me.name
    profiles['location'] = me.location
    profiles['description'] = me.description
    profiles['icon'] = me.profile_image_url_https.replace('_normal', '')
    if me.profile_use_background_image == 'True':
      profiles['bg_image'] = me.profile_background_image_url_https
    else:
      profiles['bg_image'] = None
    return profiles



if __name__ == '__main__':
  g = GetStatus()
  print( g.getStatus() )
