# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428431048.826574
_enable_loop = True
_template_filename = '/Users/BlakeWoodward/CoHerFoun/homepage/templates/index.html'
_template_uri = 'index.html'
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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n<title>Colonial Heritage Foundation</title>\n<br><br><br>\n\n<img class="displayed" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/CHF_Logo.png" alt="Flag" width="400px"><br>\n <img class="displayed" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/13_star_us_flag-1920x1080.jpg" alt="Flag" width="800px">\n\n <h1 align="center">Preserving the values, culture, skills and history of Americas founding</h1><br><br><br>\n\n <table class="table table-bordered ">\n     <tr class="active">\n        <td class="text-center col-md-2">\n    <h2 class="bar2 text-center">Blog</h2>\n    <p>Lorem ipsum dolor sit amet, ut liber eruditi conceptam his. Alienum copiosae eos eu, est facer eruditi scripserit ea. Eu augue aperiri maiestatis sed, aliquid lucilius pertinacia in eos. Ea pri pertinax appellantur, id cum clita quando. Sint facer complectitur ius eu, laoreet mediocrem cu per.\n\n</p>\n  \n    </td>\n\n    <td class="text-center col-md-2">\n    <h2 class="bar2 text-center">Social Media</h2>\n    <p>Lorem ipsum dolor sit amet, ut liber eruditi conceptam his. Alienum copiosae eos eu, est facer eruditi scripserit ea. Eu augue aperiri maiestatis sed, aliquid lucilius pertinacia in eos. Ea pri pertinax appellantur, id cum clita quando. Sint facer complectitur ius eu, laoreet mediocrem cu per.\n    </p>\n    <a href=""><span class="glyphicon glyphicon-phone" aria-hidden="true"></span></a> |\n    <a href=""><span class="glyphicon glyphicon-globe" aria-hidden="true"></span></a> |\n    <a href=""><span class="glyphicon glyphicon-thumbs-up" aria-hidden="true"></span></a>\n    \n    </td>\n\n    <td class="text-center col-md-2">\n    <h2 class="bar2 text-center">Staff</h2>\n    <p>Lorem ipsum dolor sit amet, ut liber eruditi conceptam his. Alienum copiosae eos eu, est facer eruditi scripserit ea. Eu augue aperiri maiestatis sed, aliquid lucilius pertinacia in eos. Ea pri pertinax appellantur, id cum clita quando. Sint facer complectitur ius eu, laoreet mediocrem cu per.\n    </p>\n  \n      </tr>\n</table>\n\n\n <!-- Modal\n<div class="modal fade" id="login_dialog" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\n  <div class="modal-dialog">\n    <div class="modal-content">\n      <div class="modal-header">\n        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n        <h4 class="modal-title" id="myModalLabel">Modal title</h4>\n      </div>\n      <div class="modal-body">\n        ...\n      </div>\n      <div class="modal-footer">\n        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\n        <button type="button" class="btn btn-primary">Save changes</button>\n      </div>\n    </div>\n  </div>\n</div> -->\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "index.html", "line_map": {"35": 1, "52": 3, "53": 8, "54": 8, "55": 9, "56": 9, "27": 0, "45": 3, "62": 56}, "filename": "/Users/BlakeWoodward/CoHerFoun/homepage/templates/index.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
