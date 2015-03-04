# -*- coding:utf-8 -*-
# PROJECT_NAME : invoker
# FILE_NAME    : 
# AUTHOR       : younger shen


class BaseValidatorException(Exception):

    def __str__(self):
        return self.message

    def __unicode__(self):
        return self.__str__()


class InvalidValidateDataError(BaseValidatorException):

    def __init__(self, message=None):
        self.message = message if message else 'invalid validate data error'


class InvalidMinValidatorParameterError(BaseValidatorException):

    def __init__(self, message=None):
        self.message = message if message else 'invalid MIN validator parameter error'


class InvalidMaxValidatorParameterError(BaseValidatorException):

    def __init__(self, message=None):
        self.message = message if message else 'invalid MAX validator parameter error'


class InvalidRangeValidatorParameterError(BaseValidatorException):

    def __init__(self, message=None):
        self.message = message if message else 'invalid RANGE validator parameter error'


class InvalidLengthValidatorParameterError(BaseValidatorException):

    def __init__(self, message=None):
        self.mesage = message if message else 'invalid LENGTH validator parameter error'


class InvalidAcceptedValidatorParameterError(BaseValidatorException):

    def __init__(self, message=None):
        self.message = message if message else 'invalid ACCEPTED validator parameter error'


class InvalidDataError(BaseValidatorException):

    def __init__(self, message=None):
        self.message = message if message else 'invalid data error'


class InvalidRuleNameError(BaseValidatorException):

    def __init__(self, message=None):
        self.message = message if message else 'invalid rule name error'
