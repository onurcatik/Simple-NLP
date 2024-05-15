# NLP Project

## Overview

This project is a simple demonstration of Natural Language Processing (NLP) using Python. It includes functionality to transcribe speech into text using the Google Speech Recognition API and then process that text using the spaCy library for NLP tasks such as tokenization and part-of-speech tagging.

## Installation

To run this project, you need to have Python installed on your system. Additionally, install the required packages using pip:

```bash
pip install -r requirements.txt
```

You also need to download the English language model for spaCy:

```bash
python -m spacy download en_core_web_sm
```

## Usage

1. Run the `main.py` script:

```bash
python main.py
```

2. Once the script is running, speak into your microphone when prompted.
3. The program will transcribe your speech into text and then process it using spaCy.


