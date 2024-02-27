from llama_index.core.tools import FunctionTool
import os

#building of the note engine which save and add the notes using the pandas data
note_file = os.path.join("data", "notes.txt")

def save_note(note):
    if not os.path.exists(note_file):
        open(note_file, "w")
    with open(note_file, "a") as f:
        f.writelines([note + "\n"])
    return "note saved"

#tool who gives the access with saving notes to the llm model
note_engine = FunctionTool.from_defaults(
    fn=save_note,
    name="note_saver",
    description="this tool can save a text based note to a file for the user."
)