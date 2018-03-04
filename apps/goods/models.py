from datetime import datetime

from django.db import models

from DjangoUeditor.models import UEditorField


class GoodsCategory(models.Model):
    """
    商品类别
    """
    CATEGORY_TYPE = (
        (1, "一级类目"),
        (2, "二级类目"),
        (3, "三级类目"),
    )

    # help_text 是用户后台 description 提示信息
    name = models.CharField(max_length=50, verbose_name='类别名', help_text='类别名')
    code = models.CharField(max_length=30, verbose_name='类别code', help_text='类别code')
    desc = models.CharField(max_length=200, verbose_name='类别描述', help_text='类别描述')
    category_type = models.IntegerField(choices=CATEGORY_TYPE,  null=True, blank=True,
                                        verbose_name='类目级别', help_text='类目级别')
    parent_category = models.ForeignKey('self', null=True, related_name='sub_cat', blank=True,
                                        verbose_name='父类目级别', help_text='父类目级别')
    is_tab = models.BooleanField(default=False, verbose_name='是否导航', help_text='是否导航')

    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间', help_text='添加时间')

    class Meta:
        verbose_name = '商品类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsCategoryBrand(models.Model):
    """
    品牌
    """
    category = models.ForeignKey(GoodsCategory, related_name='brands',
                                null=True, blank=True, verbose_name='商品类目', help_text='商品类目')
    name = models.CharField(max_length=30, default='', verbose_name='品牌名', help_text='品牌名')
    desc = models.TextField(max_length=200, default='', verbose_name='品牌描叙',  help_text='品牌描叙')
    image = models.ImageField(max_length=200, upload_to='brands/', verbose_name='品牌logo', help_text='品牌logo')

    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间', help_text='添加时间')

    class Meta:
        verbose_name = '品牌'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Goods(models.Model):
    """
    商品
    """
    category = models.ForeignKey(GoodsCategory, null=True, blank=True, verbose_name='商品类目', help_text='商品类目')
    goods_sn = models.CharField(max_length=20,  verbose_name='商品唯一货号', help_text='商品唯一货号')
    name = models.CharField(max_length=50, verbose_name='商品名', help_text='商品名')
    goods_brief = models.TextField(max_length=500, verbose_name='商品简单描叙')
    goods_desc = UEditorField(verbose_name='商品详情', imagePath='goods/images/', width=1000,
                             height=300, filePath='goods/files/', null=True, blank=True, help_text='商品详情')
    goods_front_image = models.ImageField(max_length=50, upload_to='goods/images/',
                                          verbose_name='商品封面', help_text='商品封面')
    # 统计
    goods_num = models.IntegerField(default=0, verbose_name='商品库存量', help_text='商品库存量')
    market_price = models.IntegerField(default=0, verbose_name='市场价格', help_text='市场价格')
    shop_price = models.FloatField(default=0, verbose_name="本店价格", help_text='本店价格')
    ship_free = models.BooleanField(default=False, verbose_name='是否包邮', help_text='是否包邮')
    is_new = models.BooleanField(default=False, verbose_name='是否新品', help_text='是否新品')
    is_hot = models.BooleanField(default=False, verbose_name='是否热卖', help_text='是否热卖')
    sold_num = models.IntegerField(default=0, verbose_name='已出售数量', help_text='已出售数量')
    fav_num = models.IntegerField(default=0, verbose_name='收藏数量', help_text='收藏数量')
    click_num = models.IntegerField(default=0, verbose_name='点击量', help_text='点击量')

    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间', help_text='添加时间')

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.name


class IndexAd(models.Model):
    """
    首页商品类别广告
    """
    category = models.ForeignKey(GoodsCategory, related_name='category', null=True, blank=True, verbose_name="商品类目", help_text='商品类目')
    goods = models.ForeignKey(Goods, related_name='商品', help_text='商品')

    class Meta:
        verbose_name = '首页商品类别广告'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class GoodsImage(models.Model):
    """商品图片"""
    goods = models.ForeignKey(Goods, related_name='image', verbose_name='商品名', help_text='商品名')
    image = models.ImageField(max_length=100, upload_to='goods/', verbose_name='图片', help_text='图片')
    image_url = models.URLField(max_length=300, null=True, blank=True, verbose_name='图片地址', help_text='图片地址')

    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间', help_text='添加时间')

    class Meta:
        verbose_name = '商品图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class Banner(models.Model):
    """
    商品轮播图
    """
    goods = models.ForeignKey(Goods, verbose_name='商品名', help_text='商品名')
    image = models.ImageField(max_length=100, upload_to='banner/', verbose_name='轮播图', help_text='轮播图')
    index = models.ImageField(default=0, verbose_name='轮播顺序', help_text='轮播顺序')

    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间', help_text='添加时间')

    class Meta:
        verbose_name = '轮播商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class HotSearchWords(models.Model):
    """
    热搜词
    """
    keywords = models.CharField(default="", max_length=20, verbose_name="热搜词", help_text='热搜词')
    index = models.IntegerField(default=0, verbose_name="排序", help_text='排序')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text='添加时间')

    class Meta:
        verbose_name = '热搜词'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.keywords
