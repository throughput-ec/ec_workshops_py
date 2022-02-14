---
type: slides
---

<div><h1><img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module1/00_ec_slide1.png?raw=true" alt="EC Theme" width=25% align="left"/> Lesson 7<br>Introduction to CI/CD and Github Actions</h1></div>

---

## Continuous Integration (CI)

- CI is the practice of frequently integrating code changes from contributors to a shared repository. 
- Often the submission of code to a shared repository is combined with automated testing to increase code dependability and quality.

**Why use CI + automated testing**

- detects errors sooner
- reduces the amount of code to be examined when debugging
- facilitates merging
- ensures new code additions do not introduce errors

--- 

## Continous Development (CD)

- Defined as the practice of automating the deployment of software that has successfully run through your test-suite.

- For example, upon merging a pull request to master, an automation process builds the Python package and publishes to PyPI without further human intervention.

**Why use CD?**

- little to no effort in deploying new version of the software allows new features to be rolled out quickly and frequently

- allows for quick implementation and release of bug fixes

- deployment can be done by many contributors

---

## GitHub Actions 

- It is a continuous integration and continuous development (CI/CD) platform that allows you to automate your build, test, and deployment pipeline.

- A tool for automating software development tasks, located in the same place where you already store your code.

- You can create workflows that build and test every pull request to your repository, or deploy merged pull requests to production.

- GitHub Actions lets you run workflows when other events happen in your repository. For example, you can run a workflow to automatically add the appropriate labels whenever someone creates a new issue in your repository.

- GitHub provides Linux, Windows, and macOS virtual machines to run your workflows, or you can host your own self-hosted runners in your own data center or cloud infrastructure.

---

## Key concepts:

- Actions: Individual tasks you want to perform.

- Workflow: A collection of actions (specified together in one file).

- Event: Something that triggers the running of a workflow.

- Runner: A machine that can run the Github Action(s).

- Job: A set of steps executed on the same runner.

- Step: A set of commands or actions which a job executes.

---

## Create an example workflow

1. Create a new public GitHub.com repository.

2. Click on the “Actions” tab

3. Click on the first “Simple workflow” configure button

<a href="https://github.com/throughput-ec/ec-workshops/blob/main/static/module7/00_github_actions.png?raw=true" target="_blank">
<img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module7/00_github_actions.png?raw=true" alt="GH Actions" width=45% align="center" title="Click to zoom in"> 
</a>

---

4. Click on the two green commit buttons to add this workflow file

<a href="https://github.com/throughput-ec/ec-workshops/blob/main/static/module7/01_github_actions.png?raw=true" target="_blank">
<img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module7/01_github_actions.png?raw=true" alt="Commits" width=45% align="center" title="Click to zoom in"> 

---

5. Go back to the “Actions” tab. It now looks different:

<a href="https://github.com/throughput-ec/ec-workshops/blob/main/static/module7/02_github_actions.png?raw=true" target="_blank">
<img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module7/02_github_actions.png?raw=true" alt="Actions" width=45% align="center" title="Click to zoom in"> 


---

6. Click on the message associated with the event that created the action:

<a href="https://github.com/throughput-ec/ec-workshops/blob/main/static/module7/03_github_actions.png?raw=true" target="_blank">
<img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module7/03_github_actions.png?raw=true" alt="Message" width=45% align="center" title="Click to zoom in"> 

---

7. Click on the build link:

<a href="https://github.com/throughput-ec/ec-workshops/blob/main/static/module7/04_github_actions.png?raw=true" target="_blank">
<img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module7/04_github_actions.png?raw=true" alt="Actions" width=45% align="center" title="Click to zoom in"> 

---

8. Click on the arrow inside the build logs to expand a section and see the output of the action Check all of the arrows and see what happens at each step.

<a href="https://github.com/throughput-ec/ec-workshops/blob/main/static/module7/05_github_actions.png?raw=true" target="_blank">
<img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module7/05_github_actions.png?raw=true" alt="Actions" width=45% align="center" title="Click to zoom in"> 

---

## GitHub Actions workflow file

A YAML file that lives in the .github/workflows directory or your repository which speciies your workflow.

A basic example of this yaml file:

```
name: learn-github-actions
on: [push]
jobs:
  check-bats-version:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-node@v2
        with:
          node-version: '14'
      - run: npm install -g bats
      - run: bats -v
```

---

## Understanding the file

|                            |                          |
| ----------------- | -----------------------------|
| name: learn-github-actions |  Optional - The name of the workflow as it will appear in the Actions tab of the GitHub repository.  |
| on: [push]        | Specifies the trigger for this workflow. This example uses the push event, so a workflow run is triggered every time someone pushes a change to the repository  |
| jobs:  | Groups together all the jobs that run in the learn-github-actions workflow. |
| check-bats-version: | Defines a job named check-bats-version. The child keys will define properties of the job. |
|  runs-on: ubuntu-latest | Configures the job to run on the latest version of an Ubuntu Linux runner. This means that the job will execute on a fresh virtual machine hosted by GitHub. |
| steps:  | Groups all the steps that run in the check-bats-version job. |
|  uses: actions/checkout@v2  | The uses keyword specifies that this step will run v2 of the actions/checkout action. |
| uses: actions/setup-node@v2 with: node-version: '14' | This step uses the actions/setup-node@v2 action to install the specified version of the Node.js (this example uses v14). This puts both the node and npm commands in your PATH. |
| run: npm install -g bats | The run keyword tells the job to execute a command on the runner. |
| run: bats -v | Run the bats command with a parameter that outputs the software version.  |


---
# Let's practice what we learned!
