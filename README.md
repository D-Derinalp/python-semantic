# Garden Path Sentences

This is a Python project that imports Spacy and ready to run on Docker. 
It has sensible defaults for security.

## Table of Contents
1. Requirements
2. Setup
3. What does the project do?
4. Contribute

## 1. Requirements
- Python 3.7 or later versions
- Docker

## 2. Setup

Firstly install [Docker](https://docs.docker.com/get-docker/) on your computer.
Now launch pycharm and configure a project on this working directory.
All following commands must be run only once at project installation.

The first clone of the repository:

```bash
$ git clone https://github.com/D-derinalp/python-semantic.git
$ cd python-semantic
```

Then install the all dependencies:
```bash
$ pip install -r requirements.txt
```

### Docker Image
Run the following command to create docker image:

```bash
docker build -t python-semantic .
```

To create docker container you should run the image with following command:

```bash
docker run python-semantic
```

## 3. What does the project do?

This project imports SpaCy and Natural Language Processing (NLP) and includes examples about semantic similarities.
It uses 'en_core_web_md' language model to compare words (example 1 and 2)
and sentences (example 3) and find similarities.



## 4. Contribute

Contributions are always welcome! 