### Enable and Setup Python Env on VsCode:

```
- On Windows:
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process 
  py -3 -m venv .venv    
  .venv\scripts\activate

- On Linux:
  python3 -m venv .venv    
  source .venv/bin/activate

- To install a package in the workspace:
  python -m pip install <package-name>
```

### START/STOP MS SQL SERVICE (CMD or PowerShell):

```
- Open CMD in Administrator mode:
  net start SQLServerAgent
  net stop SQLServerAgent    

- Open PowerShell:
  Get-Service -Name MSSQLSERVER
  Set-Service -Name MSSQLSERVER -Status Running -PassThru
  Get-Service -Name MSSQLSERVER

```