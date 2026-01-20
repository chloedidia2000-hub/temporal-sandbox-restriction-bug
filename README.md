To reproduce:
1. Create a virtual environment and activate it
```
python -m venv venv
source venv/bin/activate
```
1. Start a Temporal dev server
```
temporal server start-dev
```
2. Install `failed-sandbox-requirements.txt`.  This will demonstrate that `requests` can be used in workflow code to successfully send HTTP requests when `urllib==1.26.19` is installed.
```
pip install -r failed-sandbox-requirements.txt
```
3. Start the worker
```
python run_worker.py
```
4. Run a workflow
```
python run_workflow.py
```
5. Observe that the workflow completes successfully and the logs contain the HTML body of the response.
6. Stop the worker
7. Install `successful-sandbox-requirements.txt`.  This will demonstrate that the sandbox can block HTTP requests on newer versions of `urllib3`.
```
pip install -r successful-sandbox-requirements.txt
```
8. Start the worker
```
python run_worker.py
```
9. Run a workflow
```
python run_workflow.py
```
10. Observe that the workflow errors with the expected sandbox restriction
```
temporalio.worker.workflow_sandbox._restrictions.RestrictedWorkflowAccessError: Cannot access http.client.IncompleteRead.__mro_entries__ from inside a workflow. If this is code from a module not used in a workflow or known to only be used deterministically from a workflow, mark the import as pass through.
```
