# Dialog Simulation between Two Models

This project simulates a dialog between two models, Anna and Bob, who are placed in an entirely white, empty world. The models think and speak based on their defined personalities and the context of the conversation.

## Project Structure

- `dialog_en.py`: The main script that runs the dialog simulation and saves the results to markdown files.

## Requirements

- Python 3.x
- `llama_index` library

## Installation

1. Clone the repository:

```sh
    git clone https://github.com/kirdeinega/AI_dialog
    cd <repository-directory>
```

2. Install the required dependencies:

```sh
    pip install -r requirements.txt
```

## Installing Ollama

To download and install Ollama, follow these steps:

1. Download Ollama from the official website: [ollama.com](https://ollama.com)
2. Follow the installation instructions for your operating system.
3. Install and run the model:

```sh
   ollama run llama3.1:8b
```

After installing Ollama, ensure it is properly configured and available for use in your project.

## Usage

To run the dialog simulation, execute the `dialog_en.py` script:

```sh
python dialog_en.py
```

The script will generate three markdown files: `dialog_full.md`, `dialog_anna.md`, and `dialog_bob.md`, containing the dialog between Anna and Bob. These files will be created in the project directory after running the script locally.

- `dialog_full.md`: The complete dialog between Anna and Bob.
- `dialog_anna.md`: The dialog from Anna's perspective.
- `dialog_bob.md`: The dialog from Bob's perspective.
