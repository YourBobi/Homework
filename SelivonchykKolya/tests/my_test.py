#!/usr/bin/env python3

from rss_reader import CreateFile, MyParser, RssKeywords, \
    create_keys, create_utility, parsing_rss, main
from datetime import datetime
import pytest
import argparse
import os

url = "https://vse.sale/news/rss"


@pytest.fixture()
def keys():
    keys = RssKeywords()
    keys.title = "title"
    keys.date = "pubdate"
    keys.image_link = "enclosure"
    keys.description = "description"
    keys.format_of_date = "%a, %d %b %Y %H:%M:%S %z"
    return keys


@pytest.fixture()
def rss(keys):
    return MyParser(url, keys=keys)


@pytest.fixture()
def create_file(rss):
    return CreateFile(rss)


class TestCreateFile:
    # Test create_file()
    def test_create_file_type_raises_rss(self, create_file):
        create_file.rss = "ghjkl"
        with pytest.raises(TypeError):
            create_file.create_file()

    def test_create_file_type_raises_html(self, create_file):
        with pytest.raises(TypeError):
            create_file.create_file(html="fghjkl")

    def test_create_file_type_raises_fb2(self, create_file):
        with pytest.raises(TypeError):
            create_file.create_file(fb2="fghjkl")

    def test_create_file_made_fb2(self, create_file):
        create_file.create_file(fb2="test.fb2")
        os.remove("test.fb2")

    def test_create_file_made_html(self, create_file):
        create_file.create_file(html="test.html")
        os.remove("test.html")

    def test_create_file_none(self, create_file):
        create_file.create_file()

    # Test write()
    def test_write(self, create_file):
        create_file.doc = "test"
        create_file.write(link="test.txt")
        os.remove("test.txt")

    def test_write_raises_file_not_found(self, create_file):
        with pytest.raises(FileNotFoundError):
            create_file.write()

    # Test convert_image()
    def test_convert_image_made(self, create_file):
        ls = []
        n = 1
        href = "https://www.handcraftguide.com/sites/default" \
               "/files/styles/original___water/public/3blackph" \
               "onewallpaper.jpg?itok=bfSUKyow"
        create_file.convert_image(ls, n, href)
        assert isinstance(ls[0], str)

    def test_convert_image_none(self, create_file):
        with pytest.raises(TypeError):
            create_file.convert_image()

    # Test create_sample_html()
    def test_create_sample_html_return(self, create_file):
        assert isinstance(create_file.create_sample_html(), str)

    # Test create_sample_html()
    def test_create_sample_fb2_return(self, create_file):
        assert isinstance(create_file.create_sample_fb2(), str)

    # Test __str__()
    def test_str(self, create_file):
        assert str(create_file) == ""

    # Test __str__()
    def test_init(self, create_file, rss):
        assert create_file.rss == rss
        assert isinstance(create_file.rss, MyParser)
        assert create_file.doc == ""
        assert create_file.link is None

    def test_init_raise(self, rss):
        with pytest.raises(ValueError):
            CreateFile(rss, date="dfghjkl;")


class TestMyParser:

    # Test parsing_rss()
    def test_parsing_rss_no_source_raises(self, rss, keys):
        url = None
        with pytest.raises(ValueError):
            rss.parsing_rss(url, header=None, keys=keys)

    def test_parsing_rss_value_keys_raises(self, rss):
        with pytest.raises(TypeError):
            rss.parsing_rss(url, header=None)

    def test_parsing_rss_io_raises(self, rss, keys):
        url = "kkkkkk"
        with pytest.raises(IOError):
            rss.parsing_rss(url, header=None, keys=keys)

    def test_parsing_rss_return(self, rss, keys):
        assert isinstance(rss.parsing_rss(url, header=None, keys=keys), dict)

    # Test write_json()
    def test_write_json(self, rss):
        rss.json_link = "test.json"
        rss.write_json()
        os.remove(rss.json_link)

    # Test write_json()
    def test_read_json(self, rss):
        rss.json_link = "test.json"
        rss.write_json()
        rss.read_json()
        os.remove(rss.json_link)

    def test_read_json_file_not_found(self, rss):
        rss.json_link = "test.json"
        with pytest.raises(FileNotFoundError):
            rss.read_json()

    # Test _w_date()
    def test_w_date_return(self, keys):
        assert isinstance(MyParser._w_date("Thu, 14 Oct 2021 20:51:00 +0300"),
                          str)

    def test_w_date_value_raises(self, keys):
        with pytest.raises(ValueError):
            MyParser._w_date("lalala")

    # Test format_el()
    def test_format_el_return(self, rss):
        el = rss[0]
        assert isinstance(MyParser.format_el(el), str)

    # Test colorize_format_el()
    def test_colorize_format_el_return(self, rss):
        el = rss[0]
        assert isinstance(MyParser.format_el(el), str)

    # Test output_format()
    def test_output_format_json(self, rss):
        rss.json_format = True
        assert isinstance(rss.output_format(), str)

    def test_output_format_json_date(self, rss):
        rss.json_format = True
        string1 = rss.output_format()
        rss.date = datetime.strptime("20211019", "%Y%m%d")
        string2 = rss.output_format()
        assert string1 != string2

    def test_output_format_normal(self, rss):
        assert isinstance(rss.output_format(), str)

    def test_output_format_normal_date(self, rss):
        string1 = rss.output_format()
        rss.date = datetime.strptime("20211019", "%Y%m%d")
        string2 = rss.output_format()
        assert string1 != string2

    # Test __str__()
    def test_str(self, rss):
        assert isinstance(rss.__str__(), str)

    # Test __init__()
    def test_init(self, keys):
        rss = MyParser(url, keys=keys)
        assert rss.colorize_format is False
        assert rss.json_format is False
        assert rss.json_link == "json.json"
        assert rss.date is None
        assert isinstance(rss.items_dict, dict)
        assert rss.limit == len(rss.items_dict["items"])

    def test_init_limit(self, keys):
        rss = MyParser(url, keys=keys, limit=1)
        assert rss.colorize_format is False
        assert rss.json_format is False
        assert rss.json_link == "json.json"
        assert rss.date is None
        assert isinstance(rss.items_dict, dict)
        assert rss.limit == 1

    def test_init_date(self, keys):
        rss = MyParser(url, keys=keys, limit=1, date="20211019")
        assert rss.colorize_format is False
        assert rss.json_format is False
        assert rss.json_link == "json.json"
        assert isinstance(rss.date, datetime)
        assert isinstance(rss.items_dict, dict)
        assert rss.limit == 1

    def test_init_json(self, keys):
        rss = MyParser(url, keys=keys, limit=1, date="20211019",
                       json_format=True)
        assert rss.colorize_format is False
        assert rss.json_format is True
        assert rss.json_link == "json.json"
        assert isinstance(rss.date, datetime)
        assert isinstance(rss.items_dict, dict)
        assert rss.limit == 1


class TestRssKeywords:

    def test_rss_keyword(self):
        keys = RssKeywords()
        keys.title = "title"
        keys.date = "pubdate"
        keys.image_link = "enclosure"
        keys.description = "description"
        keys.format_of_date = "%a, %d %b %Y %H:%M:%S %z"

        assert keys.title == "title"
        assert keys.date == "pubdate"
        assert keys.image_link == "enclosure"
        assert keys.description == "description"
        assert keys.format_of_date == "%a, %d %b %Y %H:%M:%S %z"


class TestRssReader:

    # Test create_keys()
    def test_create_keys(self):
        assert isinstance(create_keys(), RssKeywords)

    # Test create_utility()
    def test_create_utility(self):
        assert isinstance(create_utility(), argparse.Namespace)

    # Test parsing_rss()
    def test_parsing_rss(self):
        args = create_utility()
        args.source = url
        assert isinstance(parsing_rss(args), MyParser)

    # Test main()
    def test_main(self):
        main()


def run():
    exit(pytest.main(['-x']))


if __name__ == '__main__':
    run()
