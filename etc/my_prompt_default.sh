#!/bin/bash
color_prompt=yes
_my_prompt_func() {
  local U N M K UC HC
  # we want the first 5 users to get same host colour as username
  # next we advance one mod 5
  ((U=(UID-1000)))
  ((N=U%5))
  ((K=U/5))
  ((M=(N+K)%5))
  ((UC=N+2))
  ((HC=M+2))
  if [ "$color_prompt" = yes ]; then
    BASE_PS1='\n($(echo $?))\[\033[01;3'$UC'm\]\u\[\033[01;3'$HC'm\]@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\n\[\033[01;34m\]\W\[\033[00m\] \$ '
  else
    BASE_PS1='\u@\h:\w\$ '
  fi
  PS1="${BASE_PS1}"
}
_my_prompt_func

set_term_title_prompt() {
  PS1="\[\033];\h:\w\007\]""$BASE_PS1"
}
unset_term_title_prompt() {
  PS1="$BASE_PS1"
}
set_term_title_prompt
