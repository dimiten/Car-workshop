# Car-workshop

My second project for ITBootcamp.

A backend application for a car-workshop.

NOTE: If you are using my data for this project (see caption *__Database__* bellow), in order to have access to all routes, use **_Login Employee_** route with email: **_mstanicic@gmail.com_** and password: **_mstanicic_**

## Installation

### Create virtual environment
#### PyCharm
```bash
venv ./venv
```
#### Windows
Open Command Prompt or PowerShell, navigate to project folder and run
```bash
python -m venv ./venv
```
#### Linux/MacOS
Open terminal, navigate to project directory and run
```bash
python -m venv ./venv
```
In case that previous command didn't work, install virtualenv
```bash
pip install virtualenv
```
Run command in project directory to create virtual env
```bash
virtualenv venv
```
### Activate Virtual environment
Open terminal and navigate to project directory, then run

| Platform | Shell      | Command to activate virtual environment |
|----------|------------|-----------------------------------------|
| POSIX    | bash/zsh   | $ source venv/bin/activate              |
|          | fish       | $ source venv/bin/activate.fish         |
|          | csh/tcsh   | $ source venv/bin/activate.csh          |
|          | PowerShell | $ venv/bin/Activate.ps1                 |
| Windows  | cmd.exe    | C:\> venv\Scripts\activate.bat          |
|          | PowerShell | PS C:\> venv\Scripts\Activate.ps1       |

### Dependencies
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.
```bash
pip install -r requirements.txt
```
### Database
1) Start MySQL server and execute all commands in **_init_db/init_db.sql_**
2) Make sure that you are using **_car_workshop_** database and then, in the same place, or in MySQL Workbench, execute all commands in **_init_db/data.sql_**


### Environment variables
1. Create new file **_.env_**
2. Copy all consts from **env-template** to **_.env_**
3. Assign values to const in .env file


## Run server
From terminal:
```bash
python -m uvicorn app.main:app --reload --reload-delay 5 --host localhost --port 8000
```
From PyCharm:
```bash
uvicorn app.main:app --reload --reload-delay 5 --host localhost --port 8000
```
From main in PyCharm:

You can also run this app in the main module by pressing the green triangle next to the command **_if __name__ == "__main__":_**, or on the green triangle in the top-right corner. If you are getting an error when running the app this way, press the **_main_** word next to the green triangle at the top-right corner (where you also run the app), and press **_Edit configurations..._**. Make sure that the working directory is right (it should be a path where this project is stored)

## License

[GNU](https://www.gnu.org/licenses/gpl-3.0.en.html)