# Helpful Stuff a.k.a a notebook of usefulness :P #


### 1. Bash Commands ###



### 2. Git Commands ###

- Usual Workflow:
    ```bash
    git add /path/to/directories
    git commit -m "this is a commit"
    git status

    # If there are local changes that you want to keep...
    git stash 

    # else run merging
    git pull

    git push
    ```
- Shows the status of all files 
    ```bash 
    git status
    ```
- Useful .gitignore templates
    - Ignore certain file extensions:
        ```bash
        *.pkl
        *.csv
        *.pyc
        ```
    - Ignore certain directories:
        ```bash
        .pycache/

        #Use this to ignore caches by dash
        cache/
        ```
    


### 3. Anaconda / Conda ###

##### 3.1 Spyder #####
- Issue: Spyder does not start (no splash screen shown)
    - Fix: Install pyqt again (conda install pyqt)
            (Somehow, conda does not handle this well?)

##### 3.2 Some useful python packages #####

- Web Development
    - flask
    - flask_caching

- Plotting:
    - dash dash-core-components dash-html-components dash-table-experiments
    - mpld3 ?

