# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428360319.753228
_enable_loop = True
_template_filename = '/Users/BlakeWoodward/CoHerFoun/event/templates/detail.html'
_template_uri = 'detail.html'
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
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        products = context.get('products', UNDEFINED)
        event = context.get('event', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\n\n')
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
        __M_writer('\nEvent Details\t\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        products = context.get('products', UNDEFINED)
        event = context.get('event', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n<br><br><br>\n\n<div class="main">\n\n<title>')
        __M_writer(str(event.name))
        __M_writer('</title>\n<meta name="keywords" content="')
        __M_writer(str(event.name))
        __M_writer('">\n\n<h1>')
        __M_writer(str(event.name))
        __M_writer('<small> &nbsp&nbsp&nbsp')
        __M_writer(str(event.startDate))
        __M_writer('</small></h1>\n  <img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('event/media/images/')
        __M_writer(str(event.id))
        __M_writer('.png" alt="')
        __M_writer(str(event.name))
        __M_writer('"/>\n</div>\n\n')
        if request.user.has_perm(True):
            __M_writer('<div class="admin-functions">\n<p>You are Admin, you can:\n<a href="/homepage/event_details.edit/')
            __M_writer(str(event.id))
            __M_writer('">Edit</a> |\n<a href="/homepage/event_details.delete/')
            __M_writer(str(event.id))
            __M_writer('">Delete</a></p>\n</div>\n')
        __M_writer('\n<div class="details">\n\t<table class = "table table-condensed">\n  <tr>\n    <th><p>Event Name</p></th>\n    <td><p>')
        __M_writer(str(event.name))
        __M_writer('</p></td>\n  </tr>\n  <tr>\n    <th><p>Start Date</p></th>\n    <td><p>')
        __M_writer(str(event.startDate))
        __M_writer('</p></td>\n  </tr>\n  <tr>\n    <th><p>End Date</p></th>\n    <td><p>')
        __M_writer(str(event.endDate))
        __M_writer('</p></td>\n  </tr>\n  <tr>\n    <th><p >Location:</p></th>\n    <td><a href="https://www.google.com/maps/place/" target="_blank"><p>Salt Lake City</p></a></td>\n  </tr>\n  <tr>\n    <th><p>Description:</p></th>\n    <td><p>')
        __M_writer(str(event.description))
        __M_writer("</p></td>\n  </tr>\n  </table>\n\n  <div id = 'sponsered_products'>\n\t<table>\n\t\t<tr><td><h4>Sponsored Products</h4></td></tr>\n\t\t<tr><td>\n")
        for product in products:
            __M_writer("\t\t\t\t<div class = 'product_container'>\n\t\t\t\t\t<a href ='/catalog/detail/")
            __M_writer(str(product.id))
            __M_writer("'>\n\t\t\t\t\t\t<img src='")
            __M_writer(str(STATIC_URL))
            __M_writer('catalog/media/product_images/')
            __M_writer(str(product.id))
            __M_writer(".png' />\n\t\t\t\t\t\t<div>\n\t\t\t\t\t\t<p>")
            __M_writer(str(product.name))
            __M_writer('</p></div>\n\t\t\t\t\t</a>\n\t\t\t\t</div>\n')
        __M_writer('\t\t</td></tr>\n\t</table>\n\n\n\n</div>\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/BlakeWoodward/CoHerFoun/event/templates/detail.html", "source_encoding": "ascii", "uri": "detail.html", "line_map": {"27": 0, "40": 1, "45": 5, "55": 3, "61": 3, "67": 7, "77": 7, "78": 12, "79": 12, "80": 13, "81": 13, "82": 15, "83": 15, "84": 15, "85": 15, "86": 16, "87": 16, "88": 16, "89": 16, "90": 16, "91": 16, "92": 19, "93": 20, "94": 22, "95": 22, "96": 23, "97": 23, "98": 26, "99": 31, "100": 31, "101": 35, "102": 35, "103": 39, "104": 39, "105": 47, "106": 47, "107": 55, "108": 56, "109": 57, "110": 57, "111": 58, "112": 58, "113": 58, "114": 58, "115": 60, "116": 60, "117": 64, "123": 117}}
__M_END_METADATA
"""
