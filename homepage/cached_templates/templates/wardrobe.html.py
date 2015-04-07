# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428089668.448503
_enable_loop = True
_template_filename = 'C:\\Python34\\Projects\\CHF\\homepage\\templates/wardrobe.html'
_template_uri = 'wardrobe.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['title', 'content', 'header']


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
        def title():
            return render_title(context._locals(__M_locals))
        all_wardrobe = context.get('all_wardrobe', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
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


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n\tWardrobe Items\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        all_wardrobe = context.get('all_wardrobe', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\t<html>\r\n\t\t<body>\r\n\t\t\t<h2> Wardrobe Items</h2>\r\n\t\t\t<div class = "text-right">\r\n\t\t\t\t<a href="/homepage/wardrobe.create/" class ="btn btn-warning">\r\n\t\t\t\t Create New Wardrobe Item</a>\r\n\t\t\t</div>\r\n\t\t\t<br>\r\n\t\t\t<table class="table table-striped table-bordered">\r\n\t\t\t\t<tr>\r\n\t\t\t\t\t<th>ID</th>\r\n\t\t\t\t\t<th>Name</th>\r\n\t\t\t\t\t<th>Size</th>\r\n\t\t\t\t\t<th>Modifier Name</th>\r\n\t\t\t\t\t<th>Gender</th>\r\n\t\t\t\t\t<th>Color</th>\t\r\n\t\t\t\t\t<th>Pattern</th>\t\t\t\t\r\n\t\t\t\t\t<th>Start Date</th>\r\n\t\t\t\t\t<th>Actions</th>\r\n\r\n\t\t\t\t</tr>\t\t\t\r\n')
        for wardrobe in all_wardrobe:
            __M_writer('\r\n\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(wardrobe.id))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(wardrobe.name))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(wardrobe.size))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(wardrobe.sizeModifier))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(wardrobe.gender))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(wardrobe.color))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(wardrobe.pattern))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(wardrobe.start_year))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td><a href="/homepage/wardrobe.edit/')
            __M_writer(str(wardrobe.id))
            __M_writer('/">Edit</a>\r\n\t\t\t\t\t\t|\r\n\t\t\t\t\t\t <a href=\'/homepage/wardrobe.delete/')
            __M_writer(str(wardrobe.id))
            __M_writer("/'>Delete</a></td>\r\n\r\n\t\t\t\t\t</tr>\r\n")
        __M_writer('\r\n\t\t\t</table>\r\n\r\n\t</html>\r\n\r\n')
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


"""
__M_BEGIN_METADATA
{"filename": "C:\\Python34\\Projects\\CHF\\homepage\\templates/wardrobe.html", "line_map": {"65": 3, "71": 7, "78": 7, "79": 30, "80": 31, "81": 33, "82": 33, "83": 34, "84": 34, "85": 35, "86": 35, "87": 36, "88": 36, "89": 37, "90": 37, "27": 0, "92": 38, "93": 39, "94": 39, "95": 40, "96": 40, "97": 41, "98": 41, "91": 38, "100": 43, "101": 47, "39": 1, "107": 54, "44": 5, "99": 43, "49": 52, "113": 54, "119": 113, "59": 3}, "source_encoding": "ascii", "uri": "wardrobe.html"}
__M_END_METADATA
"""
