# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428369221.950718
_enable_loop = True
_template_filename = '/Users/BlakeWoodward/CoHerFoun/homepage/templates/login.html'
_template_uri = 'login.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'header', 'title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def header():
            return render_header(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n\t<html>\n\t\t<body>\n\t\t<br><br><br><br>\n\t\t<div class="everything text-center">\n\t\t<img class="displayed" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/CHF_Logo.png" alt="Flag" width="400px"><br>\n\n\t\t\t<form method=\'POST\'>\n\t\t\t\t<table>\n\t\t\t\t')
        __M_writer(str(form))
        __M_writer("\n\t\t\t\t</table><br>\n\t\t\t\t<input type='Submit' />\n\t\t\t</form>\n\t\t<a href ='/account/forgot'>Forgot your password?</a>\n\t\t</div>\n\t\t</body>\n\t</html>\n\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        __M_writer = context.writer()
        __M_writer('\n\tContact the Colonial Heritage Foundation\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\n\tLogin\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/BlakeWoodward/CoHerFoun/homepage/templates/login.html", "uri": "login.html", "source_encoding": "ascii", "line_map": {"96": 3, "68": 7, "69": 13, "70": 13, "71": 17, "72": 17, "45": 5, "78": 28, "40": 1, "50": 26, "84": 28, "90": 3, "27": 0, "60": 7, "102": 96}}
__M_END_METADATA
"""
