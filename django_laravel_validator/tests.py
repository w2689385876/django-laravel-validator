# -*- coding:utf-8 -*-
# PROJECT_NAME : laravel_validator
# FILE_NAME    : 
# AUTHOR       : younger shen

from django_laravel_validator.exceptions import InvalidMinValidatorParameterError
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
    username = 'required|min:8|numeric'
    password = 'required|min:8|numeric'

    def check(self):
        username = self.data.get('username')
        password = self.data.get('password')
        print ' i am checking '


class TestValidator3(Validator):

    username = 'required|min:sdf|numeric|sss'
    password = 'required|min:sss|numeric'


class TestValidator4(Validator):
    username = 'required|min:8|numeric'
    password = 'required|min:2|numeric'


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

    data = dict(username='', password='wwwsf')
    validator = TestValidator2(data)
    ret = validator.fails()
    error_list = validator.errors()

    assert ret is False
    assert error_list.get('username').get('required') == 'it is required'
    assert error_list.get('username').get('min') == 'it should be longger than 8'
    assert error_list.get('username').get('numeric') == 'it should be numeric string'
    assert error_list.get('password').get('min') == 'it should be longger than 8'
    assert error_list.get('password').get('numeric') == 'it should be numeric string'


def test_validator3():
    data = dict(username='tinker', password='i am tinker')
    validator = TestValidator3(data)
    try:
        ret = validator.fails()
    except InvalidMinValidatorParameterError as e:
        pass


def test_validator4():
    data = dict(username='', password='')
    message = {'username.required': 'haha', 'password.required': 'heihei', 'username.min': 'min'}

    validator = TestValidator4(data, message=message)

    ret = validator.fails()
    error_list = validator.errors()

    assert ret is False
    assert error_list.get('username').get('required') == 'haha'
    assert error_list.get('password').get('required') == 'heihei'
    assert error_list.get('username').get('min') == 'min'
    assert error_list.get('username').get('numeric') == 'it should be numeric string'