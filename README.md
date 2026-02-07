# File Organizer

A robust Python script to organize your Downloads folder (or any directory) by file type.

## Features
- **Categorization**: Automatically moves files into `Images`, `Videos`, `Documents`, `Music`, `Compressed`, `Executables`, `Code`, and `Others`.
- **Safe Handling**: Handles duplicate filenames by renaming them (e.g., `file (1).txt`) instead of overwriting.
- **Web Interface**: Includes a simple local web interface for easy usage.
- **Portability**: Uses only standard Python libraries.

## Usage

### Command Line
1.  Run the script:
    ```bash
    python organize_downloads.py
    ```
2.  Enter the path to the directory you want to organize when prompted, or pass it as an argument:
    ```bash
    python organize_downloads.py "C:\Users\YourName\Downloads"
    ```

### Web Interface
1.  Start the web server:
    ```bash
    python app.py
    ```
2.  Open your browser to `http://localhost:8000`.
3.  Enter the directory path and click "Organize Files".

## Requirements
- Python 3.6+
