#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2016/12/28.
import random
from argeweb import Controller, scaffold, route_menu, Fields, route_with
from argeweb.components.pagination import Pagination
from argeweb.components.search import Search


class PageTracker(Controller):
    class Meta:
        components = (scaffold.Scaffolding, Pagination, Search)
        pagination_limit = 10

    class Scaffold:
        display_in_list = ('title', 'image', 'is_enable', 'category')
        hidden_in_form = ['name']

    @route_menu(list_name=u'backend', text=u'頁面追縱', sort=9961, group=u'系統設定', need_hr=True)
    def admin_list(self):
        return scaffold.list(self)