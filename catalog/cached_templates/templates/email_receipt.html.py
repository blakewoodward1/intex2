# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428364852.086945
_enable_loop = True
_template_filename = '/Users/BlakeWoodward/CoHerFoun/catalog/templates/email_receipt.html'
_template_uri = 'email_receipt.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        user = context.get('user', UNDEFINED)
        int = context.get('int', UNDEFINED)
        request = context.get('request', UNDEFINED)
        cart = context.get('cart', UNDEFINED)
        str = context.get('str', UNDEFINED)
        all_items = context.get('all_items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<img src="http://2.bp.blogspot.com/-Al9-SWLlHdo/UmGvQhcFQqI/AAAAAAAAACk/mBRacWRhQSw/s400/logoH2.png" />\n<p>\nHello ')
        __M_writer(str(user.first_name))
        __M_writer("\n</p>\n<p>\nThank you for shopping with us.  Your products will arrive in a few days.  \n</p>\n\n<table style='border: solid 1px black'>\n<tr style='border: solid 1px black'>\n\t<th span=3>Order Receipt</th>\n</tr>\n<tr style='border: solid 1px black'>\n\t<td>Item Number</td>\n\t<td>Quantity</td>\n\t<td>Item</td>\n\t<td>Price per Unit</td>\n\t<td>Total</td>\n</tr>\n")
        TP = 0
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['TP'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n')
        for item in cart:
            __M_writer("\t<tr style='border: solid 1px black'>\n\t\t<td>")
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
                        __M_writer('\t\t\t\t\t<td>')
                        __M_writer(str(product.price * int(request.session['shopping_cart'][item][0]) * int(request.session['shopping_cart'][item][1]) ))
                        __M_writer('</td>\n\t\t\t\t\t')
                        TP = TP+ product.price * int(request.session['shopping_cart'][item][0]) * int(request.session['shopping_cart'][item][1])
                        
                        __M_locals_builtin_stored = __M_locals_builtin()
                        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['TP'] if __M_key in __M_locals_builtin_stored]))
                        __M_writer('\n')
                    else:
                        __M_writer('\t\t\t\t\t<td>')
                        __M_writer(str(product.price * int(request.session['shopping_cart'][item][0])))
                        __M_writer('</td>\n\t\t\t\t\t')
                        TP = TP+ product.price * int(request.session['shopping_cart'][item][0])
                        
                        __M_locals_builtin_stored = __M_locals_builtin()
                        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['TP'] if __M_key in __M_locals_builtin_stored]))
                        __M_writer('\n')
                    __M_writer('\n\n')
            __M_writer('\n\n\t</tr>\n\n\n')
        __M_writer("<tr id='total_cost'>\n\t<td></td><td></td><td></td><td>Total:</td><td>")
        __M_writer(str(TP))
        __M_writer("</td>\n</tr>\n</table>\n\n\n\n\n<p>\n\tIf you didn't request this code, please contact us at support@chfgroup.us.\n</p>")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/BlakeWoodward/CoHerFoun/catalog/templates/email_receipt.html", "source_encoding": "ascii", "uri": "email_receipt.html", "line_map": {"67": 37, "68": 39, "69": 43, "70": 49, "71": 50, "72": 50, "78": 72, "16": 0, "27": 1, "28": 3, "29": 3, "30": 20, "34": 20, "35": 21, "36": 22, "37": 23, "38": 23, "39": 24, "40": 24, "41": 26, "42": 27, "43": 28, "44": 29, "45": 30, "46": 30, "47": 30, "48": 31, "49": 31, "50": 32, "51": 33, "52": 33, "53": 33, "54": 34, "58": 34, "59": 35, "60": 36, "61": 36, "62": 36, "63": 37}}
__M_END_METADATA
"""
