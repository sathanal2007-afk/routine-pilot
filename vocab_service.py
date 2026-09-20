import requests
from database import SessionLocal
from models import Vocabulary

# 1. Dictionary Feature: எந்த வார்த்தைக்கும் உடனே Meaning & Example தேடும் வசதி
def lookup_dictionary(word: str):
    """Free Dictionary API வழியா வார்த்தையின் முழு விவரங்களை எடுக்கும்"""
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word.strip().lower()}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()[0]
            word_text = data.get("word", word)
            phonetic = data.get("phonetic", "N/A")
            
            # முதல் meaning மற்றும் example-ஐ எடுத்தல்
            meanings = data.get("meanings", [])
            definition = "No definition found"
            example = "No example available"
            part_of_speech = ""

            if meanings:
                part_of_speech = meanings[0].get("partOfSpeech", "")
                definitions = meanings[0].get("definitions", [])
                if definitions:
                    definition = definitions[0].get("definition", "")
                    example = definitions[0].get("example", "Practice using it in your own sentence!")

            return {
                "word": word_text.capitalize(),
                "part_of_speech": part_of_speech,
                "phonetic": phonetic,
                "definition": definition,
                "example": example
            }
        else:
            return {"error": f"'{word}' என்ற வார்த்தைக்கான விளக்கம் கிடைக்கவில்லை. ஸ்பெல்லிங்கை சரிபார்க்கவும்."}
    except Exception as e:
        return {"error": f"Dictionary error: {str(e)}"}


# 2. Daily Vocabulary: குறிப்பிட்ட நாளுக்கான 10 வார்த்தைகளை எடுக்கும் வசதி
def get_daily_vocab(day: int):
    """Database-ல் இருந்து அன்றைய நாளுக்கான 10 வார்த்தைகளை எடுக்கும்"""
    db = SessionLocal()
    words = db.query(Vocabulary).filter(Vocabulary.day_number == day).all()
    db.close()
    return words


# 3. Test செய்து பார்க்க
if __name__ == "__main__":
    print("--- 1. Testing Dictionary Lookup ---")
    result = lookup_dictionary("resilient")
    print(result)

    print("\n--- 2. Testing Day 1 Vocabulary ---")
    day_1_words = get_daily_vocab(day=1)
    for v in day_1_words:
        print(f"• {v.word} ({v.tamil_meaning}) - e.g., {v.example}")