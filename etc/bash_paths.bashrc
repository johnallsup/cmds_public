# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

. "$JDA"/stuff/pathif.stuff
for s in "$JDA"/stuff /usr/npm/bin "$JDA"/cmds/sbin "$JDA"/bin "$HOME/.local/bin" "$HOME"/bin; do
  if [[ "$s" =~ etc/$ ]]; then continue; fi
  pathif -p "$s"
done
for s in "$HOME/perl5/bin" "/usr/local/go/bin"; do
  pathif -a "$s"
done
PATH="$("$JDA/"bin/tidypath -c -p)"
export PYTHONPATH="$("$JDA/"bin/tidypath -c "$HOME/.python:$PYTHONPATH")"
export VISUAL=vi EDITOR=vi
