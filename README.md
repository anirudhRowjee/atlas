# Atlas - Lightweight Ranked-choice election system

## What

Atlas is an open-source tool to conduct authenticated ranked-choice elections. The administrator can choose candidates, who authenticated voters can rank in order of their choice. When the administrator chooses to tabulate the votes, a [ranked-choice instant runoff](https://en.wikipedia.org/wiki/Instant-runoff_voting) ([this](https://www.youtube.com/watch?v=3Y3jE3B8HsE) video explains it _really_ well) election is conducted, and the winner is declared.

The uses of this framework are limited only by your voter base and imagination. As of now, the planned use-case is to deploy atlas as a decision framework for upcoming livestream/event topics. 

**It has been decided that Atlas will be implemented as a Slack bot. The rest of the details, apart from the core purpose, is still WIP**

## How

_Deliberate on the Tech Stack here._



## Getting started

1. Fork this Repository to your Github Account

2. Clone this repository to your computer/workspace.

3. Switch to a new branch.

```bash
$ git checkout -b <my-new-branch>
```
for example,
```bash
$ git checkout -b documentation-changes
```

4. Setup your virtual environment
```bash
# `pip install virtualenv` or  `pip3 install virtualenv` (if you don't already have it installed)
$ virtualenv env
$ source env/bin/activate
# on windows 
# .\env\Scripts\activate
```
Your terminal prompt should look something like this-
```
(env) $ 
```

5. Install all dependencies
```
(env) $ pip install -r requirements.txt
```

6. Run the Application
```
(env) $ <TODO>
```

If you want to run the tests - 
```
(env) $ python tests.py
```
