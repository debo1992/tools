# Tools
Building some tools to set up a working environment

## Add color to console

Edit your `~/.bashrc` (or `/root/.bashrc` if working as root) and add the following:

```bash
# Enable colors in prompt
export PS1="\[\e[32m\]\u\[\e[0m\]@\h:\[\e[34m\]\w\[\e[0m\]\[\e[31m\]\($(__git_ps1 ' (%s)'))\[\e[0m\]# "
```
then run  ` source ~/.bashrc`

