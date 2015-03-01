# -*- coding:utf-8 -*-
# PROJECT_NAME : invoker
# FILE_NAME    : 
# AUTHOR       : younger shen
from django.utils.translation import ugettext_lazy as _


class InvalidValidateDataError(Exception):

    def __init__(self, message):
        self.message = message if message else _('invalid validate data error')

    def __str__(self):
        return self.message

    def __unicode__(self):
        return self.__str__()