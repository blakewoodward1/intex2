# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428368034.204924
_enable_loop = True
_template_filename = '/Users/BlakeWoodward/CoHerFoun/catalog/templates/index.html'
_template_uri = 'index.html'
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
        list = context.get('list', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        all_item = context.get('all_item', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n\n\n')
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
        __M_writer('\n\tBrowse Products  \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        list = context.get('list', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        len = context.get('len', UNDEFINED)
        all_item = context.get('all_item', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n<title>Products & Rentals</title>\n<br><br><br>\n\n<div class="jumbotron">\n  <h1>Products & Rentals</h1>\n  <p>Eum clita partem admodum ea, vel et nibh aliquam. Cu nam probo option, ei inani euismod maluisset ius. Graeci percipit has eu. Nisl nulla appareat usu cu, ei iusto quidam nam, doctus incorrupte vel ad. Graece libris prodesset vel eu, ne homero latine posidonium his.</p>\n</div>\n\n<div class="showfloor text-center">\n\n')
        if len(list(all_item))>0:
            for item in all_item:
                __M_writer("\t\t<div class = 'item_container text-center'>\n\t\t\t<a href='/catalog/detail/")
                __M_writer(str(item.id))
                __M_writer('\'>\n\t\t\t\t<img class="hvr-glow" src=\'')
                __M_writer(str(STATIC_URL))
                __M_writer('catalog/media/product_images/')
                __M_writer(str(item.id))
                __M_writer(".png' />\n\t\t\t\t<div>\n\t\t\t\t\t <p>")
                __M_writer(str(item.name))
                __M_writer('<br>$')
                __M_writer(str(item.price))
                __M_writer("</p>\n\t\t\t\t</div>\n\t\t\t\t<div class = 'text-right'>\n\t\t\t </a>\n")
                if item.isRental:
                    __M_writer("\t\t\t\t<a href='/catalog/detail/")
                    __M_writer(str(item.id))
                    __M_writer("' class='btn btn-success'>View Details</a>\n")
                else:
                    __M_writer('\t\t\t \t<button data-pid="')
                    __M_writer(str(item.id))
                    __M_writer('" class=\' add_button btn btn-warning\'>Add to Cart</button>\n')
                __M_writer('\t\t\t</div>\n\t\t</div>\n')
        else:
            __M_writer('\t<h1>Sorry, there are no items that match your search.</h1>\n\n')
        __M_writer('</div>\n\n\n<!-- Modal -->\n      <div class="modal fade" id="add_to_cart" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\n        <div class="modal-dialog">\n          <div class="modal-content">\n            <div class="modal-header">\n              <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n              <h4 class="modal-title" id="myModalLabel">Login</h4>\n            </div>\n            <div class="modal-body">\n              ...\n            </div>\n            <div class="modal-footer">\n              <!--<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\n              <button type="button" class=" btn btn-primary">Save changes</button>-->\n            </div>\n          </div>\n        </div>\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/BlakeWoodward/CoHerFoun/catalog/templates/index.html", "source_encoding": "ascii", "uri": "index.html", "line_map": {"67": 9, "77": 9, "78": 21, "79": 22, "80": 23, "81": 24, "82": 24, "83": 25, "84": 25, "85": 25, "86": 25, "87": 27, "88": 27, "89": 27, "90": 27, "91": 31, "92": 32, "93": 32, "94": 32, "95": 33, "96": 34, "97": 34, "98": 34, "27": 0, "100": 39, "101": 40, "102": 43, "40": 1, "108": 102, "45": 7, "99": 36, "55": 5, "61": 5}}
__M_END_METADATA
"""
