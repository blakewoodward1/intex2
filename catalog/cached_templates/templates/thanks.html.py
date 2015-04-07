# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428427292.31091
_enable_loop = True
_template_filename = '/Users/BlakeWoodward/CoHerFoun/catalog/templates/thanks.html'
_template_uri = 'thanks.html'
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
        cart = context.get('cart', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        int = context.get('int', UNDEFINED)
        str = context.get('str', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        all_items = context.get('all_items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\n\n\n')
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
        __M_writer('\n \tThank you!\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        cart = context.get('cart', UNDEFINED)
        def content():
            return render_content(context)
        request = context.get('request', UNDEFINED)
        int = context.get('int', UNDEFINED)
        str = context.get('str', UNDEFINED)
        all_items = context.get('all_items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<br><br><br>\n\n<div class="everything">\n<h1 class="text-center"> Thank You!</h1>\n<p>A copy of this receipt has been sent to your email. Please keep a copy for your own records.</p>\n<table>\n<tr>\n\t<th span=3>Order Receipt</th>\n</tr>\n<tr>\n\t<td>Item Number</td>\n\t<td>Quantity</td>\n\t<td>Item</td>\n\t<td>Price per Unit</td>\n\t<td>Total</td>\n</tr>\n')
        TP = 0
        
        __M_writer('\n')
        for item in cart:
            __M_writer('\t<tr>\n\t\t<td>')
            __M_writer(str(item))
            __M_writer('</td>\n\t\t<td> ')
            __M_writer(str( request.session['shopping_cart'][item][0] ))
            __M_writer('</td>\n\t\t\n')
            for product in all_items:
                if not str(product.id)  == item:
                    __M_writer('\t\t\t\t\n')
                else:
                    __M_writer('\t\t\t\t<td>')
                    __M_writer(str(product.name))
                    __M_writer('</td>\n\t\t\t\t<td>$')
                    __M_writer(str(product.price))
                    __M_writer('</td>\n')
                    if product.isRental:
                        __M_writer('\t\t\t\t\t<td>$')
                        __M_writer(str(product.price * int(request.session['shopping_cart'][item][0]) * int(request.session['shopping_cart'][item][1]) ))
                        __M_writer('</td>\n\t\t\t\t\t')
                        TP = TP+ product.price * int(request.session['shopping_cart'][item][0]) * int(request.session['shopping_cart'][item][1])
                        
                        __M_writer('\n')
                    else:
                        __M_writer('\t\t\t\t\t<td>$')
                        __M_writer(str(product.price * int(request.session['shopping_cart'][item][0])))
                        __M_writer('</td>\n\t\t\t\t\t')
                        TP = TP+ product.price * int(request.session['shopping_cart'][item][0])
                        
                        __M_writer('\n')
                    __M_writer('\n\n')
            __M_writer('\n\n\t</tr>\n\n\n')
        __M_writer("<tr id='total_cost'>\n\t<td></td><td></td><td></td><td>Total:</td><td>$")
        __M_writer(str(TP))
        __M_writer('</td>\n</tr>\n</table>\n<br>\n<a href="/catalog/" class="btn btn-primary">Return to Products</a>\n\n</div>\n\n')
  
        del request.session['shopping_cart']
        if 'shopping_cart' not in request.session:
                request.session['shopping_cart'] = {}
                request.session.modified=True
        
        
        
        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "thanks.html", "line_map": {"131": 125, "27": 0, "41": 1, "46": 4, "56": 2, "62": 2, "68": 7, "79": 7, "80": 24, "82": 24, "83": 25, "84": 26, "85": 27, "86": 27, "87": 28, "88": 28, "89": 30, "90": 31, "91": 32, "92": 33, "93": 34, "94": 34, "95": 34, "96": 35, "97": 35, "98": 36, "99": 37, "100": 37, "101": 37, "102": 38, "104": 38, "105": 39, "106": 40, "107": 40, "108": 40, "109": 41, "111": 41, "112": 43, "113": 47, "114": 53, "115": 54, "116": 54, "117": 62, "125": 68}, "filename": "/Users/BlakeWoodward/CoHerFoun/catalog/templates/thanks.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
