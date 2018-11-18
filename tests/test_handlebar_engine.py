import os

from nose.tools import eq_
from moban.plugins import ENGINES, BaseEngine
from moban_handlebars.engine import EngineHandlebars


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
    assert engine.engine_cls == EngineHandlebars


def test_handlebars_file_tests():
    output = "test.txt"
    path = os.path.join("tests", "fixtures", "handlebars_tests")
    engine = BaseEngine([path], path, EngineHandlebars)
    engine.render_to_file("file_tests.template", "file_tests.json", output)
    with open(output, "r") as output_file:
        content = output_file.read()
        eq_(content, "here")
    os.unlink(output)
