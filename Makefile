checks:
	sed 's/ method="dialog"//' index.html > /tmp/tmp.html
	tidy -q -e --warn-proprietary-attributes no /tmp/tmp.html
	npx standard --plugin html index.html

deps:
	npm install --no-save standard eslint-plugin-html
	if command -v brew; then brew install tidy-html5; fi

push:
	git remote remove cb || :
	git remote remove gh || :
	git remote add gh ssh://git@github.com/susam/wander.git
	git remote add cb ssh://git@codeberg.org/susam/wander.git
	git push cb main
	git push gh main
