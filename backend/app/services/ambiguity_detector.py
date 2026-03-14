from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

known_terms = [
"apple",
"line",
"issue"
]

def detect_ambiguity(text):

words = text.lower().split()

ambiguous=[]

for w in words:

if w in known_terms:

ambiguous.append(w)

return ambiguous
