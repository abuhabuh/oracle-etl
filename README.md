# Overview

Python client for interfacing with Oracle database using cx_Oracle package


# Setup

## Python 

1. create dir drivers/ and download and unzip Oracle Client normal and SDK packages into the drivers folder: drivers/libclntshcore.dylib.12.1
  * update env.sh to match the folder name of the drivers you downloaded
  * probably need to `ln -s` libclntsh.dylib.12.1 and libclntshcore.dylib.12.1 files into names that don't end in 12.1
  * This is for cx_Oracle
3. pip install -r requirements.txt

## Oracle

Log into database and create user in correct pluggable database

1. on db server: sqlplus /nolog
  * Rest of steps are in sql
2. connect / as sysdba
3. alter session set container = <pdb name>
4. <Create user and set permissions>
