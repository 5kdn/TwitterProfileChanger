#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Get status."""
import tweepy
import json
from keys import Consumer, Token


class GetStatus(object):
  """Get status."""

  def getStatus(self, *args):
    """Get status."""
    c = Consumer(*args)
    t = Token(*args)
    auth = tweepy.OAuthHandler(c.key, c.secret)
    auth.set_access_token(t.key, t.secret)
    api = tweepy.API(auth)

    me = api.me()
    profiles = {}
    profiles['name'] = me.name
    profiles['location'] = me.location
    profiles['description'] = me.description
    return json.dumps(profiles)


if __name__ == '__main__':
  g = GetStatus()
  print(g.getStatus())
