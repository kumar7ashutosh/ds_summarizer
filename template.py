import os,logging
from pathlib import Path

logging.basicConfig(level=logging.INFO,format='[%(asctime)s] : %(message)s')

project_title="datascience_summarizer"
list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_title}/__init__.py",
    f"src/{project_title}/components/__init__.py",
    f"src/{project_title}/utils/__init__.py",
    f"src/{project_title}/utils/common.py",
    f"src/{project_title}/logging/__init__.py",
    f"src/{project_title}/config/__init__.py",
    f"src/{project_title}/config/configuration.py",
    f"src/{project_title}/pipeline/__init__.py",
    f"src/{project_title}/entity/__init__.py",
    f"src/{project_title}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]
for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    
    if filedir!="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory: {filedir} for {filename}")
    
    if(not(os.path.exists(filepath)) or (os.path.getsize(filepath)==0)):
        with open(filepath,'w') as f:
            pass
            logging.info(f"creating {filepath}")
        
    else:
        logging.info(f" {filename} already exists")    
        