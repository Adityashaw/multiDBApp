## Multi DB App

#### A simple flask app to show how to connect to multiple databases within a single application

**Note:** The Mysql db is used by default for models unless other db is specified using `__bind_key__` attribute.


### Steps to install dependencies
```
pip3 install -e .
```

**N.B.** 1. You may install it inside `venv` or system-wide, that's your choice.


## Steps to run/use this app:

1. First export/set DATABASE_URL variable in your environment.
Example command is given in next step. Don't copy paste given secret key. Create your own.

1. `cd` into repo. Then, depending on your OS

    1. For Linux, use command 
        ```
        export DATABASE_URL_POSTGRESQL="postgresql://user:pass@localhost/dbname"
        export DATABASE_URL_MYSQL="mysql://user:pass@localhost:3306/dbname"
        export SECRET_KEY="3faf6054f65d7feb7c76f995fb940808"
        FLASK_APP=multidbapp FLASK_ENV=development flask run
        ```

    1. For Windows - CMD, use
        ```
        set DATABASE_URL_POSTGRESQL="postgresql://user:pass@localhost/dbname"
        set DATABASE_URL_MYSQL="mysql://user:pass@localhost:3306/dbname"
        set SECRET_KEY="3faf6054f65d7feb7c76f995fb940808"
        set FLASK_APP=multidbapp
        set FLASK_ENV=development
        flask run
        ```

    1. For Windows - PS, use
        ```
        $env:DATABASE_URL_POSTGRESQL="postgresql://user:pass@localhost/dbname"
        $env:DATABASE_URL_MYSQL="mysql://user:pass@localhost:3306/dbname"
        $env:SECRET_KEY="3faf6054f65d7feb7c76f995fb940808"
        $env:FLASK_APP=multidbapp
        $env:FLASK_ENV=development
        flask run
        ```

1. That's all!


### If you haven't create tables yet, you can do like this

1. In MySQL DB:
  ```
  CREATE TABLE faculty (
  id          smallint(6) NOT NULL AUTO_INCREMENT, 
  name        varchar(50) NOT NULL, 
  isAdmin     boolean, 
  CONSTRAINT fac_pkey_constraint 
    PRIMARY KEY (id)) ENGINE=InnoDB;
  ```

1. In PostgreSQL DB:
  ```
  CREATE TABLE student (
  id                  smallserial NOT NULL,
  name                varchar(50) NOT NULL,
  semester            smallint NOT NULL,
  roll_number         varchar(15) NOT NULL UNIQUE,
  CONSTRAINT stud_pkey_constraint
    PRIMARY KEY (id));
  ```

1. Then insert some data into the above tables.


### Linters used in this project :

1. Python Language Server (`pyls`) with `flake8`

1. Stylelint (for html)

## Steps to use linters:

1. Install them on your favourite text editor. `Vim`, `Sublime Text`, `Atom`, `VS Code` and many more are supported.

1. The linters should automatically pick up the configuration file(s) present in the root directory. If not, create an issue, let's find out **why?**


