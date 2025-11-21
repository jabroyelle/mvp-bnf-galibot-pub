#!/bin/bash
DOIT () {
	echo "executing : $*"
	$*
}

DOIT orchestrate chat stop
DOIT orchestrate server stop

