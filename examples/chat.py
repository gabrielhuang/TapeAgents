import sys

from tapeagents.collective import CollectiveAgent, CollectiveTape
from tapeagents.studio import Studio
from tapeagents.llms import LLAMA, LLM
from tapeagents.rendering import PrettyRenderer


def try_chat(llm: LLM, studio: bool):
    # equilavent of https://microsoft.github.io/autogen/docs/tutorial/introduction
    comedy_duo = CollectiveAgent.create_chat_initiator(
        name="Joe",
        llm=llm,
        system_prompt="Your name is Joe and you are a part of a duo of comedians.",
        collective_manager=CollectiveAgent.create(
            name="Cathy", llm=llm, system_prompt="Your name is Cathy and you are a part of a duo of comedians."
        ),
        max_turns=3,
        init_message="Hey Cathy, tell me a joke",
    )
    if studio:
        Studio(comedy_duo, CollectiveTape(context=None, steps=[]), PrettyRenderer()).launch()
    else:
        for event in comedy_duo.run(CollectiveTape(context=None, steps=[])):
            print(event.model_dump_json(indent=2))


if __name__ == "__main__":
    llm = LLAMA(
        base_url="https://api.together.xyz",
        model_name="meta-llama/Meta-Llama-3-70B-Instruct-Turbo",
        parameters=dict(temperature=0.7, max_tokens=512),
    )
    if len(sys.argv) == 2:
        if sys.argv[1] == "studio":
            try_chat(llm, studio=True)
        else:
            raise ValueError()
    elif len(sys.argv) == 1:
        try_chat(llm, studio=False)
    else:
        raise ValueError()
