# cmds
/usr/jda/cmds

This is how I organise my bashrc and similar. Ultimately all the executable scripts end up in `/usr/jda/bin`, and
are put there by the `install.sh` script. `/usr/jda/cmds` is under version management to keep sync'd between my machines.
So `/usr/jda/etc` is symlinked to `/usr/jda/cmds/etc` and in reverse, `/usr/jda/rustbin`, `/usr/jda/local/bin` and so on
are there so that everything ultimately ends up symlinked to something in `/usr/jda/bin` so that only `/usr/jda/bin` needs
to go into the `PATH` variable. There are then a number of `dot commands`. I like to previs them with `.` to avoid
namespace collisions with anything else. for example `.s name` loads `/usr/jda/stuff/name.stuff`. I then organise my
`.bashrc` into small well-defined chunks. For example `cargo` config goes in `/usr/jda/stuff/cargo.stuff`, and
anaconda stuff goes in `/usr/jda/stuff/conda.stuff`. Many of these are loaded by default, or possibly if something
is present (i.e. if `nvm` is present, load `nvm.stuff` else don't) and so on.

I wrote this for me, and it is shared in case anyone else is interested. This is just how I do it for the curious.

Ultimately this ends up with a  `.bashrc` that sources `/usr/jda/etc/bash_paths.bashrc`, then exists if noninteractive
(so that my personal `PATH` is set up for all shells), and then `/usr/jda/etc/bash_common.bashrc`. This in turn
pulls in the various `.stuff` files and a few other things. For example there is a `pathif` that appends or prepends
a directory to the `PATH`, but *only if it exists*. There is an old `tidypath` script written in PERL which takes
the `PATH`, removes duplicate entries, adds anything specified on the command line, and filters out any nonexistent directories.
The problem there when setting up a new machine is a) what happens if I forget to put `tidypath` in `/usr/local/bin` or
b) if I don't have Perl installed, as may happen in a minimal VM designed for containers. Thus at some point I'll replace
tidypath with a bash function.

At some later time I'll investigate `zsh` as that's the defacto shell on Apple and has some nice features. Also other shells
like `fish` and `nu` will get played with at some time. Ramble over.
