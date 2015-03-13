# -*- coding:utf-8 -*-
# PROJECT_NAME : laravel_validator
# FILE_NAME    : 
# AUTHOR       : younger shen
from importlib import import_module
import re
from django.core.exceptions import ValidationError, FieldError
from django.core.validators import RegexValidator
from .regex import RE_NUMBERIC
from .regex import RE_ALPHA
from .regex import RE_EMAIL
from .regex import RE_IP_ADDRESS
from .exceptions import InvalidMinValidatorParameterError
from .exceptions import InvalidMaxValidatorParameterError
from .exceptions import InvalidRangeValidatorParameterError
from .exceptions import InvalidLengthValidatorParameterError
from .exceptions import InvalidRegexValidatorParameterError
from .exceptions import InvalidMatchValidatorParameterError
from .exceptions import InvalidUniqueValidatorParameterError
from .messages import REQUIRED_MESSAGE
from .messages import NUMERIC_MESSAGE
from .messages import MIN_MESSAGE
from .messages import MAX_MESSAGE
from .messages import RANGE_MESSAGE
from .messages import LENGTH_MESSAGE
from .messages import ACCEPTED_MESSAGE
from .messages import ALPHA_MESSAGE
from .messages import EMAIL_MESSAGE
from .messages import IP_ADDRESS_MESSAGE
from .messages import BOOLEAN_MESSAGE
from .messages import REGEX_MESSAGE
from .messages import MATCH_MESSAGE
from .messages import UNIQUE_MESSAGE
from .messages import UNIQUE_UNKNOW_APP_NAME
from .messages import UNIQUE_UNKNOW_MODEL_NAME
from .messages import UNIQUE_UNKNOW_MODEL_FIELD
WITH_PARAMETERS_VALIDATOR = ['MIN', 'MAX', 'RANGE', 'LENGTH', 'REGEX', 'MATCH', 'UNIQUE']


class BaseValidator(RegexValidator):
    pass


class RequiredValidator(BaseValidator):

    def __init__(self, **kwargs):
        super(RequiredValidator, self).__init__(**kwargs)
        self.code = 'required'
        self.message = REQUIRED_MESSAGE

    def __call__(self, value=None):
        if value is None or value == '':
            raise ValidationError(message=self.message, code=self.code)

        if value and value.strip() == '':
            raise ValidationError(message=self.message, code=self.code)


class NumericValidator(BaseValidator):

    def __init__(self, **kwargs):
        super(NumericValidator, self).__init__(**kwargs)
        self.code = 'numeric'
        self.message = NUMERIC_MESSAGE

    def __call__(self, value=None):
        if not re.match(RE_NUMBERIC, value):
            raise ValidationError(message=self.message, code=self.code)


class MinValidator(BaseValidator):

    def __init__(self, args=None, **kwargs):
        super(MinValidator, self).__init__(**kwargs)

        if not args or len(args) != 1 or args[0] is None or args[0] == '':
            raise InvalidMinValidatorParameterError()

        if not re.match(RE_NUMBERIC, args[0]):
            raise InvalidMinValidatorParameterError()

        self.min = int(args[0])
        self.code = 'min'
        self.message = MIN_MESSAGE.format(min=self.min)

    def __call__(self, value=None):

        if value is None or value == '':
            raise ValidationError(message=self.message, code=self.code)

        if len(value) < self.min:
            raise ValidationError(message=self.message, code=self.code)


class MaxValidator(BaseValidator):

    def __init__(self, args=None, **kwargs):
        super(MaxValidator, self).__init__(**kwargs)

        if not args or len(args) != 1 or args[0] is None or args[0] == '':
            raise InvalidMaxValidatorParameterError()

        if not re.match(RE_NUMBERIC, args[0]):
            raise InvalidMaxValidatorParameterError()

        self.max = int(args[0])
        self.code = 'max'
        self.message = MAX_MESSAGE.format(max=self.max)

    def __call__(self, value=None):
        if value is None or value == '':
            raise ValidationError(message=self.message, code=self.code)

        if len(value) > self.max:
            raise ValidationError(message=self.message, code=self.code)


class LengthValidator(BaseValidator):

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


class RangeValidator(BaseValidator):

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

        if self.min > value_length or self.max < value_length:
            raise ValidationError(message=self.message, code=self.code)


class AcceptedValidator(BaseValidator):

    def __init__(self, **kwargs):
        super(AcceptedValidator, self).__init__(**kwargs)

        self.code = 'accepted'
        self.message = ACCEPTED_MESSAGE

    def __call__(self, value=None):
        if value == 'yes' or value == 'on' or value == '1':
            pass
        else:
            raise ValidationError(message=self.message, code=self.code)


class AlphaValidator(BaseValidator):

    def __init__(self, **kwargs):
        super(AlphaValidator, self).__init__(**kwargs)

        self.code = 'alpha'
        self.message = ALPHA_MESSAGE

    def __call__(self, value=None):

        if not re.match(RE_ALPHA, value):
            raise ValidationError(message=self.message, code=self.code)


class EmailValidator(BaseValidator):

    def __init__(self, **kwargs):
        super(EmailValidator, self).__init__(**kwargs)
        self.code = 'email'
        self.message = EMAIL_MESSAGE

    def __call__(self, value=None):
        if not re.match(RE_EMAIL, value):
            raise ValidationError(message=self.message, code=self.code)


class IPAddressValidator(BaseValidator):

    def __init__(self, **kwargs):
        super(IPAddressValidator, self).__init__(**kwargs)
        self.code = 'ip'
        self.message = IP_ADDRESS_MESSAGE

    def __call__(self, value=None):
        if not re.match(RE_IP_ADDRESS, value):
            raise ValidationError(message=self.message, code=self.code)


class BooleanValidator(BaseValidator):

    def __init__(self, **kwargs):
        super(BooleanValidator, self).__init__(**kwargs)
        self.code = 'boolean'
        self.message = BOOLEAN_MESSAGE

    def __call__(self, value=None):
        if value == 1 or value == 0 or value == '1' or value == '0' or value == 'True' or value is True or value == 'False' or value is False:
            pass
        else:
            raise ValidationError(message=self.message, code=self.code)


class RegexValidator(BaseValidator):

    def __init__(self, args, **kwargs):
        super(RegexValidator, self).__init__(**kwargs)
        self.code = 'regex'

        if not args:
            raise InvalidRegexValidatorParameterError()
        regex = ''
        for s in args:
            regex += str(s)
            regex += ','

        self.regex = regex[:-1]
        self.message = REGEX_MESSAGE.format(regex=self.regex)

    def __call__(self, value=None):
        if not re.match(self.regex, value):
            raise ValidationError(message=self.message, code=self.code)


class MatchValidator(BaseValidator):

    def __init__(self, args, **kwargs):
        super(MatchValidator, self).__init__(**kwargs)
        self.code = 'match'

        if not args or len(args) != 1:
            raise InvalidMatchValidatorParameterError()

        self.match = args[0]
        self.message = MATCH_MESSAGE.format(match=self.match)

    def __call__(self, value=None):
        instance = getattr(self, 'validator_instance')
        data = getattr(instance, 'data', None)
        match_value = data.get(self.match, None)

        if not match_value:
            raise InvalidMatchValidatorParameterError()
        else:
            if not value == match_value:
                raise ValidationError(message=self.message, code=self.code)


class UniqueValidator(BaseValidator):

    def __init__(self, args, **kwargs):
        super(UniqueValidator, self).__init__(**kwargs)
        self.code = 'unique'
        if not args or len(args) != 2:
            raise InvalidUniqueValidatorParameterError()

        if args[0] == '' or args[1] == '':
            raise InvalidUniqueValidatorParameterError()

        temp = args[0].split('.')
        temp.insert(1, 'models')
        module_name = '.'.join(temp[:2])
        try:
            module = import_module(module_name)
        except ImportError:
            message = UNIQUE_UNKNOW_APP_NAME.format(appname=temp[0])
            raise InvalidUniqueValidatorParameterError(message)

        klass = getattr(module, temp[2], None)
        if not klass:
            message = UNIQUE_UNKNOW_MODEL_NAME.format(appname=temp[0], modelname=temp[2])
            raise InvalidUniqueValidatorParameterError(message)
        self.klass = klass
        self.field = args[1]
        self.message = UNIQUE_MESSAGE.format(field=self.field, model=temp[2])

    def __call__(self, value=None):
        try:
            self.klass.objects.get(**{self.field: value})
        except FieldError:
            message = UNIQUE_UNKNOW_MODEL_FIELD.format(fieldname=self.field)
            raise InvalidUniqueValidatorParameterError(message=message)
        except self.klass.DoesNotExist:
            return
        else:
            raise ValidationError(code=self.code, message=self.message)


REQUIRED = RequiredValidator
NUMERIC = NumericValidator
MIN = MinValidator
MAX = MaxValidator
RANGE = RangeValidator
LENGTH = LengthValidator
ACCEPTED = AcceptedValidator
ALPHA = AlphaValidator
EMAIL = EmailValidator
IP = IPAddressValidator
BOOL = BooleanValidator
REGEX = RegexValidator
MATCH = MatchValidator
UNIQUE = UniqueValidator