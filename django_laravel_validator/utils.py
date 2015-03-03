# -*- coding:utf-8 -*-
# PROJECT_NAME : laravel_validator
# FILE_NAME    : 
# AUTHOR       : younger shen

import re
from string import Template
from django.core.validators import RegexValidator
from .exceptions import InvalidMinValidatorParameterError
from .regex import RE_NUMBERIC_STR
from .regex import RE_MIN


def format_args_split(format_str):
    if ':' in format_str:
        args = format_str.split(':')[1].split(',')
        return args
    else:
        return None


def regex_builder(pattern, kwargs):
    return Template(pattern).substitute(**kwargs)


def min_regex_builder(args):
    kwargs = dict(start=args[0])
    start = kwargs.get('start', None)

    if start is None:
        raise InvalidMinValidatorParameterError()

    if re.match(RE_NUMBERIC_STR, start) is None:
        raise InvalidMinValidatorParameterError()

    return RegexValidator(regex=regex_builder(RE_MIN, kwargs), message='input is too short', code='min')

if __name__ == '__main__':
    reg = min_regex_builder(dict(start=3))
    print format_args_split('required:1')