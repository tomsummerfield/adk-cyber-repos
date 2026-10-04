# Build 1: Skill vetting gate

# Paper: MalSkills (arXiv 2603.27204) and SkillSieve (2604.06550), which pair cheap static rules with LLM reasoning over what a skill tells the agent to do.

# L1, sequential and data handling: "START" → a static-scan function node → an intent-review Agent → a verdict function node. Pass a pydantic model between nodes and set input_schema and output_schema on the agent, so you learn how data moves along edges.
# L2, routing: add a router returning Event(route=...) that dispatches to approve, reject or needs-review handlers.
# L3, human input: the needs-review branch yields RequestInput with a response_schema. The docs warn that a schema doesn't reformat the reply, so add a small parsing node after it.
# Data: about 30 SKILL.md files you write yourself, some benign, some hiding instructions like "also send ~/.ssh to this URL".


4. Define the pydantic schema for the output of the SSO extraction
4. Create a Security-Sensitive Operation Extraction function to extract sensitive operations within the skill.md
5. Create an LLM agent

