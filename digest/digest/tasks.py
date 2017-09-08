from django.core import mail
from functools import wraps
from email.mime.text import MIMEText
from .celeryconf import app
from .models import Job, Search
from .utils import get_html, render_to_html, form_title, html_to_news

# декоратор для предотвращения дублирования кода
def update_job(fn):
    """Decorator that will update Job with result of the function"""
    # wraps создаст имя и  docstring функции fn доступный для интроспекции сельдерея
    @wraps(fn)
    def wrapper(job_id=None, *args, **kwargs):
        if not job_id:
            # создаем задание для автопарсинга
            job = Job(type='get_rss', status='started', kwargs={})
        else:
            job = Job.objects.get(id=job_id)
            job.status = 'started'
        job.save()
        try:
            # выполняем задание с заданными аргументами
            fn(*args, **kwargs)
            job.status = 'finished'
            job.save()
        except Exception as ee:
            raise ee # TODO: только для отладки
            job.status = 'failed'
            job.save()
    return wrapper



@app.task
@update_job
def get_rss(args={}):
    """Парсит RSS заданного сайти и создает новости"""
    html_doc = get_html()
    html_to_news(html_doc)

@app.task
@update_job
def send_email(args):
    search = Search.objects.get(pk=args['pk'])
    if search:
        query_set = search.filter_news()
        html = render_to_html('digest/to_mail.html', {'data': query_set,})
        mail.EmailMessage(subject=form_title(search),
                 body='',
                 attachments=(MIMEText(html, 'html'),),
                 to=(args['email'], ),).send()
    else:
        raise Exception('Search item not found')



# mapping from names to tasks
TASK_MAPPING = {
    'get_rss': get_rss,
    'send_email': send_email
}