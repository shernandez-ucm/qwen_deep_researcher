
import asyncio
from ollama_deep_researcher.graph import graph
from ollama_deep_researcher.state import SummaryStateInput

async def main():
    """
    Main function to run the research agent.
    """
    topic = input("Enter the research topic: ")
    inputs = SummaryStateInput(research_topic=topic)
    
    async for output in graph.astream(inputs):
        for key, value in output.items():
            print(f"Output from node '{key}':")
            print("---")
            print(value)
        print("\n---\n")

if __name__ == "__main__":
    asyncio.run(main())

