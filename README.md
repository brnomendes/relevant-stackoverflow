# Relevant StackOverflow

## Project Requirements
 - Extract from stackoverflow.com the 10 newest Android-related questions, as well as the 10 most voted Android-related questions that are created in the past week.
 - Build a simple website that displays the titles of the extracted questions.
 - Provide a convenient way of displaying the full question thread after I click on one of the titles.

## Demo

![App Demo](https://github.com/brnomendes/relevant-stackoverflow/blob/master/demo.gif)

## Features
## How to run in Development Mode
### Project Dependencies

Front-end dependencies:
```
axios==0.19.2
bulma==0.8.0
fontawesome==5.12.0
moment==2.24.0
vue==2.6.11
```

Back-end dependencies:
```
Flask==1.1.1
requests==2.22.0
gunicorn==20.0.4 #deploy only
```

### Configure Stack Exchange API (Optional)

To increase the limit of queries that an application can make to the Stack Exchange API, it's necessary to configure an API key:
1. Obtain a Stack Exchange API key (see [documentation](https://api.stackexchange.com/docs)).
2. Store the value in an environment variable `STACK_API`.

### Run Application

To run the application, you need to clone the repository, install the dependencies and run the main file:

```bash
$ git clone https://github.com/brnomendes/relevant-stackoverflow.git
$ cd relevant-stackoverflow

# Optional: Create and activate an isolated python environment for the application.
$ virtualenv -p python3 venv
$ source venv/bin/activate

$ python -m pip install -r requirements.txt
$ python main.py
```

## Future Work:
 - Support the viewing of questions related to other tags (The back-end already allows querying with tags, only the view should be improved for this feature).
 - Support viewing the question and answer comments (The backend already supports querying comments, only the view should be improved for this feature).
 - Save the received data to a file or database.
 - Use Vue [Single File Components
](https://it.vuejs.org/v2/guide/single-file-components.html) to organize reusable components.
 - Add support for Sass in the build, to be able to modify some bulma variables (such as the modal width).
 - Add unit tests for the back-end and front-end.
