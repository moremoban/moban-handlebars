import fs.path

from .utils import Docs


class TestRegression(Docs):
    def setUp(self):
        super(TestRegression, self).setUp()
        self.base_folder = fs.path.join("tests", "regression_tests")

    def test_helper_and_partial(self):
        expected = (
            "<h1>People</h1>"
            + "<ul><li>Bill 100</li><li>Bob 90</li><li>Mark 25</li></ul>"
        )

        folder = "level-11-helpers-and-partials"
        self.run_moban(
            [
                "moban",
                "-pd",
                "helper_and_partial",
                "-c",
                "data.json",
                "--template-type",
                "hbs",
                '{{>header}}{{#list people}}{{name}} {{age}}{{/list}}',
            ],
            folder,
            [("moban.output", expected)],
        )
