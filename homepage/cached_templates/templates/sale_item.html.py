# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423184986.983769
_enable_loop = True
_template_filename = 'C:\\Python34\\Projects\\CHF\\homepage\\templates/sale_item.html'
_template_uri = 'sale_item.html'
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
        all_sale = context.get('all_sale', UNDEFINED)
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
        all_sale = context.get('all_sale', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\t<html>\r\n\t\t<body>\r\n\t\t\t<h2>Sale Items</h2>\r\n\t\t\t<div class = "text-right">\r\n\t\t\t\t<a href="/homepage/sale_item.create/" class ="btn btn-warning">\r\n\t\t\t\t Create New Sale Item</a>\r\n\t\t\t</div>\r\n\t\t\t<br>\r\n\t\t\t\r\n\t\t\t<table class="table table-striped table-bordered">\r\n\t\t\t\t<tr>\r\n\t\t\t\t\t<th>ID</th>\r\n\t\t\t\t\t<th>Name</th>\r\n\t\t\t\t\t<th>Description</th>\r\n\t\t\t\t\t<th>Low Price</th>\r\n\t\t\t\t\t<th>High Price</th>\r\n\t\t\t\t\t<th>Actions</th>\r\n\r\n\t\t\t\t</tr>\t\t\t\r\n')
        for sale in all_sale:
            __M_writer('\r\n\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(sale.id))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(sale.name))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(sale.description))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(sale.low_price))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(sale.high_price))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td><a href="/homepage/sale_item.edit/')
            __M_writer(str(sale.id))
            __M_writer('/">Edit</a>\r\n\t\t\t\t\t\t|\r\n\t\t\t\t\t\t <a href = \'/homepage/sale_item.delete/')
            __M_writer(str(sale.id))
            __M_writer("/'>Delete</a></td>\r\n\r\n\t\t\t\t\t</tr>\r\n")
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
        __M_writer('\r\n\tUsers\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "sale_item.html", "line_map": {"66": 7, "67": 28, "68": 29, "69": 31, "70": 31, "71": 32, "72": 32, "73": 33, "74": 33, "75": 34, "76": 34, "77": 35, "78": 35, "79": 36, "80": 36, "81": 38, "82": 38, "83": 42, "89": 49, "27": 0, "95": 49, "113": 107, "101": 3, "39": 1, "107": 3, "44": 5, "49": 47, "59": 7}, "filename": "C:\\Python34\\Projects\\CHF\\homepage\\templates/sale_item.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
