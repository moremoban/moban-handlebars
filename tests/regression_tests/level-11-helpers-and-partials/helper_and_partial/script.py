from moban_handlebars.api import Helper, register_partial

register_partial("header", "<h1>People</h1>")


@Helper("list")
def _list(this, options, items):
    result = [u"<ul>"]
    for thing in items:
        result.append(u"<li>")
        result.extend(options["fn"](thing))
        result.append(u"</li>")
    result.append(u"</ul>")
    return result
