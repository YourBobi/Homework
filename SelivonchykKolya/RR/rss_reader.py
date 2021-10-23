#!/usr/bin/env python3

import logging
import argparse
from RR import MyParser, RssKeywords, CreateFile
import RR

URL = "https://vse.sale/news/rss/"


def create_utility():
    """ Obtaining information about the necessary processes

        Attributes:
            --version          Print version info
            --json             Print result as JSON in stdout
            --verbose          Outputs verbose status messages
            --colorize         Colorize output
            --limit LIMIT      Limit news topics if this parameter provided
            --date DATE        Date
            --to-html TO_HTML  Make .html file
            --to-fb2 TO_FB2    Make .fb2 file

        :return: parser with arguments that user print
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", help="Print version info",
                        action="store_true")
    parser.add_argument("--json", help="Print result as JSON in stdout",
                        action="store_true")
    parser.add_argument("--verbose", help="Outputs verbose status messages",
                        action="store_true")
    parser.add_argument("--colorize", help="Colorize output",
                        action="store_true")
    parser.add_argument("--limit", type=int, help="Limit news topics if this "
                                                  "parameter provided")
    parser.add_argument("--date", type=str, help="Date")
    parser.add_argument("--to-html", type=str, help="Make .html file")
    parser.add_argument("--to-fb2", type=str, help="Make .fb2 file")
    parser.add_argument("source", nargs="?", type=str, help="RSS URL")
    return parser.parse_args()


def create_keys():
    keys = RssKeywords()
    keys.title = "title"
    keys.date = "pubdate"
    keys.image_links = ["enclosure",
                        "media:content"]
    keys.description = "description"
    return keys


def parsing_rss(arg):
    """ Parsing rss file

    :param arg: users conditions
    :return: rss object with parsing information or ""
    """
    return MyParser(arg.source, limit=arg.limit, json_format=arg.json,
                   date=arg.date, colorize=arg.colorize, keys=create_keys())


def main():
    logger = logging.getLogger(__name__)

    args = create_utility()

    if args.version:
        print(RR.__version__)
        exit(0)

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(name)s '
                                   '%(levelname)s:%(message)s')

    try:
        logger.info("starting the process")
        rss = parsing_rss(args)
        rss.write_json()
        print(rss)

        if args.to_html:
            CreateFile(rss=rss, date=args.date).create_file(html=args.to_html)
        if args.to_fb2:
            CreateFile(rss=rss, date=args.date).create_file(fb2=args.to_fb2)
    except Exception as e:
        print(e)
    finally:
        logger.info("End process!")


if __name__ == '__main__':
    main()
