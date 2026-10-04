from google.adk.agents import Agent
from google.adk.workflow import Workflow
from google.adk.events import Event
from pydantic import BaseModel, Field

import logging

logger = logging.getLogger(__name__)


class SSO(BaseModel):
    artifact: str = Field(
        description="Artifact ingested by the agent, e.g a skill.md, config.yaml, or a script file."
    )
    operation: str = Field(
        description="Operation to be performed on the artifact, e.g. read, write, execute."
    )
    operand: str = Field(
        description="Operand for the operation, e.g. the data or the command thats being operated on."
    )
    value: str = Field(
        description="Value associated with the operand, such as the content of a file or the result of a command execution."
    )


def static_scan(node_input: str) -> SSO:
    logger.info(f"Processing node input: {node_input}")
    return Event(message="SSO Stage Complete")


llm_agent = Agent(
    name="Root agent for this demonstration",
    description="This agent is designed to demonstrate the ingestion of a malicious skill.md file and its potential impact on the agent's behavior.",
)

workflow = Workflow(
    name="malicious_skillmd_workflow",
    description="Workflow to demonstrate the ingestion of a malicious skill.md file and its potential impact on the agent's behavior.",
    edges=[
        "START",
        static_scan,
    ],
)
