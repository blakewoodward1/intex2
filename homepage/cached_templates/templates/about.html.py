# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428355112.985997
_enable_loop = True
_template_filename = '/Users/BlakeWoodward/CoHerFoun/homepage/templates/about.html'
_template_uri = 'about.html'
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
        __M_writer('\n\n<title>About CHF</title>\n\n<br><br><br>\n<div class="canvas">\n<h1 align="center">Preserving America\'s founding values.</h1><br>\n<div class="about">\n<p >Lorem ipsum dolor sit amet, ut liber eruditi conceptam his. Alienum copiosae eos eu, est facer eruditi scripserit ea. Eu augue aperiri maiestatis sed, aliquid lucilius pertinacia in eos. Ea pri pertinax appellantur, id cum clita quando. Sint facer complectitur ius eu, laoreet mediocrem cu per.</p>\n\n<p >Usu quis deleniti an, timeam indoctum voluptaria et eam. Nemore dolores quo ne, id prima iisque suscipit pri, tale abhorreant at sea. Fuisset dolores imperdiet ne usu, homero dolores ad est. Et usu vocibus temporibus efficiantur, sit alia aperiri ut. Reque molestie praesent sit ut. Partiendo expetenda ne vel, delenit tractatos has id, novum necessitatibus no mei.</p>\n\n<p >In commune tacimates assueverit sit. Cetero admodum ei per, et vix legere voluptatum. Pri et viris aperiri, eu sit velit cetero habemus. Tamquam voluptatibus eu est, ei clita insolens sed. Ne probo tempor eum, an efficiendi instructior complectitur sea.</p>\n\n<p >Per ut duis vocibus. Id essent laoreet nam, in eum consul tibique, nec aperiam dolores quaestio at. Ad alterum minimum vim, ne usu lorem congue, sea mediocrem vulputate forensibus ad. Purto invenire at his. Sit te fuisset salutatus, eu vis wisi adolescens. Amet aeterno fastidii an eos, quo aperiam feugait ea.</p><br>\n</div>\n</div>\n\n<div class="images">\n<img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/about1.jpg" width="290px" alt="Colonial Heritage Foundation">\n<img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/about2.jpg" width="290px" alt="Colonial Heritage Foundation">\n<img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/about3.jpg" width="290px" alt="Colonial Heritage Foundation">\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/BlakeWoodward/CoHerFoun/homepage/templates/about.html", "source_encoding": "ascii", "uri": "about.html", "line_map": {"64": 58, "35": 1, "52": 3, "53": 22, "54": 22, "55": 23, "56": 23, "57": 24, "58": 24, "27": 0, "45": 3}}
__M_END_METADATA
"""
