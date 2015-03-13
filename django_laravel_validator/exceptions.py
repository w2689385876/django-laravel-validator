# -*- coding:utf-8 -*-
# PROJECT_NAME : invoker
# FILE_NAME    : 
# AUTHOR       : younger shen


class BaseValidatorException(Exception):
    pass


class InvalidValidateDataError(BaseValidatorException):

    def __init__(self, message=None):
        self.message = message if message else 'invalid validate data error'

    def __str__(self):
        return self.message


class InvalidMinValidatorParameterError(BaseValidatorException):

    def __init__(self, message=None):
        self.message = message if message else 'invalid MIN validator parameter error'

    def __str__(self):
        return self.message


class InvalidMaxValidatorParameterError(BaseValidatorException):

    def __init__(self, message=None):
        self.message = message if message else 'invalid MAX validator parameter error'

    def __str__(self):
        return self.message


class InvalidRangeValidatorParameterError(BaseValidatorException):

    def __init__(self, message=None):
        self.message = message if message else 'invalid RANGE validator parameter error'

    def __str__(self):
        return self.message


class InvalidLengthValidatorParameterError(BaseValidatorException):

    def __init__(self, message=None):
        self.mesage = message if message else 'invalid LENGTH validator parameter error'

    def __str__(self):
        return self.message


class InvalidAcceptedValidatorParameterError(BaseValidatorException):

    def __init__(self, message=None):
        self.message = message if message else 'invalid ACCEPTED validator parameter error'

    def __str__(self):
        return self.message


class InvalidActiveURLValidatorParameterError(BaseValidatorException):

    def __init__(self, message=None):
        self.message = message if message else 'invalid active_url validator parameter error'

    def __str__(self):
        return self.message


class InvalidAlphaValidatorParameterError(BaseValidatorException):

    def __init__(self, message=None):
        self.message = message if message else 'invalid alpha validator parameter error'

    def __str__(self):
        return self.message


class InvalidRegexValidatorParameterError(BaseValidatorException):

    def __init__(self, message=None):
        self.message = message if message else 'invalid regex validator parameter error'

    def __str__(self):
        return self.message


class InvalidDataError(BaseValidatorException):

    def __init__(self, message=None):
        self.message = message if message else 'invalid data error'

    def __str__(self):
        return self.message


class InvalidRuleNameError(BaseValidatorException):

    def __init__(self, message=None, rule=None):
        self.message = message if message else 'invalid rule name error'
        if rule:
            self.message = self.message + ': ' + rule

    def __str__(self):
        return self.message


class InvalidMatchValidatorParameterError(BaseValidatorException):

    def __init__(self, message=None):
        self.message = message if message else 'invalid match validator parameter error'

    def __str__(self):
        return self.message


class InvalidValidateDataError(BaseException):

    def __init__(self, message=None):
        self.message = message if message else 'invalid validate data error'

    def __str__(self):
        return self.message


class InvalidUniqueValidatorParameterError(Exception):

    def __init__(self, message=None):
        self.message = message if message else 'invalid unique validator parameter error'

    def __str__(self):
        return self.message

