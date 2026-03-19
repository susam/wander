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

dist:
	git checkout main || :
	git branch -df wander || :
	git checkout -b wander
	git rm *.md Makefile .gitignore
	VER=$$(grep VERSION index.html | head -n 1 | cut -d "'" -f2);
	git commit -m "Create distributable bundle for Wander $VER"
	git push -f cb wander
	git push -f gh wander
	ls -l
	git checkout main
