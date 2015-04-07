# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1421202842.828395
_enable_loop = True
_template_filename = 'C:\\Python34\\Projects\\CHF\\homepage\\scripts/index.jsm'
_template_uri = 'index.jsm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer("$(function() {\r\n  // update the time every n seconds\r\n  window.setInterval(function() {\r\n    $('.browser-time').text('The current browser time is ' + new Date());\r\n  }, ")
        __M_writer(str( request.urlparams[1] ))
        __M_writer(");\r\n\r\n  // update server time button\r\n  $('#server-time-button').click(function() {\r\n    $('.server-time').load('/homepage/index.gettime');\r\n  });\r\n});")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "index.jsm", "filename": "C:\\Python34\\Projects\\CHF\\homepage\\scripts/index.jsm", "line_map": {"16": 0, "24": 5, "30": 24, "22": 1, "23": 5}, "source_encoding": "ascii"}
__M_END_METADATA
"""
