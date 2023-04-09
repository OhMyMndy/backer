import os

from spleeter.audio.ffmpeg import FFMPEGProcessAudioAdapter


from spleeter.audio.adapter import AudioAdapter

from spleeter.separator import Separator

def spleet(files):
    adapter = FFMPEGProcessAudioAdapter
    bitrate = '320k'
    codec = 'mp3'
    duration = 0
    offset = 1200 # default is 600
    output_path = os.path.dirname(file)
    filename_format = '{filename} - {instrument}.{codec}'
    params_filename = 'spleeter:5stems'
    mwf = False
    verbose = True

    audio_adapter: AudioAdapter = AudioAdapter.get(adapter)
    separator: Separator = Separator(params_filename, MWF=mwf)

    for filename in files:
        print(filename,
            output_path,
            audio_adapter,
            offset,
            duration,
            codec,
            bitrate,
            filename_format)
        separator.separate_to_file(
            filename,
            output_path,
            audio_adapter=audio_adapter,
            offset=offset,
            duration=duration,
            codec=codec,
            bitrate=bitrate,
            filename_format=filename_format,
            synchronous=False,
        )
    separator.join()


file = "/root/Music/deemix Music/Musician __ Guitar __ Guitar - E/001 - Yes - Owner of a Lonely Heart.mp3"

files = [file]
spleet(files)
