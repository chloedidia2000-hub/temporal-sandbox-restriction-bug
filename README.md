To reproduce:
1. Create a virtual environment and activate it
```
python -m venv venv
source venv/bin/activate
```
2. Start a Temporal dev server
```
temporal server start-dev
```
3. Install `failed-sandbox-requirements.txt`.  This will demonstrate that `requests` can be used in workflow code to successfully send HTTP requests when `urllib==1.26.19` is installed.
```
pip install -r failed-sandbox-requirements.txt
```
4. Start the worker
```
python run_worker.py
```
5. Run a workflow
```
python run_workflow.py
```
6. Observe that the workflow completes successfully and the logs contain the HTML body of the response.
7. Stop the worker
8. Install `successful-sandbox-requirements.txt`.  This will demonstrate that the sandbox can block HTTP requests on newer versions of `urllib3`.
```
pip install -r successful-sandbox-requirements.txt
```
9. Start the worker
```
python run_worker.py
```
10. Run a workflow
```
python run_workflow.py
```
11. Observe that the workflow errors with the expected sandbox restriction
```
temporalio.worker.workflow_sandbox._restrictions.RestrictedWorkflowAccessError: Cannot access http.client.IncompleteRead.__mro_entries__ from inside a workflow. If this is code from a module not used in a workflow or known to only be used deterministically from a workflow, mark the import as pass through.
```
