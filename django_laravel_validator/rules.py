# -*- coding:utf-8 -*-
# PROJECT_NAME : laravel_validator
# FILE_NAME    : 
# AUTHOR       : younger shen
import re
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from .regex import RE_NUMBERIC
from .exceptions import InvalidMinValidatorParameterError
from .messages import REQUIRED_MESSAGE
from .messages import NUMERIC_MESSAGE
from .messages import MIN_MESSAGE
WITH_PARAMETERS_VALIDATOR = ['MIN', 'MAX', 'RANGE']


class RequiredValidator(RegexValidator):

    def __init__(self, **kwargs):
        super(RequiredValidator, self).__init__(**kwargs)
        self.code = 'required'
        self.message = REQUIRED_MESSAGE

    def __call__(self, value=None):
        value = value.strip()
        if value is None or value == '':
            raise ValidationError(self.message, code=self.code)


class NumericValidator(RegexValidator):

    def __init__(self, **kwargs):
        super(NumericValidator, self).__init__(**kwargs)
        self.code = 'numeric'
        self.message = NUMERIC_MESSAGE

    def __call__(self, value=None):
        if not re.match(RE_NUMBERIC, value):
            raise ValidationError(self.message, code=self.code)


class MinValidator(RegexValidator):

    def __init__(self, args=None, **kwargs):
        super(MinValidator, self).__init__(**kwargs)

        if not args:
            raise InvalidMinValidatorParameterError()

        self.length = args[0]
        self.code = 'min'
        self.message = MIN_MESSAGE.format(length=self.length)

    def __call__(self, value=None):
        value = value.strip()
        if len(value) < int(self.length):
            raise ValidationError(self.message, code=self.code)


REQUIRED = RequiredValidator()
NUMERIC = NumericValidator()
MIN = MinValidator