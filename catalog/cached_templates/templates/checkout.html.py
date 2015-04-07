# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428380588.126671
_enable_loop = True
_template_filename = '/Users/BlakeWoodward/CoHerFoun/catalog/templates/checkout.html'
_template_uri = 'checkout.html'
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
        int = context.get('int', UNDEFINED)
        str = context.get('str', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        request = context.get('request', UNDEFINED)
        cart = context.get('cart', UNDEFINED)
        all_items = context.get('all_items', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\n\n\n  <head>\n    <title>REST API Example</title> \n    <script src="//ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script> \n    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css"> \n    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap-theme.min.css">\n    <script src="//netdna.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>\n  </head>\n\n')
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
        int = context.get('int', UNDEFINED)
        str = context.get('str', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        request = context.get('request', UNDEFINED)
        cart = context.get('cart', UNDEFINED)
        all_items = context.get('all_items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<br><br><br>\n<h1>Checkout</h1>\n\n<table class="table table-condensed" style="background: white; border: black solid 2px">\n<tr>\n\t<td><p><b>Item Number</b></p></td>\n\t<td><p><b>Image</b></p></td>\n\t<td><p><b>Item</b></p></td>\n\t<td><p><b>Quantity</b></p></td>\n\t<td><p><b>Price per Unit</b></p></td>\n\t<td><p><b>Total</b></p></td>\n</tr>\n\n\n')
        TP = 0
        
        __M_writer('\n')
        for item in cart:
            __M_writer('\t<tr>\n\t\t\n\t\t<td><p>')
            __M_writer(str(item))
            __M_writer('</p></td>\n\t\t<td>\n\t\t<img src="')
            __M_writer(str(STATIC_URL))
            __M_writer('catalog/media/product_images/')
            __M_writer(str(item))
            __M_writer('.png" />\n\t\t</td>\n\t\t\n\t\t\n')
            for product in all_items:
                if not str(product.id)  == item:
                    __M_writer('\t\t\t\t\n')
                else:
                    __M_writer('\t\t\t\t<td><p>')
                    __M_writer(str(product.name))
                    __M_writer('</p></td>\n\t\t\t\t<td><p> ')
                    __M_writer(str( request.session['shopping_cart'][item][0] ))
                    __M_writer('</p></td>\n\t\t\t\t<td><p>$')
                    __M_writer(str(product.price))
                    __M_writer('</p></td>\n')
                    if product.isRental:
                        __M_writer('\t\t\t\t\t<td><p>$')
                        __M_writer(str(product.price * int(request.session['shopping_cart'][item][0]) * int(request.session['shopping_cart'][item][1]) ))
                        __M_writer('</p></td>\n\t\t\t\t\t')
                        TP = TP+ product.price * int(request.session['shopping_cart'][item][0]) * int(request.session['shopping_cart'][item][1])
                        
                        __M_writer('\n')
                    else:
                        __M_writer('\t\t\t\t\t<td><p>$')
                        __M_writer(str(product.price * int(request.session['shopping_cart'][item][0])))
                        __M_writer('</p></td>\n\t\t\t\t\t')
                        TP = TP+ product.price * int(request.session['shopping_cart'][item][0])
                        
                        __M_writer('\n')
                    __M_writer('\n\n')
            __M_writer('\n\n\t</tr>\n\n\n')
        __M_writer("<tr id='total_cost'>\n\t<td></td><td></td><td></td><td></td><td><p><b>Total:</b></p></td><td id ='chargeID'><p><b>$")
        __M_writer(str(TP))
        __M_writer('</b></p></td>\n</tr>\n</table>\n<input type="text" name="CCN" id=\'chargeId\' value="')
        __M_writer(str(TP))
        __M_writer('" style=\'display: none\'>\n\n\n<div id=\'billing_info\'>\n<h1>Billing Information</h1>\n\t<table class="table">\n\t\t<tr>\n\t\t\t<td> Credit card number </td>\n\t\t\t<td> <input type="text" name="CCN"  value="4732817300654"></td>\n\t\t</tr>\n\t\t<tr>\n\t\t\t<td> CVC Nuber </td>\n\t\t\t<td> <input type="text" value =\'411\'></td>\n\t\t</tr>\n\t\t<tr>\n\t\t\t<td> Billing Address </td>\n\t\t\t<td> <input type="text" value = \'test\'></td>\n\t\t</tr>\n\t\t<tr>\n\t\t\t<td> City </td>\n\t\t\t<td> <input type="text"></td>\n\t\t</tr>\t\t\n\t\t<tr>\n\t\t\t<td> State </td>\n\t\t\t<td> <input type="text"></td>\n\t\t</tr>\n\t\t<tr>\n\t\t\t<td> ZIP </td>\n\t\t\t<td> <input type="text"></td>\n\t\t</tr>\n\t\t<tr>\n\t\t\t<td> Name </td>\n\t\t\t<td> <input type="text"></td>\n\t\t</tr>\n\t\t<tr>\n\t\t\t<td> Phone number </td>\n\t\t\t<td> <input type="text"></td>\n\t\t</tr>\n\t\t<tr>\n\t\t\t<td>\n\t\t\t\t<a href="#" class=\'btn btn-warning\' id=\'charge\' style=\'font-size:1.25em;\'>Place Order</a>\n\n    <br/>\n    <div id="message"></div> \n\t</table>\n\n</div>\n\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\n  Billing and Checkout\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/BlakeWoodward/CoHerFoun/catalog/templates/checkout.html", "uri": "checkout.html", "source_encoding": "ascii", "line_map": {"130": 124, "27": 0, "42": 1, "47": 5, "57": 16, "69": 16, "70": 30, "72": 30, "73": 31, "74": 32, "75": 34, "76": 34, "77": 36, "78": 36, "79": 36, "80": 36, "81": 40, "82": 41, "83": 42, "84": 43, "85": 44, "86": 44, "87": 44, "88": 45, "89": 45, "90": 46, "91": 46, "92": 47, "93": 48, "94": 48, "95": 48, "96": 49, "98": 49, "99": 50, "100": 51, "101": 51, "102": 51, "103": 52, "105": 52, "106": 54, "107": 58, "108": 64, "109": 65, "110": 65, "111": 68, "112": 68, "118": 3, "124": 3}}
__M_END_METADATA
"""
