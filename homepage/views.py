# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


def index_page(request, *args, **kwargs):
    response = HttpResponse(content='NOW IT IS ALL OK')
    return response
