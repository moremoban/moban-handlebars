from moban_handlebars.helpers import HandlebarHelper
from moban_handlebars.partials import register_partial

register_partial("header", "<h1>People</h1>")


@HandlebarHelper("list")
def _list(this, options, items):
    result = [u"<ul>"]
    for thing in items:
        result.append(u"<li>")
        result.extend(options["fn"](thing))
        result.append(u"</li>")
    result.append(u"</ul>")
    return result
