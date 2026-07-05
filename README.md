# Telegram Channel Transfer Tool

This project consists of two Python scripts that enable you to transfer Telegram channels and groups that you follow from one account to another. The first script exports the list of channels and groups to a `.txt` file, while the second reads this file and adds these channels and groups to another Telegram account.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup](#setup)
  - [Clone the Repository](#clone-the-repository)
  - [Install Dependencies](#install-dependencies)
- [How to Get Telegram API Credentials](#how-to-get-telegram-api-credentials)
- [Proxy Configuration](#proxy-configuration)
- [Usage](#usage)
  - [Using Wrapper Scripts (Recommended)](#using-wrapper-scripts-recommended)
  - [Export Channels](#export-channels)
  - [Import Channels](#import-channels)

## Prerequisites

1. **Python 3.x** - Download and install it from [here](https://www.python.org/downloads/).
2. **Telegram Account** - You should have an existing Telegram account.
3. **Git** (Optional) - Download and install it from [here](https://git-scm.com/) if you wish to clone the repository.

## Setup

### Clone the Repository

If you've never used Git before, you'll need to install it first. Download and install Git from [here](https://git-scm.com/download/win) if you're on Windows or follow instructions for other operating systems as outlined on the official site.

Once Git is installed, proceed with the following steps to clone this repository to your local machine:

1. Open your terminal (Command Prompt on Windows, Terminal on macOS or Linux).
2. Navigate to the folder where you would like to download this project to. Use the `cd` command to navigate to your desired folder. For example:

    ```bash
    cd path/to/your/folder
    ```

3. Once you're in the folder, copy and paste the following command into your terminal and press Enter:

    ```bash
    git clone <repository_link>
    ```

Replace `<repository_link>` with the URL of this GitHub repository, which you can find by clicking the green 'Code' button near the top right of the GitHub repository page.

### Install Dependencies

This project relies on `uv` for fast and reliable dependency management.

1. Ensure you have Python installed.
  
2. Install `uv` if you haven't already. You can install it globally via pip:
   
    ```bash
    pip install uv
    ```
  
3. Navigate to the project folder where the `requirements.txt` file is located:

    ```bash
    cd path/to/cloned/repository
    ```
  
4. Use `uv` to create a virtual environment and install the required dependencies (including `telethon` and `python-socks` for proxy support):

    ```bash
    uv venv
    uv pip install -r requirements.txt
    ```

This will automatically create a `.venv` directory and install all the necessary packages.

## How to Get Telegram API Credentials

Before you proceed, you'll need the `api_id` and `api_hash` from Telegram. Follow these steps:

1. Go to [Telegram's Developer website](https://my.telegram.org/auth).
2. Log in with your Telegram account.
3. Click on "API development tools".
4. Fill out the form to create a new application.
5. You will be given an `api_id` and an `api_hash`. Keep these safe.

## Proxy Configuration

If you need a proxy to access the Telegram API, you can configure it via the `proxy_config.json` file in the root directory:

```json
{
  "use_proxy": true,
  "proxy_url": "http://127.0.0.1:10808"
}
```

Set `use_proxy` to `true` and update `proxy_url` to your HTTP proxy address. The `python-socks` dependency is required (and included if you use the updated project environment) to enable proxy support.

## Usage

### Using Wrapper Scripts (Recommended)

To simplify the execution and automatically apply your proxy settings, you can use the included wrapper scripts:

- **Windows PowerShell (Recommended for Windows):** Run `.\run.ps1`
- **Linux / macOS / Git Bash:** Run `./run.sh`

The wrapper script will provide an interactive menu to easily choose between exporting or importing channels.

### Export Channels

To export channels from your Telegram account, run the export script:

1. Navigate to the directory where the script is located.
2. Open your terminal and run:

\`\`\`bash
python <export_script_name>.py
\`\`\`

3. Follow the prompts to enter your `api_id`, `api_hash`, and phone number.

The list of channels and groups will be saved in a file named `channels.txt`.

### Import Channels

To import the channels to another Telegram account, run the import script:

1. Navigate to the directory where the script is located.
2. Open your terminal and run:

\`\`\`bash
python <import_script_name>.py
\`\`\`

3. Follow the prompts to enter your `api_id`, `api_hash`, and phone number.

The channels will be added to your Telegram account.
