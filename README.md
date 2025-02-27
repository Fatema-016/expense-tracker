# Expense Tracking Project

This project is a full-stack expense tracking application built using Python, MySQL, FastAPI, and Streamlit. It allows users to manage and track their expenses effectively.

## Features

* **Expense Management:** Add, view, and manage expenses.
* **Database Integration:** Uses MySQL for persistent data storage.
* **API Backend:** FastAPI provides a robust API for data access.
* **User-Friendly Frontend:** Streamlit creates an interactive and easy-to-use web interface.
* **Unit Testing:** Includes unit tests for the backend database helper.

## Project Structure

project-expense-tracking/
├── Backend/
│   ├── db_helper.py        # Database interaction logic
│   ├── server.py           # FastAPI application
│   └── .env                # Environment variables (database credentials) - DO NOT COMMIT
├── Frontend/
│   └── app.py              # Streamlit application
├── Test/
│   └── backend/
│       ├── test_db_helper.py # Unit tests
│       └── conftest.py       # pytest configuration
├── Database/
│   ├── expenses_db_creation.sql # SQL script to create the database schema
│   └── expenses_db.csv         # Sample expense data (optional)
├── .gitignore              # Files to ignore in Git
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation (this file)

## Setup Instructions

1.  **Clone the Repository:**

    ```bash
    git clone [https://github.com/Fatema-016/expense-tracker.git](https://github.com/Fatema-016/expense-tracker.git)
    cd expense-tracker
    ```

2.  **Set Up a Virtual Environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  # On Windows
    ```

3.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set Up MySQL Database:**

    * Install MySQL if you haven't already.
    * Create a database named `expense_manager`.
    * Run the `expenses_db_creation.sql` script to create the `expenses` table:

        ```bash
        mysql -u your_mysql_username -p expense_manager < Database/expenses_db_creation.sql
        ```

    * (Optional) If you want to use the sample data, import the `expenses_db.csv` file into the `expenses` table.

5.  **Configure `.env` File:**

    * Create a `.env` file in the `Backend/` directory with your MySQL credentials:

        ```env
        MYSQL_HOST=localhost
        MYSQL_USER=your_mysql_username
        MYSQL_PASSWORD=your_mysql_password
        MYSQL_DATABASE=expense_manager
        ```

    * **Important:** Never commit your `.env` file to GitHub!

6.  **Run the Backend (FastAPI):**

    ```bash
    cd Backend
    uvicorn server:app --reload
    ```

7.  **Run the Frontend (Streamlit):**

    ```bash
    cd ../Frontend
    streamlit run app.py
    ```

8.  **Access the Application:**

    * Open your web browser and go to the URL displayed by Streamlit (usually `http://localhost:8501`).

## Running Tests

To run the unit tests for the backend:

```bash
cd .. # go back to the project root
pytest ./Test/backend/

## License

This project is licensed under the MIT License.
    
    
