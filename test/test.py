import ext_llm as xllm

#read config yaml file
config : str = open("ext_llm_config.yaml").read()

#initialize extllm library
extllm = xllm.init(config)

print(extllm.list_available_models())
print(extllm.get_model("aws"))