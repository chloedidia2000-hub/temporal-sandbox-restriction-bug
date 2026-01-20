from datetime import timedelta
from temporalio import activity, workflow

with workflow.unsafe.imports_passed_through():
    import requests

# Define the Activity
@activity.defn
async def say_hello(name: str) -> str:
    return f"Hello, {name}!"

# Define the Workflow
@workflow.defn
class SayHello:
    @workflow.run
    async def run(self, name: str) -> str:
        # Execute the activity
        workflow.logger.info("RUNNING THE ACTIVITY")
        
        res = requests.get("https://nginx.org/")
        res.raise_for_status()
        print(res.text)

        result = await workflow.execute_activity(
            say_hello,
            name,
            start_to_close_timeout=timedelta(seconds=10),
        )
        return result
