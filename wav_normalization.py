import os 
import numpy as np 
import pdb
import librosa 
import soundfile as sf

wav_dirs = os.listdir("wav")
mos_dirs = os.listdir("wav/mos")

ballad_dirs = os.listdir("wav/mos/ballad")
child_dirs = os.listdir("wav/mos/child")
abtest_dirs = os.listdir("wav/abtest")

for ballad in ballad_dirs:
    wav_file_name = "wav/mos/ballad/"+ballad
    wav, sr = librosa.load(wav_file_name, 24000)
    wav = librosa.util.normalize(wav) * 0.3
    sf.write(wav_file_name, wav, 24000)

for child in child_dirs:
    wav_file_name = "wav/mos/child/"+child
    wav, sr = librosa.load(wav_file_name, 24000)
    wav = librosa.util.normalize(wav) * 0.3
    sf.write(wav_file_name, wav, 24000)

for abtest in abtest_dirs:
    wav_file_name = "wav/abtest/"+abtest
    wav, sr = librosa.load(wav_file_name, 24000)
    wav = librosa.util.normalize(wav) * 0.3
    sf.write(wav_file_name, wav, 24000)
