import os

from moban.plugins import ENGINES
from moban_handlebars.engine import EngineHandlebars

from nose.tools import eq_


def test_handlebars_template_not_found():
    path = os.path.join("tests", "fixtures", "handlebars_tests")
    engine = EngineHandlebars([path])
    template = engine.get_template("file_tests.template")
    data = dict(test="here")
    result = engine.apply_template(template, data, None)
    expected = "here"
    eq_(expected, result)


def test_handlebars_template_type():
    engine = ENGINES.get_engine("hbs", [], "")
    assert engine.engine.__class__.__name__ == "EngineHandlebars"


def test_handlebars_file_tests():
    output = "test.txt"
    path = os.path.join("tests", "fixtures", "handlebars_tests")
    engine = ENGINES.get_engine("hbs", [path], path)
    engine.render_to_file("file_tests.template", "file_tests.json", output)
    with open(output, "r") as output_file:
        content = output_file.read()
        eq_(content, "here")
    os.unlink(output)


def test_handlebars_string_template():
    template_string = "{{test}}"
    output = "test.txt"
    path = os.path.join("tests", "fixtures", "handlebars_tests")
    engine = ENGINES.get_engine("hbs", [path], path)
    engine.render_string_to_file(template_string, "file_tests.json", output)
    with open(output, "r") as output_file:
        content = output_file.read()
        eq_(content, "here")
    os.unlink(output)
