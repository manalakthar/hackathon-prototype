import random

# Realistic mock scenarios for hackathon demo
# In production, replace analyze_child_photo() with a Gemini Vision API call

SCENARIOS = [
    {
        "risk_level": "MODERATE",
        "color": "orange",
        "deficiencies": ["Iron (Anaemia)", "Vitamin D"],
        "observations": [
            "Pale inner eyelids detected",
            "Slightly dull hair texture",
            "Mild pallor in skin tone"
        ],
        "diet_recommendations": [
            "Add ragi (finger millet) to daily meals — rich in iron & calcium",
            "Include green leafy vegetables like spinach, methi, moringa (drumstick leaves)",
            "Give jaggery with warm milk every morning",
            "Soak dal overnight and cook with a squeeze of lemon for better iron absorption",
            "Encourage outdoor play for natural Vitamin D from sunlight"
        ],
        "schemes": [
            "Poshan Abhiyaan — Free nutrition supplements at Anganwadi",
            "Mid-Day Meal Scheme — Nutritious school meals",
            "PM POSHAN — Fortified food distribution"
        ]
    },
    {
        "risk_level": "HIGH",
        "color": "red",
        "deficiencies": ["Protein", "Iron (Anaemia)", "Vitamin A"],
        "observations": [
            "Signs of stunted growth for reported age",
            "Dry, scaly skin patches visible",
            "Brittle nails and sparse hair",
            "Prominent cheekbones suggesting low weight"
        ],
        "diet_recommendations": [
            "Introduce eggs, lentils, and groundnuts daily for protein",
            "Cook with moringa powder — high in protein, iron, and Vitamin A",
            "Give orange or yellow fruits (papaya, mango) for Vitamin A",
            "Use fortified atta (wheat flour) for daily rotis",
            "Add a small amount of ghee or oil to improve nutrient absorption",
            "Consult the nearest Anganwadi worker for therapeutic food supplements"
        ],
        "schemes": [
            "Poshan Abhiyaan — Urgent referral to nutrition rehabilitation centre",
            "ICDS — Supplementary nutrition from Anganwadi centre",
            "Rashtriya Bal Swasthya Karyakram (RBSK) — Free child health screening"
        ],
        "urgent": True
    },
    {
        "risk_level": "LOW",
        "color": "green",
        "deficiencies": ["Vitamin C (mild)"],
        "observations": [
            "Healthy skin tone and complexion",
            "Good hair thickness and shine",
            "Eyes appear clear and bright",
            "Minor signs of possible Vitamin C gap"
        ],
        "diet_recommendations": [
            "Include amla (Indian gooseberry) — highest Vitamin C source",
            "Add tomatoes, guava, or lemon to daily meals",
            "Continue balanced diet with local seasonal fruits",
            "Ensure child eats dal and vegetables every day"
        ],
        "schemes": [
            "PM POSHAN — Free nutritious school meals",
            "Poshan Tracker — Track child growth at Anganwadi"
        ]
    }
]


def analyze_child_photo(age_months: int) -> dict:
    """
    Mock NutriLens analysis.
    Simulates an AI assessment of child malnutrition based on age context.
    
    In production: replace with Gemini Vision API call using the uploaded image bytes.
    The prompt would ask Gemini to assess visible signs of malnutrition
    (skin pallor, hair texture, nail condition, eye clarity, growth indicators).
    """

    # Weight scenarios based on age for a more realistic demo feel
    if age_months < 12:
        # Infants — higher chance of moderate/high
        weights = [0.2, 0.4, 0.4]
    elif age_months < 36:
        # Toddlers
        weights = [0.4, 0.4, 0.2]
    else:
        # Older children
        weights = [0.5, 0.35, 0.15]

    scenario = random.choices(SCENARIOS, weights=weights, k=1)[0]

    return {
        "risk_level": scenario["risk_level"],
        "color": scenario["color"],
        "deficiencies": scenario["deficiencies"],
        "observations": scenario["observations"],
        "diet_recommendations": scenario["diet_recommendations"],
        "schemes": scenario["schemes"],
        "urgent": scenario.get("urgent", False)
    }
