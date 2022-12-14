# Installation 

## Requirement:
Python 3.7

Jupyter Lab 3.1.18

conda 4.12.0

### Current libraries version list as below:
IPython          : 8.4.0

ipykernel        : 6.15.0

ipywidgets       : 7.7.1

jupyter_client   : 7.3.4

jupyter_core     : 4.10.0

jupyter_server   : 1.18.0

jupyterlab       : 3.1.18

nbclient         : 0.6.4

nbconvert        : 6.5.0

nbformat         : 5.4.0

notebook         : 6.4.12

qtconsole        : not installed

traitlets        : 5.3.0

## Installation:
### On Fedora36
#### Install nodejs
```
dnf module list nodejs
dnf module install nodejs:16
```
:::{note}
```dnf module install nodejs:<stream>
```
<stream> corresponds to the major version of Node.js. 
:::

### Install Yarn on Fedora
#### Install Yarn using NPM
```
sudo npm install yarn -g
```

##### Install Yarn via our RPM package 
```
curl --silent --location https://dl.yarnpkg.com/rpm/yarn.repo | sudo tee /etc/yum.repos.d/yarn.repo
sudo dnf install yarn
```

#### Install conda
```
bash Anaconda-latest-Linux-x86_64.sh
```

#### Activate the virtual environment:
```
conda create -n myenv python=3.7 
conda activate myenv 
```
Deactivate the virtual environment
```
conda deactivate
```

Delete Conda Environment:
```
conda env remove -n corrupted_env
```
or
```
conda env remove --name corrupted_env
```

#### Install packages
```
conda update ipython
conda install -c anaconda ipywidgets
conda install -c anaconda matplotlib
conda install -c anaconda pandas
conda install -c anaconda seaborn
```

#### Install jupyter lab
```
conda install -c conda-forge jupyterlab 
```			

Install specific Jupyterlab version
```
conda install -c conda-forge jupyterlab=3.1.18
```

##### Install patch
```
sudo dnf install patch
```


##### Install RISE:
```
pip install jupyterlab_rise
```
Source: https://github.com/jupyterlab-contrib/rise 

Update on 12/11/2022.



#### Install nbconvert
```
conda install nbconvert
```

#### Run jupyter lab
```
jupyter lab
```

### Fedora current version
$ jupyter lab --version
3.1.18
$ conda --version
conda 4.13.0
$ npm --version
8.5.5
$ yarn --version
1.22.19


## Installation on RHEL:

Install conda 
https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html

Install npm 
```
sudo dnf -y install epel-release
sudo dnf module list nodejs
sudo dnf -y module enable nodejs:16-epel
sudo dnf -y install nodejs
```
Install jupyter lab: 
```
conda install -c conda-forge jupyterlab 
```


##### RHEL current version:
$ jupyter lab --version
3.1.18
$ conda --version
conda 4.12.0
$ yarn --version
1.22.19
$ npm --version
8.3.1




