# ORGANIZE IMAGES BY EXIF DATE
<hr>

**Step 1:** Create a virtual environment

```
python -m venv <env_name>
```

**Step 2:** Activate the virtual environment

```
source <env_name>/bin/activate
```
*The name of the activated environment will appear on the left of the prompt.* 

**Step 3:** Install the packages

```
conda env create -f environment.yml
```

Required arguments:

| Parameter                 | Default       | Description   |	
| :------------------------ |:-------------:| :-------------|
| -p --path 	       |	/           |Path to your images folder


# Required tools

[python 3.9](https://www.python.org/download/releases/3.9/)

[pillow 8.3.1](https://pypi.org/project/Pillow/8.3.1/)

[pip v21.2.4](https://pypi.org/project/pip/)
