from huggingface_hub import InferenceApi

api = InferenceApi(repo_id="meta-llama/Llama-3.2-11B-Vision-Instruct", token="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")

prompt = "Write a haiku about space:"
response = api(inputs=prompt)
print(response)

