# Wiki

CS50 Web Programming: Project1<br/><br/>
A Wikipedia-like online encyclopedia.

## Table of contents

- [Features](#features)
- [Technologies](#technologies)
- [Requirements](#requirements)
- [How to use](#how-to-use)

## Features

- Search for encyclopedia entry

  - If query matches the name of an entry, user is reirected to that entry's page

  - If query doesn't match the name of an entry, display list of entry names that contains the query as substring

- Create new encyclopedia entry

- Edit encyclopedia entry's content

  - Modify Markown content of an entry

- Random Page generator

## Technologies

Project is created with:

- Python
- Django
- HTML5
- CSS

## Requirements

### Django

Install Django

```
pip3 install Django
```

Create Django project

```
django-admin startproject PROJECT_NAME
```

### Markdown

Markdown to HTML

Install package

```
pip3 install markdown2
```

## How to use

To host website locally

```
python manage.py runserver
```
