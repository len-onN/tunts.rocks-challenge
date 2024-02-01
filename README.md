# Tunts.Rocks Challenge Repository

Welcome to the Tunts.Rocks Challenge repository! This repository contains the code for a specific challenge.

## Getting Started

Follow the steps below to clone this repository to your local machine.

### Prerequisites

Make sure you have Git installed on your machine. If not, you can download it from [https://git-scm.com/](https://git-scm.com/).

### Cloning the Repository

Open your terminal or command prompt.

```bash
git clone git@github.com:len-onN/tunts.rocks-challenge.git
```

### Changing Directory

Navigate into the cloned repository using the fallowing command:

```bash
cd tunts.rocks-challenge
```

# Creating a Virtual Environment with venv

## Introduction
A virtual environment is a self-contained directory that contains its own Python interpreter and libraries. This allows you to work on a specific project with its own dependencies without interfering with the system-wide Python installation.

## Prerequisites
Make sure you have Python installed on your system. Python 3.3 and newer come with the `venv` module, which is a lightweight alternative to `virtualenv`.

## Step 1: Open Terminal or Command Prompt
Open your terminal or command prompt. You can find it in your operating system's applications or search menu.

## Step 2: Navigate to Your Project Directory
Use the `cd` command to navigate to the directory where you want to create your virtual environment. For example:

```bash
cd tunts.rocks-challenge
```

## Step 3: Create a Virtual Enviroment
Run the fallowing command to create a virtual envrioment:

#### On Linux or macOS:

```bash
python3 -m venv .venv
```
#### On Windows:

```bash
python -m venv .venv
```

This command creates a directory named 'venv' that contains a copy of the Python interpreter
and a 'lib' (o 'Lib' on Windows) directory with a minimal Python Installation.

## Step 4: Activate the Virtual Enviroment
Activate the virtual enviroment using the appropriate command for you operating system:

#### On Linux or macOS:

```bash
source venv/bin/activate
```

#### On Windows:

```bash
venv\Scripts\activate
```

You should see the virtual enviroment name in your command prompt or terminal, indicating
that it's currently active.

## Step 5: Install Dependencies from 'requirements.txt'
Once the virtual enviroment is active, it's time to install the required dependencies for the given project.
In order to achieve it, it's necessary o use the 'pip install' command for the 'requirements.txt':

```bash
pip install -r requirements.txt
```

## Step 6: Running the code - reading, processing and updating a given xlsx spreadsheet file!
In order to run the code, and fill the fields "Situação" and "Nota para Aprovação Final" execute the fallowing commands in your prompt, or terminal:

```bash
python app.py
```

## Step 7: Deactivate the Virtual Enviroment
Once finished the update of the spreadsheet, it's time to deactivate the virtual enviroment:

```bash
deactivate
```

## Introduction to gspread Library
The code in this repository utilizes the gspread library, a Python library that simplifies the interaction with Google Sheets. It allows for reading and writing data to Google Sheets, making it convenient for handling spreadsheet data in a Google Sheets environment. To explore more about gspread, refer to the  [gspread documentation](https://docs.gspread.org/en/latest/index.html).
