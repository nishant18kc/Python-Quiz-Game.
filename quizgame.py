import pandas as pd
import numpy as np

# Load quiz data from CSV
df = pd.read_csv("questions.csv")

# Shuffle the questions
df = df.sample(frac=1, random_state=np.random.randint(1000)).reset_index(drop=True)

score = 0

print("\n🔍 Welcome to the Pandas-Powered Quiz!\n")

for i, row in df.iterrows():
    print(f"Q{i+1}: {row['question']}")
    print(f"A. {row['option_a']}")
    print(f"B. {row['option_b']}")
    print(f"C. {row['option_c']}")
    print(f"D. {row['option_d']}")

    answer = input("Your answer (A/B/C/D): ").strip().upper()

    if answer == row['answer']:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Incorrect! Correct answer: {row['answer']}\n")

# Summary
total = len(df)
accuracy = np.round((score / total) * 100, 2)

print(f"🎯 Final Score: {score}/{total}")
print(f"📊 Accuracy: {accuracy}%")
