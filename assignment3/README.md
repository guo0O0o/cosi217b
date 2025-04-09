# Assignment 3

Implementation of a simple note taker application. The app is capable of adding a note, listing all notes, searching for a key word among all notes, and seeing the content of a note. It also is capable of allowing comments, showing time and date of comments and notes, and allowing deletion of a note and all its comments.

To run the app, first build a Docker image using the following command:
```bash
docker build -t notebook-app .
```

Then run the following command to run the image and have the data persist
```bash
docker run -p 5000:5000 -v absolute/path/to/this/directory:/app/data notebook-app
```