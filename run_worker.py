import asyncio
from temporalio.client import Client
from temporalio.worker import Worker
from app_files import SayHello, say_hello

async def main():
    # Connect to the Temporal server
    client = await Client.connect("localhost:7233")

    # Run a worker for the "my-task-queue" task queue
    worker = Worker(
        client,
        task_queue="my-task-queue",
        workflows=[SayHello],
        activities=[say_hello],
    )
    print("Worker started. Waiting for workflow tasks...")
    await worker.run()

if __name__ == "__main__":
    asyncio.run(main())
