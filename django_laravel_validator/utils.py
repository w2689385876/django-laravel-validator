# -*- coding:utf-8 -*-
# PROJECT_NAME : laravel_validator
# FILE_NAME    : 
# AUTHOR       : younger shen


def format_args_split(format_str):
    if ':' in format_str:
        args = format_str.split(':')[1].split(',')
        return args
    else:
        return None


def check_errors(error_list):

    for key in error_list:
        value = error_list.get(key)
        if len(value.keys()) > 0:
            return False
    return True