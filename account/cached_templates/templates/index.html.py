# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428370319.995797
_enable_loop = True
_template_filename = '/Users/BlakeWoodward/CoHerFoun/account/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'title']


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
        user = context.get('user', UNDEFINED)
        activeUser = context.get('activeUser', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\n\n\n')
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
        user = context.get('user', UNDEFINED)
        activeUser = context.get('activeUser', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<br><br><br>\n   <h1>Welcome to your account!</h1>\n   <h3>\n\n   <table class="table table-hover">\n   <tr>\n   <th><p>Username:</th>\n   <td>')
        __M_writer(str(activeUser.username))
        __M_writer('</td></p>\n   </tr>\n\n   <tr>\n   <th><p>First Name:</th>\n   <td>')
        __M_writer(str(activeUser.first_name))
        __M_writer('</td></p>\n   </tr>\n\n   <tr>\n   <th><p>Last Name:</th>\n   <td>')
        __M_writer(str(activeUser.last_name))
        __M_writer('</td></p>\n   </tr>\n\n   <tr>\n   <th><p>Email Address:</th>\n   <td>')
        __M_writer(str(activeUser.email))
        __M_writer('</td></p>\n   </tr>\n\n   <tr>\n   <th><p>Is Superuser?:</th>\n   <td>')
        __M_writer(str(activeUser.is_superuser))
        __M_writer('</td></p>\n   </tr>\n   </table>\n   </h3>\n \n\n    <!-- Modal -->\n      <div class="modal fade" id="modal_change_password" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\n        <div class="modal-dialog">\n          <div class="modal-content">\n            <div class="modal-header">\n              <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n              <h4 class="modal-title" id="myModalLabel">Login</h4>\n            </div>\n            <div class="modal-body">\n              ...\n            </div>\n            <div class="modal-footer">\n              <!--<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\n              <button type="button" class="btn btn-primary">Save changes</button>-->\n            </div>\n          </div>\n        </div>\n      </div>\n\n   <a class=\'btn btn-success\' href="/account/edit.edit/')
        __M_writer(str(user.id))
        __M_writer('/">Edit</a>\n   <a class = \'btn btn-success\' href=\'#\' id=\'change_password\'>Change Password</a>\n\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\n  Account Home\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/BlakeWoodward/CoHerFoun/account/templates/index.html", "uri": "index.html", "source_encoding": "ascii", "line_map": {"64": 21, "65": 21, "66": 26, "67": 26, "68": 31, "69": 31, "38": 1, "71": 36, "72": 61, "73": 61, "43": 5, "79": 3, "91": 85, "53": 8, "85": 3, "27": 0, "70": 36, "61": 8, "62": 16, "63": 16}}
__M_END_METADATA
"""
