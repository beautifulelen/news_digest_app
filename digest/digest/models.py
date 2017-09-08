from django.db import models
from django.contrib.postgres.fields import JSONField

class Job(models.Model):
    """Class describing a computational job"""
    # currently, available types of job are:
    TYPES = (
        ('get_rss', 'get_rss'),
        ('send_email', 'send_email')
    )

    # list of statuses that job can have
    STATUSES = (
        ('pending', 'pending'),
        ('started', 'started'),
        ('finished', 'finished'),
        ('failed', 'failed'),
    )

    type = models.CharField(choices=TYPES, max_length=20)
    status = models.CharField(choices=STATUSES, max_length=20)
    kwargs = JSONField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        """Save model and if job is in pending state, schedule it"""
        super(Job, self).save(*args, **kwargs)
        if self.status == 'pending':
            from .tasks import TASK_MAPPING
            task = TASK_MAPPING[self.type]
            task.delay(job_id=self.id, args=self.kwargs)


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class News(models.Model):
    date = models.DateTimeField('published_date')#todo pretty date
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=500)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return self.name


class Search(models.Model):
    param = JSONField()

    FILTER_FIELDS = {'category': 'category__in',
                     'from': 'date__gt',
                     'to': 'date__lt'}

    def filter_news(self):
        d = {}
        for request_key, filter_key in Search.FILTER_FIELDS.items():
            if request_key in self.param:
                d[filter_key] = self.param.get(request_key)
        if not d:
            qs = News.objects.all()
        else:
            qs = News.objects.filter(**d)
        return qs


