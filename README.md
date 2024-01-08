# Phase 4 Lecture 2: Many-to-Many Relationships in Flask-SQLAlchemy

## Objectives

By the end of today's lecture, you will be able to create a three-model ORM in Flask-SQLAlchemy that reflects a many-to-many relationship. You will also be able to establish the relationships associated with such a relationship

## Lesson Plan

0. Run `pipenv install` and `pipenv shell` to install the necessary dependencies.
1. Set up a many-to-many DB relationship to store restaurants and foods.
    - Why is modeling a relationship ahead of time important?
    - What is a **join table**? Why is it necessary?
2. Fill out the models to reflect the DB relationship. Run `flask db init` to create the database, and `flask db migrate` and `flask db upgrade` to update its schema.
    - What is a relationship here? Is it within the schema or the models?
    - What does `serialize_rules` do?
    - What is **recursion**?

## Looking Ahead

Tomorrow's lesson will introduce server-side routing in Flask, particularly GET and DELETE requests.