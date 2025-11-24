# prepare_seed_jsonl.py
# Creates jarvic_seed.jsonl (25 user->assistant pairs). English only.

import json

examples = [
    {"id":"P0001","input":"Hi Jarvic.","response":"Hi — I’m Jarvic. How can I help you today?"},
    {"id":"P0002","input":"Set a reminder for tomorrow 9 AM to call mom.","response":"Reminder set for tomorrow at 09:00 to call your mom."},
    {"id":"P0003","input":"Translate 'Where is the nearest hospital' to Tamil.","response":"'அருகிலுள்ள மருத்துவமனை எங்கு?' — formal Tamil."},
    {"id":"P0004","input":"Give a one-line summary of climate change.","response":"Climate change is the long-term shift in temperatures and weather patterns, mainly due to human activities."},
    {"id":"P0005","input":"I need a 30-minute dinner recipe for two.","response":"Try lemon garlic pasta with sautéed vegetables — I’ll give step-by-step instructions."},
    {"id":"P0006","input":"What's 234 times 12?","response":"234 × 12 = 2808."},
    {"id":"P0007","input":"How do I reduce phone heating?","response":"Close background apps, lower screen brightness, and avoid heavy apps while charging."},
    {"id":"P0008","input":"Create a short, polite resignation template.","response":"Subject: Resignation — Dear [Manager], I am writing to formally resign effective [date]..."},
    {"id":"P0009","input":"Quick breathing exercise.","response":"Try box breathing: inhale 4s, hold 4s, exhale 4s, repeat 4 times."},
    {"id":"P0010","input":"Find a nearby cafe.","response":"Share your location or city and I’ll list nearby cafes."},
    {"id":"P0011","input":"Set a timer for 45 minutes.","response":"Timer started for 45 minutes."},
    {"id":"P0012","input":"Draft a short birthday message for a friend.","response":"'Happy Birthday! Hope your day is full of fun and good food — let’s celebrate soon!'"},
    {"id":"P0013","input":"How many kilometers in 10 miles?","response":"10 miles = 16.0934 kilometers."},
    {"id":"P0014","input":"Remind me every Sunday to call dad.","response":"Weekly reminder created for every Sunday to call your dad."},
    {"id":"P0015","input":"Summarize this paragraph: [paste text]","response":"Paste the paragraph and I’ll give a 2–3 sentence summary."},
    {"id":"P0016","input":"Recommend a beginner-friendly project to learn coding.","response":"Build a to-do list app — it covers UI, storage, and basic logic."},
    {"id":"P0017","input":"What’s the capital of Australia?","response":"Canberra."},
    {"id":"P0018","input":"Help me prepare for an interview for a software engineer role.","response":"I’ll run you through common questions, and we can do a short mock interview."},
    {"id":"P0019","input":"Create a 3-point meeting agenda about product launch.","response":"1) Launch timeline updates 2) Blockers & mitigation 3) Next steps & owners."},
    {"id":"P0020","input":"How to boil an egg perfectly?","response":"For hard-boiled: boil 9 minutes. For soft yolk: 6–7 minutes."},
    {"id":"P0021","input":"Give 3 icebreaker questions for a team meeting.","response":"1) One win this week? 2) Favorite weekend activity? 3) What’s one tool you can’t work without?"},
    {"id":"P0022","input":"I feel stressed — give a short grounding exercise.","response":"Name 5 things you can see, 4 things you can touch, 3 you can hear, 2 you can smell, 1 you can taste."},
    {"id":"P0023","input":"Convert 500 INR to USD (approx).","response":"Approximate conversion: 500 INR ≈ 6–7 USD (rates fluctuate)."},
    {"id":"P0024","input":"Set Do Not Disturb for 1 hour.","response":"Do Not Disturb enabled for 1 hour."},
    {"id":"P0025","input":"Tell a short clean joke.","response":"Why did the scarecrow win an award? Because he was outstanding in his field."}
]

out_file = "jarvic_seed.jsonl"
with open(out_file, "w", encoding="utf-8") as f:
    for e in examples:
        prompt = f"<|user|> {e['input']} <|assistant|> {e['response']}"
        obj = {"id": e["id"], "text": prompt}
        f.write(json.dumps(obj, ensure_ascii=False) + "\n")

print(f"Wrote {len(examples)} examples to {out_file}")
