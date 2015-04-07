# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423189240.717882
_enable_loop = True
_template_filename = 'C:\\Python34\\Projects\\CHF\\homepage\\templates/users.html'
_template_uri = 'users.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'title', 'header']


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
        allusers = context.get('allusers', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n')
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
        allusers = context.get('allusers', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\t<html>\r\n\t\t<body>\r\n\t\t\t<h2> User Accounts</h2>\r\n\r\n\t\t\t<div class = "clearfix"></div>\r\n\r\n\t\t\t<div class = "text-right">\r\n\t\t\t\t<a href="/homepage/users.create/" class ="btn btn-warning">\r\n\t\t\t\t Create New User</a>\r\n\t\t\t</div>\r\n\t\t\t<br>\r\n\t\t\t<table class="table table-striped table-bordered">\r\n\t\t\t\t<tr>\r\n\t\t\t\t\t<th>ID</th>\r\n\t\t\t\t\t<th>Username</th>\r\n\t\t\t\t\t<th>First Name</th>\r\n\t\t\t\t\t<th>Last Name</th>\r\n\t\t\t\t\t<th>Email</th>\r\n\t\t\t\t\t<th>Actions</th>\r\n\r\n\t\t\t\t</tr>\t\t\t\r\n')
        for user in allusers:
            __M_writer('\r\n\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(user.id))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(user.username))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(user.first_name))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(user.last_name))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(user.email))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td><a href="/homepage/users.edit/')
            __M_writer(str(user.id))
            __M_writer('/">Edit</a>\r\n\t\t\t\t\t\t|\r\n\t\t\t\t\t\t <a href=\'/homepage/users.delete/')
            __M_writer(str(user.id))
            __M_writer("/'>Delete</a></td>\r\n\r\n\t\t\t\t\t</tr>\r\n")
        __M_writer('\r\n\t\t\t</table>\r\n\r\n\t</html>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n\tUsers\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        __M_writer = context.writer()
        __M_writer('\r\n\tContact the Colonial Heritage Foundation\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"66": 7, "67": 30, "68": 31, "69": 33, "70": 33, "71": 34, "72": 34, "73": 35, "74": 35, "75": 36, "76": 36, "77": 37, "78": 37, "79": 38, "80": 38, "81": 40, "82": 40, "83": 44, "89": 3, "27": 0, "95": 3, "113": 107, "101": 51, "39": 1, "107": 51, "44": 5, "49": 49, "59": 7}, "uri": "users.html", "source_encoding": "ascii", "filename": "C:\\Python34\\Projects\\CHF\\homepage\\templates/users.html"}
__M_END_METADATA
"""
