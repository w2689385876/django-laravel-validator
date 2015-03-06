##django-laravel-validator

__1. what__

[django-laravel-validator](https://pypi.python.org/pypi/django-laravel-validator) is a [django](https://www.djangoproject.com/) third party plugin of the purpose to validate input data easily, the easily means easy to validate , and easy to custom error message, the most import is easy to extend, the project is inspired by the validation system of [Laravel](http://laravel.com/) , the most sexy php framework I ever use , she is sexy but she is also Fat, but i do not care fat. 

----------------------

__2. why__

I use [Django](https://www.djangoproject.com/) framework since last year, i built some small apps, yap, it is fast to code ,but hard to use and understand, expecially the FORM system of django, i found it hard to validate and add custom error message, in some way you should hack the code to  satisfied your logic, but in [laravel](http://laravel.com/), validate is more easy and helpful, so i copy the validate system of [Laravel](http://laravel.com/) to django.

______________________

__3. how__

Install:
	
    pip install django-laravel-validator
	

if you checkout from github or download the tarball
	
    python setup.py install

Usage:

you do not need to install the app to django's setting file.

    class RegistValidator(Validator):
        email = 'required|email'
    	password = 'required|min:8'
        password_confirm = 'required|min:8'
        captcha_0 = 'required'
        captcha_1 = 'required'

        def check(self):
            password = self.data.get('password')
            password_confirm = self.data.get('password_confirm')
            email = self.data.get('email')
            captcha_0 = self.data.get('captcha_0')
            captcha_1 = self.data.get('captcha_1')

            if not password == password_confirm:
                self.add_error(dict(pass_not_match=u'密码不匹配'))

            if User.objects.filter(email=email).exists():
                self.add_error(dict(user_exists=u'该用户已存在'))

            try:
                CaptchaStore.objects.get(response=captcha_1, hashkey=captcha_0, expiration__gt=get_safe_now()).delete()
            except CaptchaStore.DoesNotExist:
                self.add_error(dict(captcha_error=u'验证码错误'))
                self.error_list.get('captcha_1').update(dict(captcha_error=u'验证码错误'))

In your  views:

    error_message = {'email.required': u'邮箱地址不能为空'}
    validator = RegistValidator(request.POST, message=error_message)
    if validator.fails():
        # do what you want
    else:
        error = validator.errors()
	# then deal with errors

Rules:
    
    REQUIRED # email = 'required'
    NUMERIC # phone = 'numeric'
    MIN # password = 'min:8'
    MAX # email = 'max:16'
    RANGE # email = 'range:8,16'
    LENGTH # email = 'length:18'
    ACCEPTED # remember_me = 'accepted' , should be 'yes' 'on' or '1'
    ALPHA # username = 'ALPHA', should be alpha characters
    EMAIL # email = 'required|email'
    IP  # ipaddr = 'ip'  validate for ip
    BOOL # confirm = 'bool' , should be 'True', 'False', '0', '1'
    REGEX # complicated = 'regex:^[0-9A-Z]{10,20}$' , for validate a regex

And others:

i hate long and useless document, so just check the code for your purpose and fork it, and it just under my development

______________________

__4. contribute__

just make pull request or fork to your repos, and if you like, buy me a beer or a launch.