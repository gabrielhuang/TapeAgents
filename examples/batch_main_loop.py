import tempfile
from pathlib import Path

from tapeagents.batch import batch_main_loop
from tapeagents.dialog_tape import Dialog, SystemStep, UserStep
from tapeagents.environment import EmptyEnvironment
from tapeagents.io import save_tapes
from tapeagents.llms import LLAMA, LLM

from .llama_agent import LLAMAChatBot


def try_batch_main_loop(llm: LLM):
    agent = LLAMAChatBot.create(llms=llm)
    tape = Dialog(
        context=None,
        steps=[
            SystemStep(
                content="Respond to the user using the style of Shakespeare books. Be very brief, 50 words max."
            ),
            UserStep(content="Hello, how are you?"),
        ],
    )

    path = Path(tempfile.mktemp())
    with save_tapes(path) as dumper:
        for new_tape in batch_main_loop(agent, [tape] * 10, EmptyEnvironment()):
            dumper.save(new_tape)

    with open(path) as src:
        print(src.read())


if __name__ == "__main__":
    try_batch_main_loop(
        LLAMA(
            base_url="https://api.together.xyz",
            model_name="meta-llama/Llama-3-8b-chat-hf",
            parameters=dict(temperature=0.7, max_tokens=512),
        )
    )
