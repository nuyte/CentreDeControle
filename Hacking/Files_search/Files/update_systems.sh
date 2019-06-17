#!/bin/bash

cd "$(brew --repo)" && git fetch && git reset --hard origin/master && brew update
brew update
brew upgrade


conda search --outdated
conda update -n ENVIRONMENT --all


