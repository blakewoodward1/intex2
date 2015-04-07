# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423171579.219206
_enable_loop = True
_template_filename = 'C:\\Python34\\Projects\\CHF\\homepage\\templates/historical_figure.html'
_template_uri = 'historical_figure.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['header', 'content', 'title']


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
        def header():
            return render_header(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        all_figure = context.get('all_figure', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        all_figure = context.get('all_figure', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\t<html>\r\n\t\t<body>\r\n\t\t\t<h2> Historical Figures</h2>\r\n\r\n\r\n\t\t\t<div class = "text-right">\r\n\t\t\t\t<a href="/homepage/historical_figure.create/" class ="btn btn-warning">\r\n\t\t\t\t Create New Historical Figure</a>\r\n\t\t\t</div>\r\n\t\t\t<br>\r\n\r\n\t\t\t<table class="table table-striped table-bordered">\r\n\t\t\t\t<tr>\r\n\t\t\t\t\t<th>ID</th>\r\n\t\t\t\t\t<th>Name</th>\r\n\t\t\t\t\t<th>Birth Date</th>\r\n\t\t\t\t\t<th>Birth Place</th>\r\n\t\t\t\t\t<th>Death Date</th>\t\r\n\t\t\t\t\t<th>Death Place</th>\t\t\t\t\r\n\t\t\t\t\t<th>Biographical Note</th>\r\n\t\t\t\t\t<th>Fictional</th>\r\n\t\t\t\t\t<th>Actions</th>\r\n\r\n\t\t\t\t</tr>\t\t\t\r\n')
        for figure in all_figure:
            __M_writer('\r\n\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(figure.id))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(figure.name))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(figure.birth_date))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(figure.birth_place))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(figure.death_date))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(figure.death_place))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(figure.biographical_note))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(figure.is_fictional))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td><a href="/homepage/historical_figure.edit/')
            __M_writer(str(figure.id))
            __M_writer('/">Edit</a>\r\n\t\t\t\t\t\t|\r\n\t\t\t\t\t\t <a href="/homepage/historical_figure.delete/')
            __M_writer(str(figure.id))
            __M_writer('/">Delete</a></td>\r\n\r\n\t\t\t\t\t</tr>\r\n')
        __M_writer('\r\n\t\t\t</table>\r\n\r\n\t</html>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n\tUsers\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "historical_figure.html", "source_encoding": "ascii", "line_map": {"65": 57, "71": 7, "78": 7, "79": 33, "80": 34, "81": 36, "82": 36, "83": 37, "84": 37, "85": 38, "86": 38, "87": 39, "88": 39, "89": 40, "90": 40, "27": 0, "92": 41, "93": 42, "94": 42, "95": 43, "96": 43, "97": 44, "98": 44, "91": 41, "100": 46, "101": 50, "39": 1, "107": 3, "44": 5, "99": 46, "49": 55, "113": 3, "119": 113, "59": 57}, "filename": "C:\\Python34\\Projects\\CHF\\homepage\\templates/historical_figure.html"}
__M_END_METADATA
"""
