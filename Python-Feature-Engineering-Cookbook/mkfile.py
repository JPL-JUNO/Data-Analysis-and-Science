from pathlib import Path

with open("toc.txt", "r") as f:
    for sec in f.readlines():
        file_name = sec.strip().lower().replace(" ", "_")
        ext = ".ipynb"
        Path.touch(
            Path(
                "./NOTEBOOKS/CH02_Encoding_Categorical_Variables"
                / Path(file_name + ext)
            )
        )
