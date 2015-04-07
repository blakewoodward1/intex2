# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428202391.725265
_enable_loop = True
_template_filename = 'C:\\Python34\\Projects\\CHF\\homepage\\templates/payment.html'
_template_uri = 'payment.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['title', 'content']


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
        def title():
            return render_title(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        fees = context.get('fees', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n\r\n\r\n  <head>\r\n    <title>REST API Example</title> \r\n    <script src="//ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script> \r\n    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css"> \r\n    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap-theme.min.css">\r\n    <script src="//netdna.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>\r\n  </head>\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n  Billing and Checkout\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        fees = context.get('fees', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<h1> Checkout</h1>\r\n\r\n<div id=\'shopping_cart\'>\r\n\r\n</div>\r\n\r\n\r\n<input type="text" name="CCN" id=\'chargeId\' value="')
        __M_writer(str(fees))
        __M_writer('" style=\'display: none\'>\r\n\r\n\r\n<div id=\'billing_info\'>\r\n\t<table>\r\n\t\t<tr>\r\n\t\t\t<td> Credit card number </td>\r\n\t\t\t<td> <input type="text" name="CCN"  value="4732817300654"></td>\r\n\t\t</tr>\r\n\t\t<tr>\r\n\t\t\t<td> CVC Nuber </td>\r\n\t\t\t<td> <input type="text" value =\'411\'></td>\r\n\t\t</tr>\r\n\t\t<tr>\r\n\t\t\t<td> Billing Address </td>\r\n\t\t\t<td> <input type="text" value = \'test\'></td>\r\n\t\t</tr>\r\n\t\t<tr>\r\n\t\t\t<td> City </td>\r\n\t\t\t<td> <input type="text"></td>\r\n\t\t</tr>\t\t\r\n\t\t<tr>\r\n\t\t\t<td> State </td>\r\n\t\t\t<td> <input type="text"></td>\r\n\t\t</tr>\r\n\t\t<tr>\r\n\t\t\t<td> ZIP </td>\r\n\t\t\t<td> <input type="text"></td>\r\n\t\t</tr>\r\n\t\t<tr>\r\n\t\t\t<td> Name </td>\r\n\t\t\t<td> <input type="text"></td>\r\n\t\t</tr>\r\n\t\t<tr>\r\n\t\t\t<td> Phone number </td>\r\n\t\t\t<td> <input type="text"></td>\r\n\t\t</tr>\r\n\t\t<tr>\r\n\t\t\t<td>\r\n\t\t\t\t<a href="#" class=\'btn btn-warning\' id=\'charge\' style=\'font-size:1.25em;\'>Place Order</a>\r\n\r\n    <br/>\r\n    <div id="message"></div> \r\n\t</table>\r\n\r\n</div>\r\n\r\n\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"64": 16, "52": 3, "37": 1, "71": 16, "72": 24, "73": 24, "58": 3, "27": 0, "42": 5, "79": 73}, "uri": "payment.html", "filename": "C:\\Python34\\Projects\\CHF\\homepage\\templates/payment.html"}
__M_END_METADATA
"""
