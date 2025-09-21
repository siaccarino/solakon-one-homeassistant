# Prepare devcontainer

Add the following lines to your .bashrc or .zshrc file:

```bash
export UID=$(id -u)
export GID=$(id -g)
```

This is required to adapt the user inside of the rootless devcontainer to by synchronized with your host user.

Adapt container.env to your runtime environment
