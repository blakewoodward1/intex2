# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428430284.780055
_enable_loop = True
_template_filename = '/Users/BlakeWoodward/CoHerFoun/homepage/templates/contact.html'
_template_uri = 'contact.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


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
    return runtime._inherit_from(context, 'homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
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
        __M_writer = context.writer()
        __M_writer('\n<br><br><br>\n\n<title>Contact CHF</title>\n\n<div class="canvas">\n<h1 align="center">Questions or Comments? Contact Us</h1><br>\n\n<table class = "table table-condensed table-hover">\n  <tr>\n    <th><p>Physical Address:</p></th>\n    <td><p>1425 N University Ave, Provo, UT 84604</p></td>\n  </tr>\n  <tr>\n    <th><p>Phone Number 1:</p></th>\n    <td><p>801-704-1776</p></td>\n  </tr>\n  <tr>\n    <th><p>Phone Number 2:</p></th>\n    <td><p>801-432-9818</p></td>\n  </tr>\n  <tr>\n    <th><p>Email:</p></th>\n    <td><p>support@chfgroup.us</p></td>\n  </tr>\n</table>\n\n<div class="map">\n<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3045.07592168341!2d-111.64931600000003!3d40.251844000000006!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x874d90bc4aa0b68d%3A0xbf3eb3a3f30fdc4c!2sBrigham+Young+University!5e0!3m2!1sen!2sus!4v1428361438099" width="550" height="400" frameborder="0" style="border:0"></iframe></div><hr><br><br><br>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "contact.html", "line_map": {"34": 1, "51": 3, "39": 33, "57": 51, "27": 0, "45": 3}, "filename": "/Users/BlakeWoodward/CoHerFoun/homepage/templates/contact.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
