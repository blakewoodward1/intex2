# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427949096.589134
_enable_loop = True
_template_filename = 'C:\\Python34\\Projects\\CHF\\account\\templates/passwordResetForm.html'
_template_uri = '/passwordResetForm.html'
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
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer("\r\n   \r\n\t<form method='POST' id='passwordForm' action='/account/forgot.changePW/' >\r\n\t\t<table>\r\n\t\t\t")
        __M_writer(str(form))
        __M_writer('\r\n\t\t</table>\r\n\t\t<input type="submit" />\r\n\t</form>\t\t\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "C:\\Python34\\Projects\\CHF\\account\\templates/passwordResetForm.html", "line_map": {"35": 1, "52": 3, "53": 7, "54": 7, "27": 0, "60": 54, "45": 3}, "uri": "/passwordResetForm.html"}
__M_END_METADATA
"""
