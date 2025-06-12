# Python Generators with MySQL

## 📚 Project Overview

This project demonstrates how to use Python generators to efficiently stream data from a MySQL database one row at a time. It also includes setup for creating and populating a database with user data from a CSV file.


## ⚙️ Features

- Connects to a MySQL database using `mysql-connector-python`
- Creates a database and table (`user_data`) if they don't exist
- Reads user data from a CSV file (`user_data.csv`)
- Inserts data into the table while avoiding duplicates
- Streams rows one at a time using a Python generator
- Uses environment variables to securely manage credentials


## 📁 Project Structure

python-generators-0x00/
├── .env # Environment variables (NOT pushed to Git)
├── .gitignore # Git ignore file to hide sensitive files
├── seed.py # Main logic to handle DB and generator
├── 0-main.py # Script to run and test the generator
└── user_data.csv # Sample user data


## 🔧 Requirements

- Python 3.6+
- MySQL Server running locally
- Install dependencies:

```bash
pip install mysql-connector-python python-dotenv
```

### 🛠️ 1. Setup Instructions
Create your .env file

```env
  DB_HOST=localhost
  DB_USER=root
  DB_PASSWORD=yourpassword
```
### 2. Ensure .env is in your .gitignore file

```gitignore
.env
```
### 3. Add your CSV data

Create user_data.csv with this structure:
```csv
name,email,age
John Doe,john@example.com,30
Jane Smith,jane@example.com,25
```
### 4. Make the script executable (Linux/macOS)
```bash
./0-main.py
```
### 5. Run the project from Bash
```bash
./0-main.py
```

✅ Expected Output
- Confirmation of database and table creation

- Successful data insertion from CSV

- First 5 rows from the table

- Streaming rows one at a time using generator

❌ Error Handling
- Handles missing or malformed CSV rows

- Skips rows with fewer than 3 fields

- Detects missing `.env` or MySQL errors and logs clearly

