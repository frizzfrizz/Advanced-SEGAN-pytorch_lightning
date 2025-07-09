from pydub import AudioSegment

audio1 = AudioSegment.from_file("data/clean_trainset_wav/p226_001.wav", format = "wav")
audio2 = AudioSegment.from_file("data/clean_trainset_wav/p226_002.wav", format = "wav")
overlayed_audio = audio2.overlay(audio1)

overlayed_audio.export("output.wav", format = "wav")