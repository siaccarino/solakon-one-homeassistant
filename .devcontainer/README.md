# dev container

Purpose:

* Analyse and understand Solakon ONE Hacs integration
* Test functionality

It is a Ubuntu 24.04 LTS container with a basic python environment aimed to be used in WSL2 or native linux together with vscode.

## Prepare devcontainer

Add the following lines to your .bashrc or .zshrc file:

```bash
export UID=$(id -u)
export GID=$(id -g)
```

This is required to adapt the user inside of the rootless devcontainer to by synchronized with your host user.

Adapt container.env to your runtime environment

Your .ssh and .gitconfig settings are mounted into the container to allow git operations.
