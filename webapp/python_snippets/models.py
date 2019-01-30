from django.db import models
from django.utils import timezone


# Create your models here.
class PythonSnippet(models.Model):
    original_id = models.IntegerField(blank=False, null=False, unique=True)
    post_id = models.IntegerField(blank=False, null=False)
    pred_post_block_version_id = models.IntegerField(blank=True, null=True)
    root_post_block_version_id = models.IntegerField(blank=False, null=False)
    length = models.IntegerField(blank=False, null=False)
    line_count = models.IntegerField(blank=False, null=False)
    tags = models.CharField(max_length=2048, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    last_process_sent_p2 = models.DateTimeField(default=None, blank=True, null=True)
    last_process_sent_p3 = models.DateTimeField(default=None, blank=True, null=True)
    python2_result = models.TextField(blank=True, null=True)
    python3_result = models.TextField(blank=True, null=True)
    execution_time_p2 = models.FloatField(blank=True, null=True)
    execution_time_p3 = models.FloatField(blank=True, null=True)
    status_code_p2 = models.IntegerField(blank=True, null=True)
    status_code_p3 = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return f'{self.original_id}'

    def __str__(self):
        return self.__unicode__()
