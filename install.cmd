@Echo off


conda create -n benfordvenv python=3.12
conda activate benfordvenv
pip install python-docx
pip install python-pptx

pip install python-docx



pip install PyPDF2

pip install benfordsLaw

set /P var123="Enter the path to the directory where you want to install the repo: "
cd /d %var123%

git clone https://github.com/Nerk0s/BenfordProject.git