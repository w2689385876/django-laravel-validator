# -*- coding:utf-8 -*-
# PROJECT_NAME : laravel_validator
# FILE_NAME    : 
# AUTHOR       : younger shen

from django.core.validators import RegexValidator
from .utils import min_regex_builder
from .regex import RE_REQUIRED
from .regex import RE_NUMBERIC_STR

WITH_PARAMETERS_VALIDATOR = ['MIN', 'MAX', 'RANGE']

REQUIRED = RegexValidator(regex=RE_REQUIRED, message='it is required', code='required')
NUMERIC_STR = RegexValidator(regex=RE_NUMBERIC_STR, message='it is must be numeric', code='numeric')
MIN = min_regex_builder