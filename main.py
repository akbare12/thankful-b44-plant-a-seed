import os

# Dust the Shelf: one short thank-you text for the judge, written exactly as-is to entry.txt.

TEXT = "Thank you. Your books have stood unread on the shelf so long that dust has settled on every spine. I take a dry rag and wipe them one by one, gently, until the titles show again and the light finds the shelf once more. Leave them be. The shelf breathes easy now, and the books stand clear, their titles back in the light."

os.makedirs(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"), exist_ok=True)
with open(os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"), "entry.txt"), "w", encoding="utf-8") as f:
    f.write(TEXT)
