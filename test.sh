pip freeze
nosetests --with-coverage --cover-package moban_handlebars --cover-package tests tests  docs/source moban_handlebars && flake8 . --exclude=.moban.d,docs --builtins=unicode,xrange,long
