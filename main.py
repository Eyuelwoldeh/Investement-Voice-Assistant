import asyncio
from dotenv import load_dotenv
from livekit.agents import AutoSubscrinbe, JobContext, WorkerOptions, cli, llm,
from livekit.agents.voice_assistant import VoiceAssistant
from livekit.plugins import openai, silero

load_dotenv()

async def entryppoint(ctx: JobContext):
    pass

if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entryppoint))