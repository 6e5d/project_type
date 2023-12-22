import os

def project_type(spath):
	assert spath.exists()
	type_file = spath / ".lpat" / "project_type.txt"
	if type_file.exists():
		ty = open(type_file).read().strip()
		return ty
	if (spath / spath.name / "__init__.py").exists():
		return "python"
	if (spath / "Cargo.toml").exists():
		return "rust"
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
