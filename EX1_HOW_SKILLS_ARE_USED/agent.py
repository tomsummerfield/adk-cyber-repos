import pathlib
import logging
import os

from google.adk.agents import Agent
from google.adk.skills import load_skill_from_dir
from google.adk.tools.skill_toolset import SkillToolset
from google.adk.models.lite_llm import LiteLlm

logger = logging.getLogger(__name__)

cloud_diagnosis_skill = load_skill_from_dir(
    pathlib.Path(__file__).parent / "skills" / "cloud-diagnosis"
)
cloud_skill_toolset = SkillToolset(skills=[cloud_diagnosis_skill])

root_agent = Agent(
    name="root_agent",
    model=LiteLlm(
        model="anthropic/claude-sonnet-5",
        api_key=os.environ.get("ANTHROPIC_API_KEY"),
        timeout=50,
        num_retries=3,
    ),
    description="Root agent for cloud diagnosis skill demonstration.",
    instruction="You are a cloud agent used for diagnosing and troubleshooting cloud-related issues",
    tools=[cloud_skill_toolset],
)
