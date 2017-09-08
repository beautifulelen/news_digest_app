import unittest
import datetime

from digest.digest.utils import html_to_news, parse_date, get_html


class TestRss(unittest.TestCase):
    def setUp(self):
        # todo create datebase connection
        pass

    def test_get_rss(self):
        html_doc = '''<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <language>ru</language>
    <title>Lenta.ru : Новости</title>
    <description>Новости, статьи, фотографии, видео. Семь дней в неделю, 24 часа в сутки</description>
    <link>http://lenta.ru</link>
    <image>
      <url>http://assets.lenta.ru/small_logo.png</url>
      <title>Lenta.ru</title>
      <link>http://lenta.ru</link>
      <width>134</width>
      <height>22</height>
    </image>
    <atom:link rel="self" type="application/rss+xml" href="http://lenta.ru/rss"/>
<item>
  <guid>https://lenta.ru/news/2017/08/22/blue/</guid>
  <title>В Индии устранили причину голубизны собак</title>
  <link>https://lenta.ru/news/2017/08/22/blue/</link>
  <description>
    <![CDATA[В индийском городе Мумбай закрыли предприятие, которое обвинили в сбросе промышленных отходов и красящих веществ в местную реку. В результате действий компании шерсть десятка собак стала голубой. На животных с необычным окрасом местные жители обратили внимание в начале августа.]]>
  </description>
  <pubDate>Tue, 22 Aug 2017 15:36:55 +0300</pubDate>
  <enclosure url="https://icdn.lenta.ru/images/2017/08/22/15/20170822150032347/pic_b2a77b3640419f7d988c40883e95fde3.jpg" length="55475" type="image/jpeg"/>
  <category>Из жизни</category>
</item>
</channel>
</rss>'''

        self.assertEqual(html_to_news(html_doc)[0].category, 'Из жизни')


    def testParseDate(self):
        self.assertEqual(parse_date('Mon, 21 Aug 2017 15:11:00 +0300'),
                         datetime.datetime(2017, 8, 21, 15, 11, 0, 0,
                                           datetime.timezone(datetime.timedelta(0, 60 * 60 * 3))))

    def testGetRss(self):
        self.assertEqual(get_html(), '')


if __name__ == "__main__":
    unittest.main()