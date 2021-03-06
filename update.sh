#!/bin/sh
git add -A
git commit -am "逆波兰表达式 `date`"
git push
if which gitbook > /dev/null; then
    cd source
    gitbook build
    cd _book
    cp -R * ../../../hkust-leetcode-gitbook/
    cd ../../../hkust-leetcode-gitbook/
    git checkout gh-pages
    git add -A
    git commit -am "update `date`"
    git push
else
    echo "Gitbook not installed."
fi
