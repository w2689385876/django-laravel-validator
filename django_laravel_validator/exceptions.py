# -*- coding:utf-8 -*-
# PROJECT_NAME : invoker
# FILE_NAME    : 
# AUTHOR       : younger shen


class InvalidValidateDataError(Exception):

    def __init__(self, message=None):
        self.message = message if message else 'invalid validate data error'

    def __str__(self):
        return self.message

    def __unicode__(self):
        return self.__str__()


class InvalidMinValidatorParameterError(Exception):

    def __init__(self, message=None):
        self.message = message if message else 'invalid MIN validator parameter error'

    def __str__(self):
        return self.message

    def __unicode__(self):
        return self.__str__()