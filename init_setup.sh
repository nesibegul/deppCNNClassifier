echo [$(date)]: "START"
echo [$(date)]: "creating the env with python 3.0 version"
conda create --prefix ./env python=3.8 -y
echo [$(date)]: "activating the environment"
source activate ./env
echo [$(date)]: "installing the requirements_dev"
pip install -r requirements_dev.txt
echo [$(date)]: "END"