from .my_parser import MyParser
from datetime import datetime
import logging
# For create HTML
import threading
import dominate
# For create fb2
from dominate.tags import meta, style, a, div, img, h1, h2, h3
from FB2 import FictionBook2, Author
import xml.etree.ElementTree as ET
from urllib import request
import base64


class CreateFile:
    """ Creating a news file in the following formats:
            fb2, html

        Attributes:
            rss: object that stores a dictionary with information
            html: the name of file t be created
            fb2: the name of file t be created
            date: date of the searching news
    """

    logger = logging.getLogger(__name__)

    def __init__(self, rss: MyParser = None, *,
                 date: str = None):
        self.rss = rss
        self.doc = ""
        self.link = None
        try:
            self.news_date = datetime.strptime(date, "%Y%m%d")\
                if date else None
        except Exception:
            raise self.logger.error("incorrect date")
        # self.create_file(html=html, fb2=fb2)

    def create_file(self, html=None, fb2=None):
        """Create code for writing in file file and write on file

        :param html: link of file
        :param fb2: link of file
        :return: None
        """
        if not isinstance(self.rss, MyParser):
            raise TypeError("Not rss file")
        elif html and html[-5:] != ".html":
            raise TypeError("Incorrect link for html.")
        elif fb2 and len(fb2) < 5 or fb2 and fb2[-4:] != ".fb2":
            raise TypeError("Incorrect link for fb2.")

        if html:
            link = html
            self.doc = self.create_sample_html()
            self.write(link)
        elif fb2:
            link = fb2
            self.doc = self.create_sample_fb2()
            self.write(link)

    def create_sample_html(self):
        """Create html code

        For the function work, must be present class attributes
            self.rss and self.html. If self.rss not MyParser class
            or self.html has incorrect format raise TypeError.
            raise TypeError
        In this function
        :param self.link - link of creating file
        :param self._style_for_html - styles of html
        :param self.rss - rss Object with info
        :param self.news_date - date of news
        :return: str code for html file
        """
        date = datetime.strptime(self.rss[0]["date"][0:10], "%Y-%m-%d")
        doc = dominate.document(title='Dominate your HTML')

        # Create head of html
        with doc.head:
            meta(charset="utf8")

        # Create body
        with doc:
            style(self._styles_for_html)
            div(h1("Special News"), cls="header")
            container = div(h1(datetime.strftime(date, "%Y.%m.%d")),
                            id="data container", cls="container")

            # Create News containers
            for el in self.rss:
                if self.news_date and self.news_date > \
                        datetime.strptime(el["date"][0:10], "%Y-%m-%d"):
                    break
                elif date > datetime.strptime(el["date"][0:10], "%Y-%m-%d"):
                    container

                    date = datetime.strptime(el["date"][0:10], "%Y-%m-%d")
                    container = div(h1(datetime.strftime(date, "%Y.%m.%d")),
                                    id="data container", cls="container")
                else:
                    with container:
                        with div(cls="news"):
                            with div(cls="image_container"):
                                a(img(src=el["image link"]),
                                  href=el["image link"])
                            with div(cls="description"):
                                a(el["title"], href=el["news link"])
                                h2(el["date"], cls="date")
                                h3(el["description"])
                            div(cls="clear")
        return doc.render()

    @staticmethod
    def convert_image(ls, n, href):
        """Cover image in binary format

        :param n: number of image in fb2 file
        :param href: link of image
        :return: None
        """
        try:
            image = request.urlopen(href).read()
            ls.append(f"<binary id=\"{n}\" content-type=\"image/jpeg\">" +
                      str(base64.b64encode(image))[2:-1] + "</binary>")
        except Exception:
            ...
            # print("incorrect certificate of image.")
            # С другими rss работает.
            # Я так понял, что это проблемма этого сайта

    def create_sample_fb2(self):
        """Create fb2 code

        For the function work, must be present class attributes
            self.rss and self.html. If self.rss not MyParser class
            or self.html has incorrect format raise TypeError.
            raise TypeError.
        Attributes:
            n: number of image id
            ls: list of adding info in body
            x_thread: list of threads
            date: date of news posting

        :return: str code for fb2 file
        """
        book = FictionBook2()
        book.titleInfo.title = "Special news!"
        book.titleInfo.annotation = "Эта книга представляет собой новостную" \
                                    " ленту, разработанную лучшим " \
                                    "программистом: Селивончиком Николаем." \
                                    " Спасибо за ваш интерес. "
        book.titleInfo.authors = [Author(firstName="Nikolay",
                                         lastName="Selivonchyk",
                                         nickname="still_dog",
                                         emails=["still_student@mail.ru"],
                                         homePages=["inst:still_dog"], )]
        book.titleInfo.genres = ["news", "ru_news"]
        book.titleInfo.coverPageImages = [
            request.urlopen("https://www.handcraftguide.com/sites/"
                            "default/files/styles/original___water/public"
                            "/3blackphonewallpaper.jpg"
                            "?itok=bfSUKyow").read()]
        book.titleInfo.sequences = [("News", 2)]
        book.documentInfo.authors = ["Selivonchyk Kolya"]
        book.documentInfo.version = "1.5"

        n = 0
        binary_images = []
        x_thread = []
        ls = []
        date = datetime.strptime(self.rss[0]["date"][0:10], "%Y-%m-%d")
        for el in self.rss:
            if self.news_date and self.news_date > \
                    datetime.strptime(el["date"][0:10], "%Y-%m-%d"):
                break

            ls.extend([ET.fromstring("<subtitle> * * * </subtitle>"),
                       ET.fromstring("<strong><p>" + el["title"] +
                                     "</p></strong>"),
                       ET.Element("image", attrib={"xlink:href": "#{}"
                                  .format(n)}),
                       ET.fromstring("<epigraph><p>" + el["date"] +
                                     "</p></epigraph>"),
                       ET.fromstring("<p>" + el["description"] + "</p>"),
                       ET.fromstring("<p>" + el["news link"] + "</p>")
                       ])
            x_thread.append(threading.Thread(target=self.convert_image,
                                             args=(binary_images, n,
                                                   el["image link"])))
            x_thread[n].start()

            if date > datetime.strptime(el["date"][0:10], "%Y-%m-%d"):
                ls.append(ET.fromstring("<subtitle>___________________________"
                                        "________________________</subtitle>"))
                book.chapters.append((datetime.strftime(date, "%Y.%m.%d"), ls))
                date = datetime.strptime(el["date"][0:10], "%Y-%m-%d")
                ls = []
            n += 1

        for el in x_thread:
            el.join()

        # create str of output code
        code = str(book)[0:-15]
        for el in binary_images:
            code += el
        code += str(book)[-15:]

        return code

    def write(self, link):
        with open(link, 'w', encoding="UTF-8") as file:
            file.write(self.doc)

    def __str__(self):
        return "lol"
        return self.doc

    # Classes for html elements
    _styles_for_html = """
        body {
            background: beige;
            margin: 0px;
            padding: 0px;
            }
        .header h1{
            font-size: 30px;
            margin-top: 0;
            padding-top: 10px;
            padding-left: 30px;
            color: azure;
            font-family: 'Permanent Marker', cursive;

        }
        .container h1{
            font-size: 28px;
            text-align: left;
            margin-left: 100px;
            font-family: 'Karantina', cursive;
        }
        .description h3{
            font-size: 16px;
            text-align: left;
            font-weight: 400;
            }
        .container{
            padding-bottom: 50px;
            background: floralwhite;
            margin-left: 20px;
            margin-right: 20px;
            }
        .news{
            width: 100%;
            padding-bottom: 40px;
            padding-top: 30px;
            background: floralwhite;
            margin-bottom: 20px;
            }
        .image_container{
            width: 150px;
            float:left;
            margin-left: 100px;
            display: flex;
        }
        .description{
            width: 60%;
            max-height: 100%;
            margin-left: 100px;
            float:left;
        }
        .header{
            display: flex;
            height: 60px;
            background:black;
            }
        .clear{
            clear:left;
        }
        .date{
            font-size: 16px;
            color:gainsboro;
        }
        img{
            max-width: 100%;
            border: 0;
        }
        a {
            display: inline-block;
            display: block;
            font-size: 20px;
            font-weight: 700;
            text-align: left;
            color: black;
            text-decoration: none;
            cursor: pointer;
            }
        a:hover{
            color: #3d9ef9;
            text-decoration:none;
        }
        """
