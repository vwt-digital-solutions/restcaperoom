#!/usr/bin/env bash
docker run --rm -v ${PWD}:/local openapitools/openapi-generator-cli generate \
--skip-overwrite \
-i /local/restcaperoom.yaml \
-g python-flask \
-o /local
