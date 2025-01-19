from fastapi import FastAPI
import random
import string

app = FastAPI()

@app.get("/generate-letter")
def generate_random_letter():
    random_letter = random.choice(string.ascii_letters)  # Randomly select a letter from the alphabet
    return {"letter": random_letter}
