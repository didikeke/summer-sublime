import sublime, sublime_plugin

MYSNIPPET = \
"""
namespace('${1:%(packages)s}');

$1.${2:${TM_FILENAME/(.*)[.](.*)/$1/g}} = function() {

    var that = this;

    this.${3:methodName} = function() {
        ${4}
    };

};

//===========================================================================
// STATIC METHODS
//===========================================================================
$1.$2.__instance = new $1.$2();

$1.$2.getInstance = function() {
    return $1.$2.__instance;
};

""" 

class SummerCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        packages = self.view.file_name()
        # self.view.run_command("insert_snippet", {"name": "Packages/Summer/namespace.sublime-snippet"})
        self.view.run_command("insert_snippet", { "contents" : (MYSNIPPET % \
            { "packages": packages }) })
    

