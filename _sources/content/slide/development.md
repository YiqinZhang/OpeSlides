development

Jupyter extension development

Doc
https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html

Tutorial
https://jupyterlab.readthedocs.io/en/stable/extension/extension_tutorial.html#extension-tutorial


Prerequisites
Python >= 3.7
Node.js >= 12 (LTS version preferred)
VSCode, download from here
(Optional) Note: We'll be using conda as a virtual environment, see here for instructions on installation of conda
 

 Run this command to create a new environment named jupyterlab-ext.
conda create -n jupyterlab-ext --override-channels --strict-channel-priority -c conda-forge -c nodefaults jupyterlab=3 cookiecutter nodejs jupyter-packaging git


activate the new environment so that all further commands you run work out of that environment.
conda activate jupyterlab-ext


Yiqin env
(jupyterlab-ext) node -v
v6.11.2
(jupyterlab-ext) npm -v
3.10.10

 
Create an extension project¶
use cookiecutter to get a quick project structure.
cookiecutter https://github.com/jupyterlab/extension-cookiecutter-ts

Cookiecutter will prompt you for a few fields of information. Pick the frontend option and fill the remaining fields out as follows:

Select kind:
1 - frontend
2 - server
3 - theme
Choose from 1, 2, 3 [1]: 1
author_name []: Your Name
author_email []: your@name.org
labextension_name [myextension]: jupyterlab_apod
python_name [myextension]: jupyterlab_apod
project_short_description [A JupyterLab extension.]: Show a random NASA Astronomy Picture of the Day in a JupyterLab panel
has_settings [n]: n
has_binder [n]: y
repository [https://github.com/github_username/myextension]: https://github.com/github_username/jupyterlab_apod





cd jupyterlab_apod
ls


Import 
Inside of src/index.ts add these lines after the first import:
import { ICommandPalette } from '@jupyterlab/apputils';
import { INotebookTracker, NotebookActions } from '@jupyterlab/notebook';
import { IMainMenu } from '@jupyterlab/mainmenu';
import { Menu } from '@lumino/widgets';


Run the following lines of code in your terminal:
jlpm add @jupyterlab/notebook
jlpm add @jupyterlab/mainmenu
jlpm add @lumino/widgets
jlpm
jlpm build



Commands 
After the console.log('JupyterLab extension snippetsexample is activated!') line add the following lines of code:

const { commands } = app; 

commands.addCommand('openLink', { 
  label: 'Documentation', 
  caption: 'Documentation', 

  execute: () => { 
    const win = window.open('https://jupyterlab.readthedocs.io/en/stable/', '_blank'); 
    win?.focus(); 
  } 
}); 

commands.addCommand('printHelloWorld', { 
  label: 'Hello World!', 
  caption: 'Hello World!', 

  execute: () => { 
    const current = tracker.currentWidget; 
    const notebook = current!.content; 
    NotebookActions.insertBelow(notebook); 
    const activeCell = notebook.activeCell; 
    activeCell!.model.value.text = 'print("Hello World!")'; 
  } 
}); 
 
commands.addCommand('printTest', { 
  label: 'Test', 
  caption: 'Test', 

  execute: () => { 
    const current = tracker.currentWidget; 
    const notebook = current!.content; 
    NotebookActions.insertBelow(notebook); 
    const activeCell = notebook.activeCell; 
    activeCell!.model.value.text = 'print("Test")'; 
  }
});



