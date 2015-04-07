# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428371481.884199
_enable_loop = True
_template_filename = '/Users/BlakeWoodward/CoHerFoun/catalog/templates/shopping_cart.html'
_template_uri = 'shopping_cart.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


import datetime as dt 

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
    return runtime._inherit_from(context, '/homepage/templates/base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        int = context.get('int', UNDEFINED)
        str = context.get('str', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        request = context.get('request', UNDEFINED)
        cart = context.get('cart', UNDEFINED)
        all_items = context.get('all_items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        int = context.get('int', UNDEFINED)
        str = context.get('str', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        request = context.get('request', UNDEFINED)
        cart = context.get('cart', UNDEFINED)
        all_items = context.get('all_items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer(' <!-- ! -->\n<h2>Products</h2>\n<table class="table">\n\t<tr> \n\t\t<th>Item ID</th>\n\t\t<th>Image</th>\n\t\t<th>Quantity</th>\n\n\t\t<th>Total</th>\n\t\t<th></th>\n\t</tr>\n')
        for item in cart:
            __M_writer('\t\t<tr>\t\t\t\n')
            for product in all_items:
                if not str(product.id)  == item:
                    __M_writer('\t\t\t\t\t\n')
                else:
                    if not product.isRental:
                        __M_writer('\t\t\t\t\t\t<td>')
                        __M_writer(str(item))
                        __M_writer('</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t<img src="')
                        __M_writer(str(STATIC_URL))
                        __M_writer('catalog/media/product_images/')
                        __M_writer(str(item))
                        __M_writer('.png" />\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t ')
                        __M_writer(str( request.session['shopping_cart'][item][0] ))
                        __M_writer('\n\t\t\t\t\t\t</td>\n\n\t\t\t\t\t\t<td>$')
                        __M_writer(str(product.price * int(request.session['shopping_cart'][item][0])))
                        __M_writer("</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t<button class='delete btn btn-danger' data-pid='")
                        __M_writer(str(item))
                        __M_writer("'>Remove from cart</button>\n\t\t\t\t\t\t\n\t\t\t\t\t\t</td>\n")
            __M_writer('\t\t\t\n\t\t\t\n\t\t</tr>\n')
        __M_writer('</table>\n\n\n<h2>Rentals</h2>\n<table class="table">\n\t<tr> \n\t\t<th>Item ID</th>\n\t\t<th>Image</th>\n\t\t<th>Quantity</th>\n\t\t<th>Due Date</th>\n\t\t<th>Total</th>\n\t\t<th></th>\n\t</tr>\n')
        for item in cart:
            __M_writer('\t\t<tr>\t\t\t\n')
            for product in all_items:
                if not str(product.id)  == item:
                    __M_writer('\t\t\t\t\t\n')
                else:
                    if product.isRental:
                        __M_writer('\t\t\t\t\t\t<td>')
                        __M_writer(str(item))
                        __M_writer('</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t<img src="')
                        __M_writer(str(STATIC_URL))
                        __M_writer('catalog/media/product_images/')
                        __M_writer(str(item))
                        __M_writer('.png" />\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t ')
                        __M_writer(str( request.session['shopping_cart'][item][0] ))
                        __M_writer('\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>')
                        __M_writer(str(dt.date.today() + dt.timedelta(days=int(request.session['shopping_cart'][item][1]))))
                        __M_writer('</td>\n\t\t\t\t\t\t<td>$')
                        __M_writer(str(product.price * int(request.session['shopping_cart'][item][0]) * int(request.session['shopping_cart'][item][1])))
                        __M_writer("</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t<button class='delete btn btn-danger' data-pid='")
                        __M_writer(str(item))
                        __M_writer("'>Remove from cart</button>\n\t\t\t\t\t\t</td>\n")
            __M_writer('\t\t</tr>\n')
        __M_writer("</table>\n\n<p><a href='/catalog/' class='btn btn-primary'>Continue Shopping</a>\n\n<a href='/catalog/checkout/' class='btn btn-warning'>Check out</a></p>\n\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/BlakeWoodward/CoHerFoun/catalog/templates/shopping_cart.html", "uri": "shopping_cart.html", "source_encoding": "ascii", "line_map": {"16": 3, "29": 0, "42": 1, "47": 84, "53": 2, "65": 2, "66": 3, "67": 14, "68": 15, "69": 16, "70": 17, "71": 18, "72": 19, "73": 20, "74": 21, "75": 21, "76": 21, "77": 23, "78": 23, "79": 23, "80": 23, "81": 26, "82": 26, "83": 29, "84": 29, "85": 31, "86": 31, "87": 37, "88": 41, "89": 54, "90": 55, "91": 56, "92": 57, "93": 58, "94": 59, "95": 60, "96": 61, "97": 61, "98": 61, "99": 63, "100": 63, "101": 63, "102": 63, "103": 66, "104": 66, "105": 68, "106": 68, "107": 69, "108": 69, "109": 71, "110": 71, "111": 76, "112": 78, "118": 112}}
__M_END_METADATA
"""
