# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428368951.217889
_enable_loop = True
_template_filename = '/Users/BlakeWoodward/CoHerFoun/account/templates/forgot.html'
_template_uri = 'forgot.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'title']


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
        def title():
            return render_title(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        hash = context.get('hash', UNDEFINED)
        userid = context.get('userid', UNDEFINED)
        status = context.get('status', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\n\n\n')
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
        userid = context.get('userid', UNDEFINED)
        hash = context.get('hash', UNDEFINED)
        form = context.get('form', UNDEFINED)
        status = context.get('status', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n\n\n<script>\nfunction myFunction() {\n    console.log("An email has been sent, please check your inbox!");\n}\n</script>\n<br><br><br>\n\n\n')
        if status == 'sent':
            __M_writer('\t<h2> An email has been sent to your address</h2>\n\n\n\n\n\n')
        elif status == 'new_password':
            __M_writer("\t<h2> You have gotten to the change your password page</h2>\n\t\t<form method='POST' id='passwordForm' action='/account/forgot.changePW/")
            __M_writer(str(userid))
            __M_writer('/')
            __M_writer(str(hash))
            __M_writer("' >\n\t\t<table>\n\t\t\t\t\t")
            __M_writer(str(form))
            __M_writer('\n\n\t\t</table>\n\t\t<input type="submit" />\n\t</form>\t\t\n\n\n\n\n\n\n\n')
        elif status =='bad_hash':
            __M_writer('\t<h2> Bad URL</h2>\n\n')
        elif status == 'bad_user':
            __M_writer('\t<h2> User does not exist</h2>\n\n')
        else:
            __M_writer('\t<div class="text-center">\n\t\t<h1>Forgot your password?<small> No Problem</small></h1>\n\n\t\t<p>Enter your username and we will send you a link to reset your password.</p>\n\n\t\t\t\t<form method=\'POST\' action=\'/account/forgot.reset/\'> \n\t\t\t\t\t')
            __M_writer(str(form))
            __M_writer('\n\t\t\t\t\t<br>\n\t\t\t\t\t<div class="button"><br>\n\t\t\t\t\t<input type=\'Submit\' onclick="myFunction()"/>\n\t\t\t\t\t</div>\n\t\t\t\t</form>\t\n\t</div>\n')
        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\n\tForgot My Password\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/BlakeWoodward/CoHerFoun/account/templates/forgot.html", "uri": "forgot.html", "source_encoding": "ascii", "line_map": {"65": 7, "66": 19, "67": 20, "68": 26, "69": 27, "70": 28, "71": 28, "72": 28, "73": 28, "74": 30, "75": 30, "76": 42, "77": 43, "78": 45, "79": 46, "80": 48, "81": 49, "82": 55, "83": 55, "84": 63, "90": 2, "27": 0, "96": 2, "102": 96, "40": 1, "45": 4, "55": 7}}
__M_END_METADATA
"""
