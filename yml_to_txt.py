import yaml
import re

def yaml_to_requirements(yaml_path, output_path="requirements_converted.txt"):
    with open(yaml_path, "r") as f:
        env = yaml.safe_load(f)

    requirements = []

    for dep in env.get("dependencies", []):
        if isinstance(dep, str):
            parts = dep.split("=")
            if len(parts) >= 2:
                name = parts[0]
                version = parts[1]
                if re.match(r"^\d+(\.\d+)*$", version):  # version is numeric
                    requirements.append(f"{name}=={version}")
                else:
                    requirements.append(name)  # fallback
            else:
                requirements.append(dep)
        elif isinstance(dep, dict) and "pip" in dep:
            # Handle nested pip dependencies
            requirements.extend(dep["pip"])

    # Write to requirements.txt
    with open(output_path, "w") as f:
        f.write("\n".join(requirements))

    print(f"Converted {yaml_path} → {output_path}")
    print("Extracted dependencies:")
    for r in requirements:
        print("  -", r)


if __name__ == "__main__":
    yaml_to_requirements("hf-env.yml")
