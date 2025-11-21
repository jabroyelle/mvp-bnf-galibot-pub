#!/bin/bash

DOIT () {
        echo ">>>> $*"
        $*
}

## First start rancher

DOIT orchestrate server start -l --env-file .env
DOIT orchestrate env activate local
cd mvp-bnf-galibot

DOIT orchestrate knowledge-bases import -f knowledge_base/essentials_data.yaml
DOIT orchestrate knowledge-bases import -f knowledge_base/exhibition_data.yaml
DOIT orchestrate knowledge-bases import -f knowledge_base/galica_data.yaml
DOIT orchestrate agents import -f agents/BNF_librarian_agent.yaml
DOIT orchestrate agents import -f agents/Documentalist_agent.yaml
DOIT orchestrate agents import -f agents/Exhibition_agent.yaml
DOIT orchestrate agents import -f agents/galibo_agent.yaml
