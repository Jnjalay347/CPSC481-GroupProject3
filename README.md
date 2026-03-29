---
title: 481 Project 3
emoji: 🚀
colorFrom: red
colorTo: red
sdk: docker
app_port: 8501
tags:
- streamlit
pinned: false
short_description: '(CPSC 481) Group Project #3: Resume Management System'
license: mit
---

# CPSC 481: Group Project #3
Resume Management System

## Set-Up Instructions
- **Step #1**:\
Log into HuggingFace website.

- **Step #2**:\
Create your own Hugginface space @ https://huggingface.co/new-space, with the following configuration:\
• **Space SDK**: _Docker_\
• **Docker template**: _Streamlit_\
• Use default settings for the rest.

- **Step #3**:\
Copy files from this GitHub repo -> your HuggingFace space.

- **Step #4**:\
That's it. Space will auto-build and run your program.\
• _Note_: Every time you add or modify files on HuggingFace, it'll take some time to build, start, and run.

## Uploading Your Code Changes (via Pull Requests)
- Write your code (add/modify files) over at HuggingFace AND build/test them there to ensure it works and runs without any issues.
- Then, upload/commit that code here on GitHub and submit a Pull Request.
- Someone will verify & review your code to make sure it works.
- Pushing directly into the repo will not work.\
• Must pull request & someone else will approve/push your changes once they verify it works.\
• This prevents pushing untested code/discrepancies that might break the program for everyone.

## Update Files before Pull Requesting
- Before making your pull request here, make sure your files are up-to-date with the latest commit from this Repo.
- Verify that your updates still work as expected, with the latest commit.

## HuggingFace Repo Example
- https://huggingface.co/spaces/Jnjalay347/481-Project-3
- I'll try to keep mine up-to-date, as reasonably possible. That way, we have something that always works & to test with.

## Question: Why don't we just upload our code to the same HuggingFace repo to make it easier for everyone?
- **tl;dr**: It's not easier. HuggingFace is slow. It's slow to build, run, and test.
- **Answer**: Every time someone makes a commit or a change, Docker has to take (a lot of) time to re-build the program every single time, and HuggingFace has to allocate a certain number of resources to make it happen.\
• It's better to write and test your features on YOUR HuggingFace space and then upload it onto our GitHub repo.\
• This way, everyone doesn't have to sit around waiting for the same HuggingFace space to build, run, and test each time.
