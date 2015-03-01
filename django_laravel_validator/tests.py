# -*- coding:utf-8 -*-
# PROJECT_NAME : laravel_validator
# FILE_NAME    : 
# AUTHOR       : younger shen

#
#
#  vdr = Validator(request.POST,{'username':'required|min5|unique:users'})
#
#
#
#
from .validator import Validator


class UserValidator(Validator):
    ussername = 'required|min:6|unique:users'
    password = 'required|min8'

    def __init__(self, data, messages, regex_list):
        self.data = data
        # a regex must contains a code name and a regex
        # such as regex_list = [dict('love:2'=r'sdfsf'), dict()]
        self.regex_list = regex_list
        self.messages = messages

    def fails(self):
        errors = self.data
        return errors if errors else False

    def check(self):
        # do custom check
        # may return the same error as ValidationError with a message and a error code
        pass
    pass


