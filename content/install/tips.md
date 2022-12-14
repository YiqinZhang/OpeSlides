# Tips

## Requirement:
Python 3.7
Jupyter Lab 3.1.18
conda 4.12.0


Install specific Jupyterlab version

(Downgrade jupyterlab version)
```
conda install -c conda-forge jupyterlab=3.1.18
```

### Bugs with Yarn
1.'command `build` not found'

This error is due to not installing the ‘patch’ yet.
Solution: **Install patch**
```
sudo dnf install patch
```

2. Cannot complete `yarn install`
command failed with exit code 127.
Solution: 
Getting rid of the node_modules folder entirely (rm -rf node_modules from the root folder),
```
rm -rf node_modules
```

