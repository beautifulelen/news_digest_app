import urllib3
import datetime
from django.template.loader import get_template

from bs4 import BeautifulSoup
from .models import Category, News


RSS_SITE = 'https://lenta.ru/rss'

def parse_date(str_date):
    return datetime.datetime.strptime(str_date, '%a, %d %b %Y %H:%M:%S %z')


def get_html():
    http = urllib3.PoolManager()
    r = http.request('GET', RSS_SITE)
    return r.data

def html_to_news(html_doc):
    bs = BeautifulSoup(html_doc, features='lxml-xml')
    for title, description, category, pub_date, link in zip(bs.select('item > title'),
                                                            bs.select('item > description'),
                                                            bs.select('item > category'),
                                                            bs.select('item > pubDate'),
                                                            bs.select('item > link')):
        news = News.objects.filter(name=title.string)
        if not news:
            categories, create_category = Category.objects.get_or_create(name=category.string)
            news = News(name=title.string,
                        description=str(description.next_element.string).strip('\n').strip(' ').strip('\n'),
                        date=parse_date(pub_date.string),
                        category=categories,
                        link=link.string)
            news.save()


def render_to_html(template_src, context_dict):
    template = get_template(template_src)
    html  = template.render(context_dict)
    return html


def get_date_text(type_date_key, search_param):
    date_str = search_param.get(type_date_key)
    if type_date_key == 'to':
        preposition = ' по'
    elif type_date_key == 'from':
        preposition = ' с'
    text = ''
    if date_str:
        text = ' %s %s' % (preposition, datetime.datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ'). \
            strftime('%d %B %Y %H:%M'))
    return text

def get_category_text(search_param):
    category_array = search_param.get('category')
    if category_array:
        if len(category_array) > 1:
            category_text = 'категориям: '
        else:
            category_text = 'категории: '

        category_text += ', '.join([Category.objects.get(pk=category_id).name for category_id in category_array])
    else:
        category_text = 'всем категориям'
    return category_text


def form_title(search):
    return 'Сводка новостей по %s%s%s' % (get_category_text(search.param),
                                          get_date_text('from', search.param),
                                          get_date_text('to', search.param))



