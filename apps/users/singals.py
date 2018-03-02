__author__ = 'beimenchuixue'
__blog__ = 'http://www.cnblogs.com/2bjiujiu/'
__date__ = '2018/3/2 10:02'

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth import get_user_model
UserProfile = get_user_model()


# receiver是接收信号量装饰器, past_save是信号量, sender指定表
@receiver(post_save, sender=UserProfile)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        # 判断是否新建用户，如果新建则把用户的明文密码置为加密
        password = instance.password
        instance.set_password(password)
        instance.save()