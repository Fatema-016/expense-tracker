## Expense Management System
This project is an expense management system that consists of a Streamlit frontend application and a FastAPI backend server.

### Project Structure

- **frontend/** : Contains the Streamlit application code.
- **backend/** : Contains the FastAPI backend server code.
- **tests/**:Contains the test cases for both frontend and backend.
- **requirements.txt**:Lists the required Python packages.
- **README.md**:Provides an overview and instructions for the project.



## Setup Instructions

1.  **Clone the repository:**

    ```shell
    git clone [https://github.com/Fatema-016/expense-management-system](https://github.com/Fatema-016/expense-management-system)
    cd expense-management-system
    ```

2.  **Install dependencies:**

    ```python
    pip install -r requirements.txt
    ```

3.  **Run the FastAPI server:**

    ```shell
    uvicorn server:app --reload
    ```
4.  **Run the Streamlit app:**
    ```shell
    streamlit run frontend/app.py
    ```
    
    
