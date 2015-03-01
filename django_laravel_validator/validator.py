# -*- coding:utf-8 -*-
# PROJECT_NAME : laravel_validator
# FILE_NAME    : 
# AUTHOR       : younger shen
from importlib import import_module
from django.core.exceptions import ValidationError
from django_laravel_validator.exceptions import InvalidValidateDataError


class BaseValidator(type):
    """
        Metaclass for all validators
    """

    def __init__(cls, name, bases, dct):
        new_attrs = dict()
        if name is not 'Validator':
            for k in dct:
                if k != '__module__' and k != '__main__':
                    new_attrs.update(**{k: dct.get(k, None)})
            setattr(cls, 'validate_data', new_attrs)

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
        self.error_list = dict()

    def fails(self):
        validate_data = getattr(self, 'validate_data')
        for k in validate_data:
            rules = validate_data.get(k, None)
            if not rules:
                raise InvalidValidateDataError()
            else:
                rules_list = rules.split('|')
                for rule in rules_list:
                    rule_validator = import_module('.rules', package='django_laravel_validator')
                    regex_validator = getattr(rule_validator, rule.upper())
                    try:
                        regex_validator('')
                    except ValidationError as e:
                        if self.error_list.get(k, None):
                            self.error_list.get(k).update(**{rule: str(e)})
                        else:
                            self.error_list.update(**{k: {rule: str(e)}})

        if len(self.error_list.keys()) > 0:
            return False
        else:
            return True

    def errors(self):
        return self.error_list


if __name__ == '__main__':
    class Data(Validator):
        name = 'required'
        age = 'required'

    a = Data('')
    if a.fails():
        pass
    else:
        print a.errors()
