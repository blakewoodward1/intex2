# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428088732.331026
_enable_loop = True
_template_filename = 'C:\\Python34\\Projects\\CHF\\catalog\\templates/rest.html'
_template_uri = 'rest.html'
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
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n\n\n  <head>\n    <title>REST API Example</title> \n    <script src="//ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script> \n    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css"> \n    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap-theme.min.css">\n    <script src="//netdna.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>\n  </head>\n\n  ')
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
        __M_writer = context.writer()
        __M_writer('\n  <body style="padding: 2em;">\n    <h1>REST API Example</h1>\n    <pre>\n    <!--Endpoint: http://dithers.cs.byu.edu/iscore/api/v1/charges\n    Valid credit card: Visa, 4732817300654, Exp. 10/15, CVC 411, Cardholder Name: Cosmo Limesandal\n    Sample Charge Creation:\n    curl http://dithers.cs.byu.edu/iscore/api/v1/charges \\ -d apiKey=YOUR_API_KEY ')
        __M_writer('    -d currency=usd ')
        __M_writer('    -d amount=5.99 \\ -d type=Visa ')
        __M_writer('    -d number=4732817300654 ')
        __M_writer('    -d exp_month=10 \\ -d exp_year=15 ')
        __M_writer('    -d cvc=411 \\I\n    -d "name=Cosmo Limesandal" \\ -d "description=Charge for cosmo@is411.byu.edu"\n    Query Charges:\n    curl --get http://dithers.cs.byu.edu/iscore/api/v1/charges ')
        __M_writer('    -d apiKey=YOUR_API_KEY-->\n    </pre>\n    <button type="button" class="btn btn-primary" id="charge">Charge</button>\n    <input type="text" id="chargeId">\n    <br/>\n    <div id="message"></div> \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Python34\\Projects\\CHF\\catalog\\templates/rest.html", "line_map": {"34": 1, "51": 21, "52": 22, "53": 23, "54": 24, "55": 25, "56": 29, "27": 0, "44": 13, "50": 13, "62": 56}, "source_encoding": "ascii", "uri": "rest.html"}
__M_END_METADATA
"""
