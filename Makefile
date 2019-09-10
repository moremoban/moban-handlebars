all: test

test:
	bash test.sh

document:
	bash document.sh

format:
	isort -y $(find moban_handlebars -name "*.py"|xargs echo) $(find tests -name "*.py"|xargs echo)
	black -l 79 moban_handlebars
	black -l 79 tests
	git diff

lint:
	sh lint.sh
