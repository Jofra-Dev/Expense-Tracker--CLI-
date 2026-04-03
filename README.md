# Expense Tracker CLI

A professional Command Line Interface (CLI) application for personal
financial management. This project features a state-based navigation
system, CRUD operations for financial records, and an AI-powered
financial advisor integration.

## Features

-   **Financial Dashboard:** Clear visualization of all income and
    expenses in a formatted table.
-   **Data Persistence:** All records are stored and managed in a local
    `finances.json` file.
-   **Complete CRUD:** Functionalities to Add, Remove, and Edit entries
    with automatic ID reindexing.
-   **Smart Sorting:** Organize data chronologically by date or
    alphabetically by category.
-   **AI Financial Advisor:** Integration with OpenRouter API
    (Qwen/Gemini models) to analyze spending habits and provide
    actionable savings tips.
-   **Security:** Environment variable support for API key protection.

## Project Structure

-   `main.py`: The entry point of the application containing the state
    machine and menu loops.
-   `functions.py`: Core logic, including JSON handling, data
    manipulation, and API requests.
-   `finances.json`: Database file for storing transaction records.
-   `.env`: Configuration file for sensitive credentials (API Keys).

## Installation

### Clone the repository:

``` bash
git clone https://github.com/Jofra-Dev/expense-tracker-cli.git
cd expense-tracker-cli
```

### Install dependencies:

This project requires `requests` for API communication and
`python-dotenv` for environment variable management.

``` bash
pip install requests python-dotenv
```

### Setup Environment Variables:

Create a `.env` file in the root directory and add your OpenRouter API
key:

``` env
OPENROUTER_API_KEY=your_api_key_here
```

## Usage

Run the application using Python:

``` bash
python main.py
```

## Navigation Guide

-   **Main Menu:** Access the Dashboard, the Editor Sub-menu, the AI
    Agent, or Sorting options.
-   **Editor Menu:** Manage your data. Choose to add new launches,
    remove existing ones by ID, or update specific details of a record.
-   **Sorting:** Select between Category or Date to reorder your local
    database.
-   **Agent AI:** Automatically sends your current `finances.json` data
    to the AI for a professional financial audit.

## Data Schema

The application manages data using the following JSON structure:

``` json
{
    "id": 1,
    "type": "Gain/Expense",
    "category": "Category Name",
    "name": "Item Description",
    "value": 0.00,
    "date": "MM-DD-YYYY"
}
```

## Important Security Note

Do not commit your `.env` file to version control systems like GitHub.
Ensure that `.env` is included in your `.gitignore` file to prevent
leaking your API credentials.

## License

This project is intended for educational purposes and personal portfolio
use.
