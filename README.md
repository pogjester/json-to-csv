# JSON to CSV Converter

This script converts a JSON file into a CSV file. The JSON file must be formatted as a list of dictionaries, where each dictionary represents a row in the CSV file.

## Prerequisites

- **Python**: Ensure you have Python installed on your system. You can verify this by running the following command in your terminal or command prompt:

  ```bash
  python --version
  ```

## Usage

1. **Prepare Your JSON File**: 
   - Ensure your JSON file is a list of dictionaries. Each dictionary should represent a row in the CSV file, and the keys of the dictionaries will be used as the CSV headers.

2. **Run the Script**:
   - Use the command line to execute the script. The script requires two arguments: the path to the input JSON file and the path where you want to save the output CSV file.

   ```bash
   python converter.py <input_json_file> <output_csv_file>
   ```

   Replace `<input_json_file>` with the path to your JSON file and `<output_csv_file>` with the desired path for the CSV output.

3. **Example**:
   - If your JSON file is named `data.json` and you want to save the CSV as `output.csv`, you would run:

   ```bash
   python converter.py data.json output.csv
   ```

## Error Handling

- If the JSON file does not contain a list of dictionaries, the script will raise a `ValueError`. Ensure your JSON data is correctly formatted to avoid this error.

By following these steps, you can successfully convert a JSON file to a CSV file using this script.