import logging
import argparse
from .my_parser import MyParser, RssKeywords
from .create_file import CreateFile

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
    return parser


def parsing_rss(arg):
    logger = logging.getLogger(__name__)
    """ Parsing rss file

    :param arg: users conditions
    :return: rss object with parsing information
    """
    output = ""
    try:
        keys = RssKeywords()
        keys.title = "title"
        keys.date = "pubdate"
        keys.image_link = "enclosure"
        keys.description = "description"
        # keys.format_of_date = "%Y-%m-%dT%H:%M:%SZ"
        keys.format_of_date = "%a, %d %b %Y %H:%M:%S %z"
        rss = MyParser(arg.source, limit=arg.limit, json_format=arg.json,
                       date=arg.date, colorize=arg.colorize, keys=keys)
        output = rss
    except Exception as e:
        print(e)
    finally:
        logger.info("End process!")
    return output


def main():
    logger = logging.getLogger(__name__)

    parser = create_utility()
    args = parser.parse_args()

    if args.version:
        print("1.4")
        exit(0)

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(name)s '
                                   '%(levelname)s:%(message)s')
        logger.info("starting the process")

    rss = parsing_rss(args)
    print(rss)

    if args.to_html:
        CreateFile(rss=rss, html=args.to_html, date=args.date)
    if args.to_fb2:
        CreateFile(rss=rss, fb2=args.to_fb2, date=args.date)


if __name__ == '__main__':
    main()