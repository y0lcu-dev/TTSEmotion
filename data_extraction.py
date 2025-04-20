import os
import random

dataset_path = "TurEV-DB/Sound Source"
output_dir = "filelists"
os.makedirs(output_dir, exist_ok=True)

emotion_prompts = {
    "Happy": "mutlu ve enerjik bir ses tonu",
    "Angry": "öfkeli ve sert bir ses tonu",
    "Sad": "üzgün ve düşük enerjili bir ses tonu",
    "Calm": "sakin ve rahatlatıcı bir ses tonu"
}

data = []
for emotion, prompt in emotion_prompts.items():
    emotion_folder = os.path.join(dataset_path, emotion)
    for wav in os.listdir(emotion_folder):
        if wav.endswith(".wav"):
            wav_path = os.path.abspath(os.path.join(emotion_folder, wav))
            transcript = os.path.splitext(wav)[0]
            data.append(f"{wav_path}|{prompt}|{transcript}\n")

random.shuffle(data)
train_split = int(len(data) * 0.8)
val_split = int(len(data) * 0.9)

with open(f"{output_dir}/train.txt", "w", encoding='utf-8') as f:
    f.writelines(data[:train_split])

with open(f"{output_dir}/val.txt", "w", encoding='utf-8') as f:
    f.writelines(data[train_split:val_split])

with open(f"{output_dir}/test.txt", "w", encoding='utf-8') as f:
    f.writelines(data[val_split:])