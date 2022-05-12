Step to run application locally:
Step 1: Create the copy of hte project.
Step 2: Open command prmpt and change your current path to folder where you can find 'app.py' file.
Step 3: Create environment by command given--
conda create -name <environment name>
Step 4: Activate environment by command--
conda activate <environment name>
Step 5: Install tesseract using windows installer avail at: https://github.com/UB-Mannheim/tesseract/wiki
Step 6: Note the tesseract path from the installation. Default installation path at the time of this edit was:"D:\ mini-Project\/ It may change so please check the installation path
Step 7: pytesseract.pytesseract.tesseract_cmd = 
r'C:\Program Files\Tesseract-OCR\tesseract.exe'
Step 8: Use command to install dependencies--
pytnon -m pip install -r requirements.txt
Step 9: Run application by command-
python app.py
You'll get URL, copy it and paste in browser 
Step 10: You've sample_data folder where you can get image to test.