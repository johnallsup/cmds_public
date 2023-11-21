#!/bin/bash
ME="$(readlink -f "$0")"
HERE="$(dirname "$ME")"
TARGET="$(dirname "$HERE")"
TARGET="${TARGET%/}"
alias rm=/bin/rm
rm -rf "$TARGET"/{bin,etc,stuff}
mkdir -p "$TARGET"/bin
for s in $HERE/*/; do
  [[ "$s" =~ ^Install|stuff|etc ]] && continue
  for t in "$s"/*; do
    [ -x "$t" ] && ln -s "$t" "$TARGET"/bin
  done
done
ln -vs "$HERE"/etc "$TARGET"
ln -vs "$HERE"/stuff "$TARGET"
