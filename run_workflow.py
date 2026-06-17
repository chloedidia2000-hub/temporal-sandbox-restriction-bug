import asyncio
from temporalio.client import Client

from app_files import SayHello

async def main():
    # Connect to the Temporal server
    client = await Client.connect("localhost:7233")

    # Execute the workflow and wait for the result
    result = await client.execute_workflow(
        SayHello.run,
        "World",  # Input argument for the workflow
        id="hello-workflow-id",
        task_queue="my-task-queue",
    )
    print(f"Workflow result: {result}")

if __name__ == "__main__":
    asyncio.run(main
