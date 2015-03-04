# -*- coding:utf-8 -*-
# PROJECT_NAME : laravel_validator
# FILE_NAME    : 
# AUTHOR       : younger shen
import re
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from .regex import RE_NUMBERIC
from .exceptions import InvalidMinValidatorParameterError
from .exceptions import InvalidMaxValidatorParameterError
from .exceptions import InvalidRangeValidatorParameterError
from .exceptions import InvalidLengthValidatorParameterError
from .exceptions import InvalidAcceptedValidatorParameterError
from .messages import REQUIRED_MESSAGE
from .messages import NUMERIC_MESSAGE
from .messages import MIN_MESSAGE
from .messages import MAX_MESSAGE
from .messages import RANGE_MESSAGE
from .messages import LENGTH_MESSAGE
from .messages import ACCEPTED_MESSAGE

WITH_PARAMETERS_VALIDATOR = ['MIN', 'MAX', 'RANGE']


class RequiredValidator(RegexValidator):

    def __init__(self, **kwargs):
        super(RequiredValidator, self).__init__(**kwargs)
        self.code = 'required'
        self.message = REQUIRED_MESSAGE

    def __call__(self, value=None):
        if value is None or value == '':
            raise ValidationError(message=self.message, code=self.code)


class NumericValidator(RegexValidator):

    def __init__(self, **kwargs):
        super(NumericValidator, self).__init__(**kwargs)
        self.code = 'numeric'
        self.message = NUMERIC_MESSAGE

    def __call__(self, value=None):
        if not re.match(RE_NUMBERIC, value):
            raise ValidationError(message=self.message, code=self.code)


class MinValidator(RegexValidator):

    def __init__(self, args=None, **kwargs):
        super(MinValidator, self).__init__(**kwargs)

        if not args or len(args) != 1 or args[0] is None or args[0] == '':
            raise InvalidMinValidatorParameterError()

        if not re.match(RE_NUMBERIC, args[0]):
            raise InvalidMinValidatorParameterError()

        self.min = int(args[0])
        self.code = 'min'
        self.message = MIN_MESSAGE.format(min=self.length)

    def __call__(self, value=None):

        if value is None or value == '':
            raise ValidationError(message=self.message, code=self.code)

        if len(value) < self.min:
            raise ValidationError(message=self.message, code=self.code)


class MaxValidator(RegexValidator):

    def __init__(self, args=None, **kwargs):
        super(MaxValidator, self).__init__(**kwargs)

        if not args or len(args) != 1 or args[0] is None or args[0] == '':
            raise InvalidMaxValidatorParameterError()

        if not re.match(RE_NUMBERIC, args[0]):
            raise InvalidMaxValidatorParameterError()

        self.max = int(args[0])
        self.code = 'max'
        self.message = MAX_MESSAGE.format(max=self.length)

    def __call__(self, value=None):
        if value is None or value == '':
            raise ValidationError(message=self.message, code=self.code)

        if len(value) > self.max:
            raise ValidationError(message=self.message, code=self.code)


class LengthValidator(RegexValidator):

    def __init__(self, args=None, **kwargs):
        super(LengthValidator, self).__init__(**kwargs)

        if not args or len(args) != 1:
            raise InvalidLengthValidatorParameterError()

        if not re.match(RE_NUMBERIC, args[0]):
            raise InvalidLengthValidatorParameterError()

        self.length = int(args[0])
        self.code = 'length'
        self.message = LENGTH_MESSAGE.format(length=self.length)

    def __call__(self, value=None):
        if value is None or value == '':
            raise ValidationError(message=self.message, code=self.code)

        if not len(value) == self.length:
            raise ValidationError(message=self.message, code=self.code)


class RangeValidator(RegexValidator):

    def __init__(self, args=None, **kwargs):
        super(RangeValidator, self).__init__(**kwargs)

        if not args or len(args) != 2:
            raise InvalidRangeValidatorParameterError()

        if not re.match(RE_NUMBERIC, args[0]) or not re.match(RE_NUMBERIC, args[1]):
            raise InvalidMinValidatorParameterError()

        self.min = int(args[0])
        self.max = int(args[1])

        if self.min > self.max:
            self.min, self.max = self.max, self.min

        self.code = 'range'
        self.message = RANGE_MESSAGE.format(min=self.min, max=self.max)

    def __call__(self, value=None):
        if value is None or value == '':
            raise ValidationError(self.message, code=self.code)

        value_length = len(value)

        if self.min == self.max:
            if not value_length == self.max:
                raise ValidationError(message=self.message, code=self.code)

        if not self.min > value_length or not self.max < value_length:
            raise ValidationError(message=self.message, code=self.code)


class AcceptedValidation(RegexValidator):

    def __init__(self, args, **kwargs):
        super(AcceptedValidation, self).__init__(**kwargs)

        if not args or len(args) != 1:
            raise InvalidAcceptedValidatorParameterError()

        self.accepted = args[0]
        self.code = 'accepted'
        self.message = ACCEPTED_MESSAGE

    def __call__(self, value=None):
        if value == 'yes' or value == 'on' or value == '1':
            pass
        else:
            raise ValidationError(message=self.message, code=self.code)


def min_validator_wrapper():
    return MinValidator


def max_validator_wrapper():
    return MaxValidator


def length_validator_wrapper():
    return LengthValidator


def range_validator_wrapper():
    return RangeValidator


def accepted_validator_wrapper():
    return AcceptedValidation

REQUIRED = RequiredValidator()
NUMERIC = NumericValidator()
MIN = min_validator_wrapper()
MAX = max_validator_wrapper()
REANGE = range_validator_wrapper()
LENGTH = length_validator_wrapper()
ACCEPTED = accepted_validator_wrapper()