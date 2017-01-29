#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2016/12/28.

from argeweb import ViewDatastore, ViewFunction
from models.page_tracker_model import PageTrackerModel, get_page_tracker_code

ViewFunction.register(get_page_tracker_code)
ViewDatastore.register('page_tracker', PageTrackerModel.find_by_name)

plugins_helper = {
    'title': u'頁面追縱',
    'desc': u'頁面追縱',
    'controllers': {
        'page_tracker': {
            'group': u'頁面追縱',
            'actions': [
                {'action': 'list', 'name': u'頁面追縱'},
                {'action': 'add', 'name': u'新增頁面追縱'},
                {'action': 'edit', 'name': u'編輯頁面追縱'},
                {'action': 'view', 'name': u'檢視頁面追縱'},
                {'action': 'delete', 'name': u'刪除頁面追縱'},
                {'action': 'plugins_check', 'name': u'啟用停用模組'},
            ]
        }
    }
}