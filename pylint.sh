#!/bin/bash
pylint -f parseable --ignore-patterns="env/" * | tee pylint.out
