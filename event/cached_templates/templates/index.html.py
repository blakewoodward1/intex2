# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428429613.045879
_enable_loop = True
_template_filename = '/Users/BlakeWoodward/CoHerFoun/event/templates/index.html'
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
        len = context.get('len', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        list = context.get('list', UNDEFINED)
        all_event = context.get('all_event', UNDEFINED)
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
        __M_writer('\n  Events and Festivals\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        len = context.get('len', UNDEFINED)
        all_event = context.get('all_event', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context)
        list = context.get('list', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<br><br><br>\n\n<title>Events</title>\n\n<div class="jumbotron">\n  <h1 >Upcoming Events</h1>\n  <p >Eum clita partem admodum ea, vel et nibh aliquam. Cu nam probo option, ei inani euismod maluisset ius. Graeci percipit has eu. Nisl nulla appareat usu cu, ei iusto quidam nam, doctus incorrupte vel ad. Graece libris prodesset vel eu, ne homero latine posidonium his.</p>\n\n</div>\n\n<div class="showfloor text-center">\n\n')
        if len(list(all_event))>0:
            for event in all_event:
                __M_writer('\t<div class="item_container text-center">\n\n\t\t<a href="/event/detail/')
                __M_writer(str(event.id))
                __M_writer('"><img class="hvr-glow" src="')
                __M_writer(str(STATIC_URL))
                __M_writer('event/media/images/')
                __M_writer(str(event.id))
                __M_writer('.png" /></a>\n\n\t\t<div>\n\t\t<div>\n\t\t<h3 style="color: #5C5959">')
                __M_writer(str(event.name))
                __M_writer('</h3>\n\t\t<h3 style="color: #5C5959">')
                __M_writer(str(event.startDate))
                __M_writer('</h3>\n\t\t</div>\n\t\t</div>\n\t</div>\n')
        else:
            __M_writer('\t<h1>Sorry, there are no events</h1>\n')
        __M_writer('</div>\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "index.html", "line_map": {"67": 7, "77": 7, "78": 20, "79": 21, "80": 22, "81": 24, "82": 24, "83": 24, "84": 24, "85": 24, "86": 24, "87": 28, "88": 28, "89": 29, "90": 29, "91": 34, "92": 35, "93": 37, "27": 0, "40": 1, "45": 5, "99": 93, "55": 3, "61": 3}, "filename": "/Users/BlakeWoodward/CoHerFoun/event/templates/index.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
