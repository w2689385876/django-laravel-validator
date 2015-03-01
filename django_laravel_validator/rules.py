# -*- coding:utf-8 -*-
# PROJECT_NAME : laravel_validator
# FILE_NAME    : 
# AUTHOR       : younger shen

from django.core.validators import RegexValidator


REQUIRED = RegexValidator(regex=r'[0-9]+', message='it is required', code='required')