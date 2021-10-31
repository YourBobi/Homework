#!/usr/bin/env python3

import json
import logging
from datetime import datetime
# For parsing rss
from bs4 import BeautifulSoup
import requests
import timestring
# For colorize output
import os

os.system("")


class RssKeywords:

    title: str = ""
    date: str = ""
    news_link: str = ""
    image_links: list = []
    description: str = ""


class MyParser:
    """ Class that parsing site and write result in json.json file
            in format, which the user specified.

        Attributes:
            url: url of rss file
            limit: limit of news when printing an object
            json_format: printing in json format (true, False)
            date: date of the searching news
            colorize: color news output when printing

        Methods:
            parsing_rss: parse rss file.
            read_json: read json file with parsing information.
            write_json: write object in json file.
            _w_date: convert rss date of news in readable format.
            format_el: return standard format of news for printing.
            colorize_format_el: return standard format of news for printing.
            output_format: choose the format of output news and return
                news in str.
    """

    logger = logging.getLogger(__name__)

    def __init__(self, url: str, *,
                 header: str = None,
                 limit: int = None,
                 json_format: bool = False,
                 date: str = None,
                 colorize: bool = False,
                 keys: RssKeywords = None):
        self.logger.info("Start constructor")
        self.colorize_format = colorize
        self.json_format = json_format
        self.json_link = "json.json"
        try:
            self.date = datetime.strptime(date, "%Y%m%d") if date else None
        except Exception:
            raise ValueError("incorrect date")

        self.logger.info("Create json file and dict with information!")
        self.items_dict = self.parsing_rss(url, header, keys)
        self.limit = len(self.items_dict["items"]) \
            if limit is None or limit < 0 else limit
        # self.write_json()
        self.logger.info("End constructor")

    def parsing_rss(self, url, header=None, keys=None):
        """Parses the rss page according to the given url

        :param keys:
        :param url: url of rss file
        :return: dict with information
        """
        self.logger.info(f"Start parse {url}")
        if not url and not self.date:
            raise ValueError("error: the following arguments "
                             "are required: source")
        elif not isinstance(keys, RssKeywords):
            raise TypeError("Type error. Keys are not RssKeywords")

        try:
            soup = BeautifulSoup(requests.get(url, headers=header).text,
                                 'lxml')
        except requests.exceptions.ConnectionError:
            raise requests.exceptions.ConnectionError("Connection error")
        except Exception:
            if not self.date:
                raise IOError("Invalid Url")
            items = False
            feed = ''
        else:
            items = soup.find_all('item')
            feed = soup.find('title').get_text(strip=True)

        return {
            "feed": feed,
            "items":
                [{"title": el.find(keys.title).get_text(strip=True)
                  if el.find(keys.title) else "",
                  "date": self._w_date(el.find(keys.date).get_text(strip=True))
                  if el.find(keys.date) else "",
                  "description": el.find(keys.description).get_text(strip=True)
                  if el.find(keys.description) else "",
                  "news link": el.link.next_sibling.get_text(strip=True)
                  if el.link else "",
                  "image link": el.find(self._w_image(keys.image_links,
                                                      el)).get("url")
                  if self._w_image(keys.image_links, el) else ""
                  } for el in items]
        } if items else self.read_json()

    def sort(self):
        length = len(self.items_dict['items'])
        for i in range(length - 1):
            for j in range(i+1, length):
                if datetime.strptime(self[i]['date'][0:10], "%Y-%m-%d") < \
                        datetime.strptime(self[j]['date'][0:10], "%Y-%m-%d"):
                    self.items_dict['items'][i], self.items_dict['items'][j] =\
                        self.items_dict['items'][j], self.items_dict['items'][i]

    def read_json(self):
        """Read json file

        :return: dict from json file
        """
        try:
            self.logger.info("Start read in file:{}".format(self.json_link))
            with open(self.json_link, 'r') as file:
                data = json.load(file)
                self.logger.info("End read json file!")
        except Exception:
            raise FileNotFoundError("could not read json file. "
                                    "Not file or file is empty.")

        return data

    def write_json(self):
        """Write result of parsing in file

        :return: None
        """
        self.logger.info("Start writing in file: {}".format(self.json_link))
        with open(self.json_link, 'w', encoding="UTF-8") as file:
            json.dump(self.items_dict, file, indent=3)
            self.logger.info("End writing in file: {}".format(self.json_link))

    @staticmethod
    def _w_date(date):
        """Converts date to human readable format

        :param date: date from rss
        :return: str date
        """
        try:
            out = str(timestring.Date(date))
        except Exception:
            raise ValueError("Change format of date")
        return out

    @staticmethod
    def _w_image(forms, item):
        """
        :param forms: list of image names
        :param item: element of items
        :return: name of image name or none
        """
        try:
            for el in forms:
                if item.find(el):
                    return el
        except Exception:
            raise ValueError("Change keys.images_links")
        else:
            return None

    @staticmethod
    def format_el(el):
        """Convert dict on output str

        :param el: element of rss object
        :return: beautiful str
        """
        return "Title: {0}" \
               "\nDate: {1}" \
               "\nLink: {2}" \
               "\nDescription: {3}" \
               "\nLinks:" \
               "\n[1]{2} (link)" \
               "\n[2] {4} (image)\n\n".format(el["title"], el["date"],
                                              el["news link"],
                                              el["description"],
                                              el["image link"])

    @staticmethod
    def colorize_format_el(el):
        """Convert dict on output str with color

                :param el: element of rss object
                :return: beautiful str with color
                """
        return "Title: \033[47m\033[30m {0} \033[0m"\
               "\nDate: \033[4m {1} \033[0m" \
               "\nLink: \033[34m {2} \033[0m" \
               "\nDescription: \033[33m\033[1m {3} \033[0m" \
               "\nLinks:" \
               "\n[1] \033[34m {2} \033[0m (link)\n" \
               "[2] \033[34m {4} \033[0m (image)\n\n".format(el["title"],
                                                             el["date"],
                                                             el["news link"],
                                                             el["description"],
                                                             el["image link"])

    def output_format(self):
        """Prepares an object for output

        Checks all conditions that the user specified when creating
        an object and returns a string in the desired format
        :return: output str
        """
        if self.json_format:
            self.logger.info("Convert object in str(json) for __str__")
            output = ""
            n = 0
            for el in self:
                if not el["date"] and self.date or self.date and self.date \
                        != datetime.strptime(el["date"][0:10], "%Y-%m-%d"):
                    continue
                elif n == self.limit or self.date and self.date >\
                        datetime.strptime(el["date"][0:10], "%Y-%m-%d"):
                    break
                else:
                    output += json.dumps(el, indent=2)
                    n += 1
        else:
            self.logger.info("Convert object in str for __str__")
            output = "Feed: " + self.items_dict["feed"] + "\n"
            n = 0
            for el in self:
                if not el["date"] and self.date or self.date and self.date\
                        != datetime.strptime(el["date"][0:10], "%Y-%m-%d"):
                    continue
                elif n == self.limit or self.date and self.date >\
                        datetime.strptime(el["date"][0:10], "%Y-%m-%d"):
                    break
                else:
                    n += 1
                    output += "\n" + str(n) + ")"
                    output += self.colorize_format_el(el)\
                        if self.colorize_format else self.format_el(el)

        return output

    def __getitem__(self, item):
        return self.items_dict["items"][item]

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i < len(self.items_dict["items"]):
            r = self.items_dict["items"][self.i]
            self.i += 1
            return r
        else:
            del self.i
            raise StopIteration

    def __str__(self):
        return self.output_format()
