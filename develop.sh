#!/bin/sh
cd ..
mkdir hkust-leetcode-gitbook
cd hkust-leetcode-gitbook
git init
git remote add origin https://github.com/KellyHwong/leetcode-datastructure.git
git fetch
git checkout gh-pages
cd ../leetcode-datastructure
cd source
gitbook install
cd ..

