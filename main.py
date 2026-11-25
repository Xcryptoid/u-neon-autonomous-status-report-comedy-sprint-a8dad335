import os
import shutil

out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
os.makedirs(out_dir, exist_ok=True)
shutil.copyfile("entry.txt", os.path.join(out_dir, "entry.txt"))

# How this entrypoint works (plain words):
# - It reads the MAKEFUN_OUTPUT_DIR environment variable to learn where
#   the grader wants the finished entry to go.
# - It creates that directory if it is missing, so the run does not fail
#   on a fresh output folder.
# - It copies the pre-written entry.txt into that directory, byte for byte.
# - It uses only the Python standard library (os and shutil), so it runs
#   anywhere plain python3 runs, with no extra packages or network.
