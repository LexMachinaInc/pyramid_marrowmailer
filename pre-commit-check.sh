#!/bin/bash
# TODO: stash changes before doing tests: http://codeinthehole.com/writing/tips-for-using-a-git-pre-commit-hook/

function handle_exit {
    if [ $? -ne 0 ]; then
        EXITCODE=1
    fi
}

echo '====== Running tests ========='
nosetests src/pyramid_marrowmailer; handle_exit

echo '====== Running pep8 =========='
pycodestyle src/pyramid_marrowmailer; handle_exit
pycodestyle ./*.py; handle_exit
