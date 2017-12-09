#!/usr/bin/python
#
# Screen scraper based API for BookMyShow.

import re
import urllib.request
import urllib.error
import pprint

class BookMyShowClient(object):
  NOW_SHOWING_REGEX = '{"event":"productClick","ecommerce":{"currencyCode":"INR","click":{"actionField":{"list":"Filter Impression:category\\\/now showing"},"products":\[{"name":"(.*?)","id":"(.*?)","category":"(.*?)","variant":"(.*?)","position":(.*?),"dimension13":"(.*?)"}\]}}}'
  COMING_SOON_REGEX = '{"event":"productClick","ecommerce":{"currencyCode":"INR","click":{"actionField":{"list":"category\\\/coming soon"},"products":{"name":"(.*?)","id":"(.*?)","category":"(.*?)","variant":"(.*?)","position":(.*?),"dimension13":"(.*?)"}}}}'

  def __init__(self, location = 'Bengaluru'):
    self.__location = location.lower()
    self.__url = "https://in.bookmyshow.com/%s/movies" % self.__location
    self.__html = None

  def __download(self):
    req = urllib.request.Request(self.__url, headers={'User-Agent' : "Magic Browser"})
    html = urllib.request.urlopen(req).read().decode('utf-8')
    return html

  def get_now_showing(self):
    if not self.__html:
      self.__html = self.__download()
    now_showing = re.findall(self.NOW_SHOWING_REGEX, self.__html)
    return now_showing

  def get_coming_soon(self):
    if not self.__html:
      self.__html = self.__download()
    coming_soon = re.findall(self.COMING_SOON_REGEX, self.__html)
    return coming_soon

  def create_url(self,show):
    return show

  def get_processed_names(self,shows):
    processed_names = []
    for show in shows:
      processed_names.append(self.create_url(show))
    return processed_names


def utility(city):
    bms_client = BookMyShowClient(city)
    now_showing = bms_client.get_now_showing()
    coming_soon = bms_client.get_coming_soon()
    return str(len(now_showing)) + ' movies playing in str(city) ' + str(bms_client.get_processed_names(now_showing))

if __name__ == '__main__':
  # Test code.
  bms_client = BookMyShowClient('Bangalore')
  now_showing = bms_client.get_now_showing()
  coming_soon = bms_client.get_coming_soon()
  print (str(len(now_showing))+' movies playing in Bengaluru: ', bms_client.get_processed_names(now_showing))