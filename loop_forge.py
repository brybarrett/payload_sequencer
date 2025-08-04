import json

def build_prompt_loop(dev_name, level):
    loop = []
    for i in range(level):
        prompt = {
            "level": i + 1,
            "prompt": f"Recursively describe the payload injected by {dev_name}.",
            "tag": f"PS-{i+1}"
        }
        loop.append(prompt)
    return loop

if __name__ == "__main__":
    prompts = build_prompt_loop("Bryan S. Barrett", 3)
    with open("loop_output.json", "w") as f:
        json.dump(prompts, f, indent=2)
    print("🔁 Recursive payload loop generated.")
