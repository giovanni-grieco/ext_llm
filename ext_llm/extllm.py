from ext_llm import ExtLlmContext
import ext_llm.llm as llms

class ExtLlm:

    def __init__(self, context: ExtLlmContext):
        self.context = context

    def list_available_models(self):
        return self.context.get_configs()["models"]

    def get_model(self, model_name: str, module_name="ext_llm.llm") -> llms.Llm:
        class_name = self.context.get_configs()["models"][model_name]["class_name"]
        try:
            module = __import__(self.context.get_configs()["models"][model_name]["module_name"], fromlist=[class_name])
        except KeyError:
            module = __import__(module_name, fromlist=[class_name])
        if hasattr(module, class_name):
            return getattr(module, class_name)()
        else:
            raise Exception("Class not found")
