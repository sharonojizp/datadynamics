# DataDynamics

DataDynamics is a Python program designed to manage and analyze data storage efficiently on Windows systems. It uses advanced algorithms to scan directories, summarize storage usage, and provide optimization suggestions.

## Features

- **Storage Analysis:** Scans a specified directory and calculates the size of each file.
- **Optimization Suggestions:** Provides suggestions for optimizing storage based on file size.
- **Analysis Saving:** Saves the analysis summary into a JSON file for future reference.
- **System Memory Information:** Retrieves and logs system memory details.

## Requirements

- Python 3.x
- Required Python libraries: `os`, `psutil`, `json`, `logging`

You can install the required library using pip:

```bash
pip install psutil
```

## Usage

1. Modify the `directory_to_analyze` variable in the script to point to the directory you want to analyze.
2. Run the script using Python:

   ```bash
   python datadynamics.py
   ```

3. The program will output the storage analysis and optimization suggestions in the console and save the analysis in `storage_analysis.json`.

## Logging

DataDynamics uses Python's built-in logging module to provide detailed information about its operations. Logs are displayed in the console with timestamps and log levels.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.