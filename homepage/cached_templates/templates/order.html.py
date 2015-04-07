# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423171270.584694
_enable_loop = True
_template_filename = 'C:\\Python34\\Projects\\CHF\\homepage\\templates/order.html'
_template_uri = 'order.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['header', 'content', 'title']


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
        def header():
            return render_header(context._locals(__M_locals))
        all_order = context.get('all_order', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
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
        all_order = context.get('all_order', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\t<html>\r\n\t\t<body>\r\n\t\t\t<h2> All Orders</h2>\r\n\t\t\t<div class = "text-right">\r\n\t\t\t\t<a href="/homepage/order.create/" class ="btn btn-warning"> Create New Order</a>\r\n\t\t\t</div>\r\n\t\t\t<br>\r\n\t\t\t<table class="table table-striped table-bordered">\r\n\t\t\t\t<tr>\r\n\t\t\t\t\t<th>ID</th>\r\n\t\t\t\t\t<th>Order Number</th>\r\n\t\t\t\t\t<th>Order Date</th>\r\n\t\t\t\t\t<th>Phone</th>\r\n\t\t\t\t\t<th>Date Packed</th>\t\r\n\t\t\t\t\t<th>Date Paid</th>\t\t\t\t\r\n\t\t\t\t\t<th>Date Shipped</th>\r\n\t\t\t\t\t<th>Tracking Number</th>\r\n\t\t\t\t\t<th>Actions</th>\r\n\r\n\t\t\t\t</tr>\t\t\t\r\n')
        for order in all_order:
            __M_writer('\r\n\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(order.id))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(order.OrderNumber))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(order.orderDate))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(order.Phone))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(order.datePacked))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(order.datePaid))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(order.dateShipped))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(order.trackingNumber))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td><a href="/homepage/order.edit/')
            __M_writer(str(order.id))
            __M_writer('/">Edit</a>\r\n\t\t\t\t\t\t|\r\n\t\t\t\t\t\t <a href=\'/homepage/order.delete/')
            __M_writer(str(order.id))
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
        __M_writer('\r\n\tOrders\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "order.html", "source_encoding": "ascii", "line_map": {"65": 53, "71": 7, "78": 7, "79": 29, "80": 30, "81": 32, "82": 32, "83": 33, "84": 33, "85": 34, "86": 34, "87": 35, "88": 35, "89": 36, "90": 36, "27": 0, "92": 37, "93": 38, "94": 38, "95": 39, "96": 39, "97": 40, "98": 40, "91": 37, "100": 42, "101": 46, "39": 1, "107": 3, "44": 5, "99": 42, "49": 51, "113": 3, "119": 113, "59": 53}, "filename": "C:\\Python34\\Projects\\CHF\\homepage\\templates/order.html"}
__M_END_METADATA
"""
