all: test

test: 
	bash test.sh

install_test:
	pip install -r tests/requirements.txt

git-diff-check:
	git diff --exit-code

lint:
	bash lint.sh

format:
	isort -y $(find moban_handlebars -name "*.py"|xargs echo) $(find tests -name "*.py"|xargs echo)
	black -l 79 moban_handlebars
	black -l 79 tests

git-diff-check:
	git diff --exit-code
