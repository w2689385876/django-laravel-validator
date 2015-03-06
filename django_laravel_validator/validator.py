# -*- coding:utf-8 -*-
# PROJECT_NAME : laravel_validator
# FILE_NAME    : 
# AUTHOR       : younger shen
from importlib import import_module
from django.core.exceptions import ValidationError
from .exceptions import InvalidValidateDataError, InvalidRuleNameError
from .utils import format_args_split, check_errors, error_message_generate
from .rules import WITH_PARAMETERS_VALIDATOR


class BaseValidator(type):
    """
        Metaclass for all validators
    """

    def __init__(cls, name, bases, dct):
        new_attrs = dict()
        error_list = dict()

        if name is not 'Validator':
            for k in dct:
                if k != '__module__' and k != '__main__':
                    pattern = dct.get(k, None)
                    if not callable(pattern):
                        new_attrs.update(**{k: pattern})
                        error_list.update(**{k: {}})

            setattr(cls, 'validate_data', new_attrs)
            setattr(cls, 'error_list', error_list)

        super(BaseValidator, cls).__init__(name, bases, dct)

    def __new__(mcs, name, bases, dct):
        return type.__new__(mcs, name, bases, dct)


class Validator(object):
    """
        base class for all Validator
    """
    __metaclass__ = BaseValidator

    def __init__(self, data, message=None, regex_list=None):
        self.data = data
        self.message = message
        self.regex_list = regex_list

    def fails(self):
        validate_data = getattr(self, 'validate_data')
        for k in validate_data:
            rules = validate_data.get(k, None)
            if not rules:
                raise InvalidValidateDataError()
            else:
                rules_list = rules.split('|')
                for rule in rules_list:
                    rule_origin = rule
                    rule = rule.split(':')[0]
                    if rule is None or rule == '':
                        raise InvalidRuleNameError(rule=rule)

                    rule_validator = import_module('.rules', package='django_laravel_validator')

                    try:
                        regex = getattr(rule_validator, rule.upper())
                    except AttributeError:
                        raise InvalidRuleNameError(rule=rule)

                    if rule.upper() in WITH_PARAMETERS_VALIDATOR:
                        rule_args = format_args_split(rule_origin)
                        regex = regex(rule_args)
                    try:
                        regex(self.data.get(k, None))

                    except ValidationError as e:
                        error_message = error_message_generate(k, rule, self.message, e)
                        error_dict = self.error_list.get(k)
                        error_dict.update({rule: error_message})
                        self.error_list.get(k).update(error_dict)

        check = getattr(self, 'check', None)
        if check and callable(check):
            check()

        return check_errors(self.error_list)

    def errors(self):
        return self.error_list
