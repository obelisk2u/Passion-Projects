from PIL import Image
import requests
from transformers import AutoProcessor, MllamaForConditionalGeneration
import os
os.environ['HF_HUB_DISABLE_SYMLINKS_WARNING'] = '1'

checkpoint = "meta-llama/Llama-3.2-11B-Vision"
model = MllamaForConditionalGeneration.from_pretrained(checkpoint)
processor = AutoProcessor.from_pretrained(checkpoint)

prompt = "<|image|>If I had to write a haiku for this one"
url = "https://www.ilankelman.org/stopsigns/australia.jpg"
image = Image.open(requests.get(url, stream=True).raw)

inputs = processor(text=prompt, images=image, return_tensors="pt")

# Generate
output = model.generate(**inputs, max_new_tokens=15)

prompt_len = inputs.input_ids.shape[-1]
generated_ids = output[:, prompt_len:]
generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)
print(generated_text)