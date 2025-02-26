from ext_llm import ExtLlmContext


class ExtLlm:

    def __init__(self, context: ExtLlmContext):
        self.context = context

    def list_available_models(self):
        return self.context.get_configs()["models"]

    def get_model(self, model_name: str):
        return self.context.get_configs()["models"][model_name]