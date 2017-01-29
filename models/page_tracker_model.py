#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2016/12/28.

from argeweb import BasicModel
from argeweb import Fields


def get_page_tracker_code(**kwargs):
    return '<h1> code is here</h1>'


class PageTrackerModel(BasicModel):
    name = Fields.StringProperty(verbose_name=u'頁面名稱(網址)')
    title = Fields.StringProperty(verbose_name=u'標題')
    content = Fields.RichTextProperty(verbose_name=u'內容')
    image = Fields.ImageProperty(verbose_name=u'圖片')
    is_enable = Fields.BooleanProperty(default=True, verbose_name=u'顯示於前台')

    @classmethod
    def all_enable(cls, category=None, *args, **kwargs):
        return cls.query(cls.is_enable==True).order(-cls.sort)

    @classmethod
    def insert(cls, name, title, content=u'', is_enable=True, image=u''):
        item = cls.find_by_name(name)
        if item is not None:
            return
        if content == u'':
            content = title
        item = cls()
        item.name = name
        item.title = title
        item.content = content
        item.is_enable = is_enable
        item.image = image
        item.put()
        return item

