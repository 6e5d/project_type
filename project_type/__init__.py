import os

def project_type(spath):
	assert spath.exists()
	if (spath / spath.name / "__init__.py").exists():
		return "python"
	if (spath / "Cargo.toml").exists():
		return "rust"
	if (spath / "lib.c3").exists() or (spath / "main.c3").exists():
		return "c3"
	if (spath / "src").exists():
		for file in (spath / "src").iterdir():
			if file.suffix == ".c":
				return "c"
			elif file.suffix == ".glsl":
				return "glsl"
	if (spath / "include").exists():
		for file in (spath / "include").iterdir():
			if file.suffix == ".h":
				return "h" # header only
	return "unknown"
