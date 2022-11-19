# Based Linter

A linter for Python, in Python, created in ~8 hours for Northeastern IWC's 2022 hackathon.

## What it does
* identify biased & non-inclusive language in plaintext and variable names (drawing from various best-practice style guides)
* suggest alternative phrasing
* complain at you for using certain pre-train word embedding libraries with undesirable biases

## How it does
* parse Python code into abstract syntax tree
* check different types of content in the code (strings, names, imports)
* output a list of bias warnings

## More resources
* [Word Embeddings Fairness Evaluation Framework](https://wefe.readthedocs.io/en/latest/)
* [NPM "Alex"](https://www.npmjs.com/package/alex)
* [Google developer docs style guide](https://developers.google.com/style/word-list)
