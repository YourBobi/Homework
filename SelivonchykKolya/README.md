#This application is a parser for rss pages.

***
***
##Code of Conduct
Everyone interacting in the rss_reader project’s codebases, issue trackers, chat rooms, and mailing lists is expected to follow the PSF Code of Conduct.

##Package structure

1. RR
	* __init__.py
	* create_file.py
	* my_parser.py
	* rss_reader.py
2. tests
	* __init__.py
	* my_test.py
3. setup.py
4. README.md

##Iterations performed

- [ ]iterations 1

- [ ]iterations 2

- [ ]iterations 3

- [ ]iterations 4

- [ ]iterations 5

- [x]iterations 6

***
***

##Examples
####1. 
">>rss_reader.py https://vse.sale/news/rss --limit 1

Feed: Газета ВСЁ

1)Title: Скоро ездить на летней резине станет небезопасно
Date: 2021-10-20 20:01:00+03:00
Link: https://vse.sale/news/view/36906
Description: Синоптики назвали день, после которого менять шины будет уже поздно.
Links:
[1]https://vse.sale/news/view/36906 (link)
[2] http://vse.sale/files/news/2021/10/102375_1634737080.jpg (image)
"
***
####2. 
">>rss_reader.py https://vse.sale/news/rss --limit 1 --json

{
  "title": "\u0421\u043a\u043e\u0440\u043e \u0435\u0437\u0434\u0438\u0442\u044c \u043d\u0430 \u043b\u0435\u0442\u043d\u0435\u0439 \u0440\u0435\u0437\u0438\u043d\u0435 \u0441\u0442\u0430\u043d\u0435\u0442 \u043d\u0
435\u0431\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u043e",
  "date": "2021-10-20 20:01:00+03:00",
  "description": "\u0421\u0438\u043d\u043e\u043f\u0442\u0438\u043a\u0438 \u043d\u0430\u0437\u0432\u0430\u043b\u0438 \u0434\u0435\u043d\u044c, \u043f\u043e\u0441\u043b\u0435 \u043a\u043e\u0442\u043e\u0440\u043e\u04
33\u043e \u043c\u0435\u043d\u044f\u0442\u044c \u0448\u0438\u043d\u044b \u0431\u0443\u0434\u0435\u0442 \u0443\u0436\u0435 \u043f\u043e\u0437\u0434\u043d\u043e.",
  "news link": "https://vse.sale/news/view/36906",
  "image link": "http://vse.sale/files/news/2021/10/102375_1634737080.jpg"
}
'
***
####3. 
'a>rss_reader.py https://vse.sale/news/rss --limit 1 --date 20211018

Feed: Газета ВСЁ

1)Title: В Петрозаводске пройдут традиционные Гусаровские чтения
Date: 2021-10-18 19:05:00+03:00
Link: https://vse.sale/news/view/36881
Description: Читателей ждут традиционные познавательные мероприятия,
Links:
[1]https://vse.sale/news/view/36881 (link)
[2] http://vse.sale/files/news/2021/10/102375_1634570612.jpg (image)

'
***
####4.
'>rss_reader.py https://vse.sale/news/rss --version

1.0.1
' 
***
####5.
'>rss_reader.py https://vse.sale/news/rss --version -h

usage: rss_reader.py [-h] [--version] [--json] [--verbose] [--colorize] [--limit LIMIT] [--date DATE] [--to-html TO_HTML] [--to-fb2 TO_FB2] [source]

positional arguments:
  source             RSS URL

optional arguments:
  -h, --help         show this help message and exit
  --version          Print version info
  --json             Print result as JSON in stdout
  --verbose          Outputs verbose status messages
  --colorize         Colorize output
  --limit LIMIT      Limit news topics if this parameter provided
  --date DATE        Date
  --to-html TO_HTML  Make .html file
  --to-fb2 TO_FB2    Make .fb2 file
'

***
***
