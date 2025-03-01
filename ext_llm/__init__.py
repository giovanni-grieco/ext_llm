from .llm import Llm
from .context import ExtLlmContext
from .extllm import ExtLlm

# This function initializes the ExtLlm object
# It takes in a string containing the yaml configuration
# It returns an ExtLlm object
def init(configs: str) -> ExtLlm:
    ext_llm_context = ExtLlmContext(configs)
    return ExtLlm(ext_llm_context)