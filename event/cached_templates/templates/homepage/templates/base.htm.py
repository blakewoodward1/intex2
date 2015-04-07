# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428430419.31273
_enable_loop = True
_template_filename = '/Users/BlakeWoodward/CoHerFoun/homepage/templates/base.htm'
_template_uri = '/homepage/templates/base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['title', 'content']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<!DOCTYPE html>\n<html>\n\n\n\n\n<head>\n    <meta charset="UTF-8">\n    <meta name="description" content="Website for the COlonial Heritage Foundation">\n    <meta name="keywords" content="Colonial Heritage Foundation, CHF, Festival">\n    <meta name="author" content="shoopes2">\n      \n    <title>\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\n    </title>\n    \n')
        __M_writer('    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\n    <script src="')
        __M_writer(str( STATIC_URL))
        __M_writer('homepage/media/jquery.form.js"></script>\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>\n    <link rel="shortcut icon" href="/favicon.ico" type="image/x-icon">\n     <link rel="icon" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('favicon.ico" type="image/x-icon">\n    <script src="')
        __M_writer(str( STATIC_URL))
        __M_writer('homepage/scripts/loadmodal.js"></script>\n    <script src="')
        __M_writer(str( STATIC_URL))
        __M_writer('catalog/scripts/shopping_cart.js"></script>  \n\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\n  \n  </head>\n  <body>\n\n<script>\n  (function(i,s,o,g,r,a,m){i[\'GoogleAnalyticsObject\']=r;i[r]=i[r]||function(){\n  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),\n  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)\n  })(window,document,\'script\',\'//www.google-analytics.com/analytics.js\',\'ga\');\n\n  ga(\'create\', \'UA-51767348-3\', \'auto\');\n  ga(\'send\', \'pageview\');\n\n</script>\n\n<div class="navbar navbar-default navbar-fixed-top">\n  <div class="navbar-header">\n    <a class="navbar-brand" href="/homepage/index#">Home</a>\n  </div>\n  <div class="navbar-collapse collapse navbar-inverse-collapse">\n    <ul class="nav navbar-nav">\n      <li><a href="/homepage/about#">About</a></li>\n      <li><a href="/event/">Events</a></li>\n      <li><a href="/catalog#">Products</a></li>\n      <li><a href="/homepage/contact#">Contact</a></li>\n      <form class="navbar-form navbar-left" role="search">\n        <div class="form-group">\n          <input type="text" id=\'keywords\' class="form-control" placeholder="Products & Rentals">\n        </div>\n        <a href=\'#\' id=\'keywordBtn\' class="btn btn-default">Search</a>\n      </form>\n    </ul>\n  <div class="navbar-collapse collapse navbar-inverse-collapse">\n    <ul class="nav navbar-nav navbar-right">\n\n')
        if request.user.is_authenticated():
            __M_writer('      <li class="dropdown">\n            <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false"> Welcome, ')
            __M_writer(str( request.user.get_full_name() ))
            __M_writer('<span class="caret"></span></a>\n            <ul class="dropdown-menu" role="menu">\n              <li><a href="/account"><span class="glyphicon glyphicon-user" aria-hidden="true"></span> Account Info</a></li>\n              \n\n')
            if request.user.has_perm(True):
                __M_writer('              <li><a href="/account/admin#"><span class="glyphicon glyphicon-list" aria-hidden="true"></span> Admin</a></li>\n')
            else:
                __M_writer('              <li class="divider"></li>\n')
            __M_writer('      \n              <li><a href="/homepage/login.logout_view/"><span class="glyphicon glyphicon-log-out" aria-hidden="true"></span> Logout</a></li>\n            </ul>\n          </li>\n')
        else:
            __M_writer('      <li><a href="/account/edit.create#"><span class="glyphicon glyphicon-plus" aria-hidden="true"></span> Create Account</a></li>\n      <li><a id=\'show_login_dialog\' href=\'#\'> Log in <span class="glyphicon glyphicon-log-in" aria-hidden="true"></span></a></li>\n')
        __M_writer('\n    </ul>\n  </div>\n  </div>\n</div>\n\n\n      <!-- Modal -->\n      <div class="modal fade" id="login_dialog" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\n        <div class="modal-dialog">\n          <div class="modal-content">\n            <div class="modal-header">\n              <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n              <h4 class="modal-title" id="myModalLabel">Login</h4>\n            </div>\n            <div class="modal-body">\n              ...\n            </div>\n            <div class="modal-footer">\n              <!--<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\n              <button type="button" class="btn btn-primary">Save changes</button>-->\n            </div>\n          </div>\n        </div>\n      </div>\n\n<!-- Modal -->\n      <div class="modal fade" id="add_to_cart" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\n        <div class="modal-dialog">\n          <div class="modal-content">\n            <div class="modal-header">\n              <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n              <h4 class="modal-title" id="myModalLabel">Login</h4>\n            </div>\n            <div class="modal-body">\n              ...\n            </div>\n            <div class="modal-footer">\n              <!--<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\n              <button type="button" class=" btn btn-primary">Save changes</button>-->\n            </div>\n          </div>\n        </div></div>  \n\n\n\n\n       <!-- <li><a href = \'/homepage/login\'>Login2</a>-->\n\n      </ul>\n    </div><!-- /.navbar-collapse -->\n  </div><!-- /.container-fluid -->\n</nav>\n\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n        </div>\n    </div>\n  </body>\n\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\n        Colonial Heritage Foundation\n      ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer(' \n       <br><br>\n      ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "/homepage/templates/base.htm", "line_map": {"64": 84, "65": 86, "66": 90, "67": 91, "68": 94, "73": 150, "79": 20, "16": 4, "18": 0, "85": 20, "91": 148, "30": 2, "31": 4, "32": 5, "97": 148, "36": 5, "103": 97, "41": 22, "42": 26, "43": 27, "44": 27, "45": 31, "46": 31, "47": 32, "48": 32, "49": 33, "50": 33, "51": 36, "52": 36, "53": 36, "54": 38, "55": 38, "56": 38, "57": 74, "58": 75, "59": 76, "60": 76, "61": 81, "62": 82, "63": 83}, "filename": "/Users/BlakeWoodward/CoHerFoun/homepage/templates/base.htm", "source_encoding": "ascii"}
__M_END_METADATA
"""
