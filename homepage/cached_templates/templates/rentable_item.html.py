# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428195607.203475
_enable_loop = True
_template_filename = 'C:\\Python34\\Projects\\CHF\\homepage\\templates/rentable_item.html'
_template_uri = 'rentable_item.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['title', 'header', 'content']


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
        def title():
            return render_title(context._locals(__M_locals))
        all_item = context.get('all_item', UNDEFINED)
        def header():
            return render_header(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
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


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n\tRentable Items\r\n')
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        all_item = context.get('all_item', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\t<html>\r\n\t\t<body>\r\n\t\t\t<h2> Rentable Items</h2>\r\n\t\t\t<div class = "text-right">\r\n\t\t\t\t<a href="/homepage/rentable_item.create/" class ="btn btn-warning">\r\n\t\t\t\t Create New Rentable Item</a>\r\n\t\t\t</div>\r\n\t\t\t<br>\r\n\t\t\t<table class="table table-striped table-bordered">\r\n\t\t\t\t<tr>\r\n\t\t\t\t\t<th>ID</th>\r\n\t\t\t\t\t<th>Name</th>\r\n\t\t\t\t\t<th>Condition</th>\r\n\t\t\t\t\t<th>New Damage</th>\r\n\t\t\t\t\t<th>Damage Fee</th>\r\n\t\t\t\t\t<th>Due Date</th>\r\n\t\t\t\t\t<th>Late Fee</th>\t\r\n\t\t\t\t\t<th>Description</th>\r\n\t\t\t\t\t<th>Actions</th>\r\n\r\n\r\n\t\t\t\t</tr>\t\t\t\r\n')
        for item in all_item:
            __M_writer('\r\n\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(item.id))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(item.name))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(item.condition))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(item.newDamage))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(item.damageFee))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(item.dueDate))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(item.lateFee))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(item.description))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td><a href="/homepage/rentable_item.edit/')
            __M_writer(str(item.id))
            __M_writer('/">Edit</a>\r\n\t\t\t\t\t\t|\r\n\t\t\t\t\t\t <a href=\'/homepage/rentable_item.delete/')
            __M_writer(str(item.id))
            __M_writer("/'>Delete</a></td>\r\n\r\n\t\t\t\t\t</tr>\r\n")
        __M_writer('\r\n\t\t\t</table>\r\n\t<a href="/homepage/rentable_item.query/" class ="btn btn-warning">Generate overdue report</a>\r\n\t<a href="/homepage/rentable_item.query_thirty/" class ="btn btn-warning">30 Days</a>\r\n\t<a href="/homepage/rentable_item.query_sixty/" class ="btn btn-warning">60 Days</a>\r\n\t<a href="/homepage/rentable_item.query_ninety/" class ="btn btn-warning">90+ Days</a>\r\n\t<a href="/homepage/rentable_item.send_email/" class ="btn btn-warning">Send Overdue Emails</a>\r\n\r\n\r\n\r\n\t</html>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"65": 3, "107": 41, "71": 62, "108": 41, "77": 62, "112": 44, "83": 7, "90": 7, "91": 31, "92": 32, "93": 34, "94": 34, "95": 35, "96": 35, "97": 36, "98": 36, "27": 0, "100": 37, "101": 38, "102": 38, "39": 1, "104": 39, "105": 40, "106": 40, "103": 39, "44": 5, "109": 42, "110": 42, "111": 44, "99": 37, "49": 60, "113": 48, "119": 113, "59": 3}, "filename": "C:\\Python34\\Projects\\CHF\\homepage\\templates/rentable_item.html", "source_encoding": "ascii", "uri": "rentable_item.html"}
__M_END_METADATA
"""
