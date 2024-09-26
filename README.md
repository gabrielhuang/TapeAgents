<div align="center">

# TapeAgents

![Supported Python Versions](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue)

</div>

*TapeAgents* is an experimental framework to build, debug, serve and optimize AI agents. The key concept of the framework is *Tape*: a complete semantic-level log of the agent's session. All Agent-Environment interactions are mediated by the orchestrator and must go through the tape

![image](/assets/overview.png)

Key features:
- Build your agent as a low-level state machine, as a high-level multi-agent team configuration, or as a mono-agent guided by multiple prompts
- Debug your agent with TapeAgent studio or TapeBrowser apps
- Serve your agent with response streaming
- Optimize your agent's configuration using successful tapes; finetune the LLM using revised tapes.

The Tape-centric design of TapeAgents will help you at all stages of your project:
- Build with ultimate flexibility of having access to tape for making prompts and generating next steps
- Change your prompts or team structure and resume  the debug session as long as the new agent can continue from the older tape
- Fully control the Agent's tape and the Agent's acting when you use a TapeAgent in an app
- Optimize tapes and agents using the carefully crafted metadata structure that links together tapes, steps, llm calls and agent configurations

# Get Started

We highly recommend starting with the [introductory Jupyter notebook](/intro.ipynb). The notebook will introduce you to all the core concepts of framework. 

# Installation

1. Clone the repository:
```
git clone https://github.com/ServiceNow/TapeAgents.git
cd TapeAgents
```

2. Create conda environment and install the package in editable mode:
```
make setup
```

# Examples

The [examples/](examples/) directory contains examples of how to use the TapeAgents framework for building, debugging and improving agents. Each example is a self-contained Python script that demonstrates how to use the framework to build an agent for a specific task.

- [intro.ipynb](intro.ipynb) - Quickstart, step by step tutorial that shows you how to build a few agents of increasing complexity and demonstrates the core concepts of the TapeAgents framework.
- How to build [teams of TapeAgents](examples/data_science.py) with [AutoGen](https://github.com/microsoft/autogen)-style low-code programming paradigm
- How to [finetune a TapeAgent](examples/gsm8k_tuning) with a small LLM to be better at math problem solving on GSM-8k dataset.
- An agent that [does planning, searches the web and uses code interpreter](examples/gaia_agent) to answer precise questions, solving the tasks from the [GAIA benchmark](https://huggingface.co/spaces/gaia-benchmark/leaderboard).

Other notable examples that demonstrate the main aspects of the framework:
- [workarena](examples/workarena) - custom agent that solves WorkArena benchmark using BrowserGym environment.
- [annotator.py](annotator.py) - example of the agent that annotates the existing tape with some score or label.
- [tape_improver.py](examples/tape_improver.py) - the agent that revisit and improves the tapes produced by another agent.
- [studio.py](examples/studio.py) - interactive Gradio demo of agent that could be edited in runtime.



# Learn more 

See our [Now AI paper](https://servicenow.sharepoint.com/sites/snrcat/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2Fsnrcat%2FShared%20Documents%2FTapeAgents%2FTapeAgents%5F2024nowai%2Epdf&parent=%2Fsites%2Fsnrcat%2FShared%20Documents%2FTapeAgents&p=true&ga=1) on TapeAgents.

# Contact

Please use the group email of the Conversational AssistanT (CAT) Program at ServiceNow

snr-cat@servicenow.com

# Acknowledgements

We acknowledge the inspiration we took from prior frameworks, in particular [LangGraph](https://github.com/langchain-ai/langgraph), [AutoGen](https://github.com/microsoft/autogen), [Agents](https://github.com/aiwaves-cn/agents) and [DSPy](https://github.com/stanfordnlp/dspy).


