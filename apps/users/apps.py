from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    verbose_name = '用户注册'

    def ready(self):
        """userApp启动信号量"""
        import users.singals
