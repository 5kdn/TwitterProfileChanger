#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Twitter key and secret of Consumer and Token."""


class Consumer(object):
  """Consumer key and secret."""

  # @5kdn
  key = 'fnBWZ0nhZT9FjpZTjo3uGQ'
  secret = 'PnueijMSQ98BtQxQDzi2ES6tgk9gYAfbwvQFhexhq7c'


class Token(object):
  """Token key and secret."""

  # @5kdn
  key = '56989640-XnXlqPPBccGz0UBpCrN196VsodblXDN9oG4jc8bvv'
  secret = 'JB3KgaKrx3NbG5RodulCiBMsGZdv6JXYNK7ErAKg'

  def __init__(self, DEBUG=True):
    """For debug user."""
    if DEBUG == True:
      # @sakuden
      self.key = '618019384-LlFm59ZOR6dKlg3Wb6luvbUGVRPObMPBgcxPS2hk'
      self.secret = 'Jc3WAHLdOXdGiax3gY8w4EL3BsNPGArMdcR15WYcsE'


if __name__ == '__main__':
  t = Token(DEBUG=True)
  print(t.key)

  u =Token()
  print(u.key)

