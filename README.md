# NT Transliteration Tool
An internal tool for transliteration for speech team (currently based on IndicXlit)

## How to run Transliteration scripts (For first time setup please refer to next section- git clone is different; has submodules)
-   `conda activate <translit-env>`
-   `cd IndicXlit/inference/cli/`
-   `python3 transliterate_task.py /path/to/input.csv /path/to/output.csv <lang-id>`

## Steps for first time setup (skip this section if already setup)

### Git clone repo and submodules
-   `git clone --recurse-submodules https://github.com/navana-tech/nt_translit.git`
-   `cd nt_translit`
-   Optionally to get access to latest version of submodules `git submodule update --remote`
-   `cd ../`

### Virtual environment and dependencies
-   `conda create --name <translit-env>`
-   `conda activate <translit-env>`
-   `conda install -n <translit-env> pip `
-   `python -m pip install indic-nlp-library `
-   `cd fairseq `
-   `python -m pip install --editable ./`
-   `cd ../`
-   `conda deactivate`

### Download model and setup for run
-   `cd IndicXlit/inference/cli/`
-   `ln -s ../../../transliterate_task.py .`
-   `mkdir source output`
-   Download suitable model version (zipped) `wget https://github.com/AI4Bharat/IndicXlit/releases/download/v1.0/indicxlit-en-indic-v1.0.zip`
-   unzip the model `unzip indicxlit-en-indic-v1.0.zip`
-   `cd ../../../`

### To test setup is working fine
-   `conda activate <translit-env>`
-   `cd IndicXlit/inference/cli/`
-   `echo "i n d i a" > source/source.txt`
-   `python3 transliterate_task.py source/source.txt output/final_transliteration.txt  hi`
-   `cat output/final_transliteration.txt `
-   should see output `india:	इंडिया`
