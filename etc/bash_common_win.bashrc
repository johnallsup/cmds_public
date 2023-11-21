# make less more friendly for non-text input files, see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

.if() { for s; do [ -f "$s" ] && { . "$s"; }; done; }
.stuff() { 
  if [ $# = 0 ]; then
    ( cd "$JDA"/stuff; ls *.stuff | cut -f1 -d.; )
  else
    for s; do 
      [ -e "$JDA"/stuff/"$s".stuff ] && . "$JDA"/stuff/"$s".stuff; 
    done; 
  fi
}
alias .s=.stuff
.s cmds
.s dircolors
.s completion
.s cd
.s mpd
.s hist
.s mvdesc
.s cygwin
.s git
.s ssh
.s antlr
.s python
.s x11
.s shopt
.s perl
.s stuff
.s aliases
.s dot_commands
.s clip
.s cargo
.s nvm
.s go
.s win
.s winvim
.s my_stuff
. my_prompt
complete -c viw catw batw lessw

PATH="$("$JDA"/bin/tidypath "$PATH")"

.if "$HOME/.bash_aliases"
