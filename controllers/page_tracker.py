#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2016/12/28.
from argeweb import Controller, scaffold, route_menu


class PageTracker(Controller):
    class Scaffold:
        display_in_list = ['title', 'image', 'is_enable', 'category']

    @route_menu(list_name=u'system', group=u'系統設定', text=u'頁面追縱', sort=9999, icon=u'settings')
    def admin_list(self):
        return scaffold.list(self)