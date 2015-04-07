# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428368113.328219
_enable_loop = True
_template_filename = '/Users/BlakeWoodward/CoHerFoun/catalog/templates/detail.html'
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        all_item = context.get('all_item', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\n\n\n  <head>\n    <title>REST API Example</title> \n    <script src="//ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script> \n    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css"> \n    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap-theme.min.css">\n    <script src="//netdna.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>\n  </head>\n  \n')
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
        __M_writer('\n \tItem Details\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        all_item = context.get('all_item', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\t\n\t<div id="product_image">\n\t\t<img  src=\'')
        __M_writer(str(STATIC_URL))
        __M_writer('catalog/media/product_images/')
        __M_writer(str(all_item.id))
        __M_writer(".png' />\n\t</div>\n\t\n\n\t<div  id = 'product_name'>\n")
        if all_item.isRental:
            __M_writer('\t\t<h1>\t\n\t\t\tRental\n\t\t</h1>\n')
        else:
            __M_writer('\t\t<h1>\t\n\t\t\tProduct for Sale\n\t\t</h1>\n')
        __M_writer('\n\t\t<table class = "table table-hover">\n\t\t<tr>\n\t\t<th><p>Item:</p></th>\n\t\t<td><p>')
        __M_writer(str(all_item.name))
        __M_writer('</p></td>\n\t\t</tr>\n\t\t<tr>\n\t\t<th><p>Price:</p></th>\n\t\t<td><p>$')
        __M_writer(str(all_item.price))
        __M_writer('\n')
        if all_item.isRental:
            __M_writer('\t\t\t\tper day\n')
        __M_writer('\t\t\t</p></td>\n\t\t</tr>\n\t\t<tr>\n\t\t<th><p>Description:</p></th>\n\t\t\t<td><p>')
        __M_writer(str(all_item.description))
        __M_writer('</p></td>\n\t\t</tr>\n\t\t<th><p>Quantity:</p></th>\n\n\t\t\t <td><p> <input type="number" name="qty" id="qty" value="1"></p></td>\n')
        if all_item.isRental:
            __M_writer('\t\t\t \t<tr>\n\t\t\t \t<th><p>Number of days (includes shipping time)</p></th>\n\t\t\t \t<td><p><input type="number" name="days" id="days" value="5"></p></td><br>\n\t\t\t \t</tr>\n\t\t\t\t\n\t\t\t\t<tr>\n \t\t\t\t<td><button data-pid="')
            __M_writer(str( all_item.id))
            __M_writer('" class=\' add_rental btn btn-warning\'> Add to cart</button></td>\n \t\t\t\t</tr>\n')
        else:
            __M_writer('\t\t\t \t<tr>\n\t\t\t \t\n\t\t\t\t<td><button data-pid="')
            __M_writer(str( all_item.id))
            __M_writer('" class=\' add_button btn btn-warning\'> Add to cart</button></td>\n\t\t\t\t</tr>\n')
        __M_writer('\t\t\t</table>\n\n\t</div>\n\t\n\n<!-- Modal -->\n      <div class="modal fade" id="add_to_cart" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\n        <div class="modal-dialog">\n          <div class="modal-content">\n            <div class="modal-header">\n              <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n              <h4 class="modal-title" id="myModalLabel">Login</h4>\n            </div>\n            <div class="modal-body">\n              ...\n            </div>\n            <div class="modal-footer">\n              <!--<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\n              <button type="button" class=" btn btn-primary">Save changes</button>-->\n            </div>\n          </div>\n        </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/BlakeWoodward/CoHerFoun/catalog/templates/detail.html", "source_encoding": "ascii", "uri": "detail.html", "line_map": {"65": 16, "73": 16, "74": 19, "75": 19, "76": 19, "77": 19, "78": 24, "79": 25, "80": 28, "81": 29, "82": 33, "83": 37, "84": 37, "85": 41, "86": 41, "87": 42, "88": 43, "89": 45, "90": 49, "27": 0, "92": 54, "93": 55, "94": 61, "95": 61, "96": 63, "97": 64, "98": 66, "91": 49, "100": 69, "38": 1, "106": 100, "43": 5, "99": 66, "53": 3, "59": 3}}
__M_END_METADATA
"""
