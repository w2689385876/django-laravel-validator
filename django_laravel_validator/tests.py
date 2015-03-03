# -*- coding:utf-8 -*-
# PROJECT_NAME : laravel_validator
# FILE_NAME    : 
# AUTHOR       : younger shen

#
# vdr = Validator(request.POST,{'username':'required|min5|unique:users'})
#
# from .validator import Validator
#
# class UserValidator(Validator):
#     ussername = 'required|min:6|unique:users'
#     password = 'required|min8'
#
#     def __init__(self, data, messages, regex_list):
#         self.data = data
#         a regex must contains a code name and a regex
#         such as regex_list = [dict('love:2'=r'sdfsf'), dict()]
#         self.regex_list = regex_list
#         self.messages = messages
#
#         def fails(self):
#         errors = self.data
#         return errors if errors else False
#
#     def check(self):
#     do custom check
#     may return the same error as ValidationError with a message and a error code
#     pass
from django_laravel_validator.utils import check_errors
from django_laravel_validator.validator import Validator


class TestValidator1(Validator):
    username = 'required'
    password = 'required'

    def check(self):
        username = self.data.get('username')
        password = self.data.get('password')

        if username != 'youngershen':
            self.error_list.get('username').update(dict(wrong_user=u'you got a wrong user'))

        if password != '123456':
            self.error_list.get('password').update(dict(wrong_pass=u'you got a wrong pass'))


class TestValidator2(Validator):
    username = 'required|min:8'
    password = 'required|min:8|numeric'

    def check(self):
        username = self.data.get('username')
        password = self.data.get('password')


def test_validator():
    data = dict(username='youngershen', password='123456')
    validator = TestValidator1(data)
    ret = validator.fails()
    error_list = validator.errors()

    assert ret is True
    assert check_errors(error_list)

    data = dict(username='123', password='123')

    validator = TestValidator1(data)
    ret = validator.fails()
    error_list = validator.errors()

    assert ret is False
    assert check_errors(error_list) is False


def test_validator2():
    data = dict(username='123456789', password='123456789')
    validator = TestValidator2(data)
    ret = validator.fails()
    error_list = validator.errors()

    assert ret is True
    assert check_errors(error_list) is True

    data = dict(username='123456', password='wwwsf')
    validator = TestValidator2(data)
    ret = validator.fails()
    error_list = validator.errors()

    assert ret is False
    assert error_list.get('username').get('min') == 'it should be longger than 8'
    print error_list
    assert error_list.get('password').get('min') == 'it should be longger than 8'
    assert error_list.get('password').get('numeric') == 'it should be numeric string'



