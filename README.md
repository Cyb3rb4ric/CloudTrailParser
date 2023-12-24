
# CloudTrail Parser for Splunk Integration

## Overview

This Python script is designed to parse AWS CloudTrail events into a format convenient for import into Splunk, a Security Information and Event Management (SIEM) system. Originally developed for Hack the Box challenge "OpTinselTrace-2," the script aims to streamline the extraction of CloudTrail logs and prepare them for efficient analysis within the Splunk environment.

## Usage

### Prerequisites

- Python 3.x
- Access to AWS CloudTrail logs in JSON format

### Instructions

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/cloudtrail-splunk-parser.git
    cd cloudtrail-splunk-parser
    ```

2. Execute the script with the path to the CloudTrail logs directory as an argument:

    ```bash
    python cloudtrail_parser.py /path/to/cloudtrail/logs
    ```

   Replace `/path/to/cloudtrail/logs` with the actual path to your CloudTrail logs.

3. The parsed CloudTrail records will be saved in a file named `cloudtrails.json` in the script's directory.

4. Import the generated `cloudtrails.json` file into Splunk for further analysis.

## Example

```bash
python cloudtrail_parser.py /path/to/cloudtrail/logs
```
## Contributing
If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
