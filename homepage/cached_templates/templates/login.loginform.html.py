# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428368668.691645
_enable_loop = True
_template_filename = '/Users/BlakeWoodward/CoHerFoun/homepage/templates/login.loginform.html'
_template_uri = 'login.loginform.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


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
    return runtime._inherit_from(context, '/homepage/templates/base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n<img class="displayed text-center" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/CHF_Logo.png" alt="Flag" width="400px">\n\t<form method=\'POST\' id=\'loginform\' action=\'/homepage/login.loginform/\' >\n\t\t<table class="text-center">\n\t\t\t')
        __M_writer(str(form))
        __M_writer('\n\t\t</table>\n\t\t<input type="submit" />\n\t</form>\t\t<br>\n\t<p><a href =\'/account/forgot\'>Forgot your password?</a></p>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/BlakeWoodward/CoHerFoun/homepage/templates/login.loginform.html", "source_encoding": "ascii", "uri": "login.loginform.html", "line_map": {"64": 58, "36": 1, "54": 3, "55": 4, "56": 4, "57": 7, "58": 7, "27": 0, "46": 3}}
__M_END_METADATA
"""
