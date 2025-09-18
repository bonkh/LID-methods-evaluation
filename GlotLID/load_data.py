from datasets import load_dataset, get_dataset_config_names
from huggingface_hub import login
import json

login(token="hf_token")


dataset_name = "cis-lmu/glotlid-corpus"

configs = get_dataset_config_names(dataset_name)
print(f"Found {len(configs)} configs")


for config in configs:
    print(f"Processing {config} ...")
    ds = load_dataset(dataset_name, config, split="train")

    data = ds.to_list()

    out_file = f"{config}.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ Saved {out_file}")
