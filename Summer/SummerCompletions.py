import sublime, sublime_plugin, os

MYSNIPPET = """\
namespace('${1:%(packages)s}');

//===========================================================================
// CLASS
//===========================================================================
$1.${2:%(name)s} = function() {

    //=======================================================================
    // PRIVATE MEMBERS
    //=======================================================================
    var that = this;

    //=======================================================================
    // PUBLIC MEMBERS
    //=======================================================================
    this.${3:methodName} = function(${4}) {
        ${0}
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

class SummerCompletions(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        if not view.match_selector(locations[0], "source.js, text"):
            return []

        snippet = (MYSNIPPET % { "packages": self.packages(view), "name": self.name(view) })
        return [("namespace\tcreate a summer class", snippet)]

    def packages(self, view):
        result = "summer.controllers"
        path = view.file_name();
        if None != path:
            print path
            path = path.replace(os.sep,".")
            
            folders = [".javascripts.",".javascript.'", ".js."]
            end = path.rfind(self.name(view)) - 1

            for folder in folders:
                if -1 != path.rfind(folder):
                    start = path.rfind(folder) + len(folder)
                    result = path[start : end]

        return result

    def name(self, view):
        result = "ClassName"
        path = view.file_name();
        if None != path:
            start  = path.rfind(os.sep) + 1;
            end = path.rfind(".");
            result = path[start : end]
        return result
