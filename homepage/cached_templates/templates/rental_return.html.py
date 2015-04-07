# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428199858.118922
_enable_loop = True
_template_filename = 'C:\\Python34\\Projects\\CHF\\homepage\\templates/rental_return.html'
_template_uri = 'rental_return.html'
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
        def header():
            return render_header(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        all_item = context.get('all_item', UNDEFINED)
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
        all_item = context.get('all_item', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\t<html>\r\n\t\t<body>\r\n\t\t\t<h2> Rentable Items</h2>\r\n\t\t\t<div class = "text-right">\r\n\t\t\t\t<a href="/homepage/rentable_item.create/" class ="btn btn-warning">\r\n\t\t\t\t Create New Rentable Item</a>\r\n\t\t\t</div>\r\n\t\t\t<br>\r\n\t\t\t<table class="table table-striped table-bordered">\r\n\t\t\t\t<tr>\r\n\t\t\t\t\t<th>Renter</th>\r\n\t\t\t\t\t<th>Name</th>\r\n\t\t\t\t\t<th>Condition</th>\r\n\t\t\t\t\t<th>New Damage</th>\r\n\t\t\t\t\t<th>Damage Fee</th>\r\n\t\t\t\t\t<th>Due Date</th>\r\n\t\t\t\t\t<th>Late Fee</th>\t\r\n\t\t\t\t\t<th>Description</th>\r\n\t\t\t\t\t<th>Actions</th>\r\n\r\n\r\n\t\t\t\t</tr>\t\t\t\r\n')
        for item in all_item:
            __M_writer('\r\n\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(item.renterName))
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
            __M_writer('</td>\r\n\t\t\t\t\t\t<td><a href="/homepage/rental_return.RReturn/')
            __M_writer(str(item.id))
            __M_writer('/">Check in</a>\r\n\t\t\t\t\t\t\r\n\t\t\t\t\t</tr>\r\n')
        __M_writer('\r\n\t\t\t</table>\r\n\r\n\t</html>\r\n\r\n')
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


"""
__M_BEGIN_METADATA
{"uri": "rental_return.html", "filename": "C:\\Python34\\Projects\\CHF\\homepage\\templates/rental_return.html", "line_map": {"66": 7, "67": 31, "68": 32, "69": 34, "70": 34, "71": 35, "72": 35, "73": 36, "74": 36, "75": 37, "76": 37, "77": 38, "78": 38, "79": 39, "80": 39, "81": 40, "82": 40, "83": 41, "84": 41, "85": 42, "86": 42, "87": 46, "27": 0, "93": 53, "99": 53, "39": 1, "105": 3, "44": 5, "111": 3, "49": 51, "117": 111, "59": 7}, "source_encoding": "ascii"}
__M_END_METADATA
"""
