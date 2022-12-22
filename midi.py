from mido import MidiFile
import pygame
import base64
import numpy as np

mid64='''\
TVRoZAAAAAYAAQAGAJBNVHJrAAAAJwD/WAQEAhgIAP9ZAgAAAP9RAwfCOwD/BgpGaXNoLVBvbGth
AP8vAE1UcmsAAANoAP8hAQAA/wMOQWNjb3JkaW9uIEhpZ2gAwRUAsQd/ALEKQAD/AQpGaXNoIFBv
bGthAJFOZGhOAAFQYyNQAAFSZBdSADFQZCNQACVOYxdOADFMZCNMACVLYxdLADFJYyNJACVOZCNO
AAFNYyNNAAFOYyNOAAFQZCNQAAFOZCNOAAFMZCNMAAFLZCNLAAFHYyNHAAFLYyNLAAFKYyNKAAFL
YyNLAAFMZCNMAAFLZCNLAAFJZCNJAAFHYyNHAAFCYyNCAAE/YyM/AAFCYyNCAAFHZCNHAAFLZCNL
AAFOYxFOADdQYyNQACVQYyNQACVJYyNJACVJZIEPSQABTGQjTAABS2QjSwABTGMjTAABTmQjTgAB
TGMjTAABS2QjSwABSWMjSQABSGMjSAABSWQjSQABQmMjQgABRmQjRgABSWQjSQABTGQjTAABSWMj
SQABRmQjRgABRGQjRAABQmMjQgABRmQjRgABSWQjSQABTGMjTAABUmMRUgA3UGQjUAAlUGMjUAAl
S2MjSwAlS2SBD0sAAU5jI04AAU1kI00AAU5jI04AAVBjI1AAAU5jI04AAUxkI0wAAUtjI0sAAUdk
I0cAAUtjI0sAAUpkI0oAAUtkI0sAAUxjI0wAAUtkI0sAAUlkI0kAAUdjI0cAAUJjI0IAAT9kIz8A
AUJjI0IAAUdkI0cAAUtkI0sAAU5kI04AAUdjI0cAAUtjI0sAAU5kI04AAVBjgXtQACVQZCNQAAFP
YyNPAAFQZCNQAAFSYyNSAAFVYyNVAAFTYyNTAAFSYyNSAAFQYyNQAAFOYyNOAAFNYyNNAAFOZCNO
AAFPZCNPAAFQZCNQAAFOYyNOAAFMZCNMAAFLYyNLAAFMZCNMAAFLYyNLAAFMZCNMAAFNZCNNAAFO
ZCNOAAFMZCNMAAFLZCNLAAFJYyNJAAFLZCNLACVMYyNMACVNZCNNACVOYyNOACVQZCNQAAFPZCNP
AAFQYyNQAAFSZCNSAAFVYyNVAAFTYyNTAAFSYyNSAAFQZCNQAAFOZCNOAAFNYyNNAAFOZCNOAAFP
YyNPAAFQZCNQAAFOYyNOAAFMZCNMAAFLZCNLAAFJZCNJAAFEZCNEAAFJZCNJAAFMYyNMAAFQZBFQ
ADdSYyNSACVTZCNTACVSYyNSACVTZCNTAAD/LwBNVHJrAAAFMAD/IQEAAP8DDUFjY29yZGlvbiBM
b3cAwhUAsgd/ALIKQACSQmRrQgABRGMjRAABRmMXRgAxRGMjRAAlQmQXQgAxQGQjQAAlP2MXPwAx
PWMjPQBtQmQAP2MAO2MROwAAPwAAQgATP2QAQmQAO2QROwAAQgAAPwBbO2QAP2MAQmMRQgAAPwAA
OwB/P2QAO2MAQmQRQgAAOwAAPwATP2MAO2MAQmMRQgAAOwAAPwBbO2MAP2MAQmMRQgAAPwAAOwB/
QmQAP2MAO2QROwAAPwAAQgATP2MAQmMAO2QROwAAQgAAPwBbP2MAO2QAQmMRQgAAOwAAPwATQmMA
P2MAO2QROwAAPwAAQgBbQGMAOmMAQmQRQgAAOgAAQAATOmQAQGQAQmQRQgAAQAAAOgATQmQAQGMA
OmQROgAAQAAAQgA3OmQAQGQAQmMRQgAAQAAAOgB/OmQAQGQAQmQRQgAAQAAAOgATQGMAOmQAQmQR
QgAAOgAAQABbOmMAQGMAQmQRQgAAQAAAOgB/QGQAOmMAQmMRQgAAOgAAQAATQGMAOmQAQmQRQgAA
OgAAQABbOmMAQGQAQmMRQgAAQAAAOgB/QGQAOmQAQmQRQgAAOgAAQAATQGQAOmMAQmQRQgAAOgAA
QABbOmMAQGQAQmMRQgAAQAAAOgATQGQAOmQAQmMRQgAAOgAAQABbP2QAO2QAQmMRQgAAOwAAPwAT
P2QAO2QAQmQRQgAAOwAAPwATP2QAO2QAQmMRQgAAOwAAPwA3P2QAO2MAQmMRQgAAOwAAPwB/QmMA
P2QAO2MROwAAPwAAQgATP2MAQmQAO2MROwAAQgAAPwBbO2QAP2QAQmMRQgAAPwAAOwB/P2MAO2QA
QmMRQgAAOwAAPwATP2MAO2MAQmMRQgAAOwAAPwBbO2MAP2MAQmQRQgAAPwAAOwB/QmQAP2MAO2MR
OwAAPwAAQgATP2QAQmQAO2MROwAAQgAAPwBbP2QAO2MAQmQRQgAAOwAAPwATQmMAP2MAO2MROwAA
PwAAQgBbO2QARGMAQGQRQAAARAAAOwATO2MARGQAQGQRQAAARAAAOwATO2QARGQAQGMRQAAARAAA
OwA3O2MARGQAQGMRQAAARAAAOwB/QGQARGMAO2QROwAARAAAQAATQGMARGMAO2QROwAARAAAQABb
O2MAQWMARGMRRAAAQQAAOwB/P2QAO2QAQmMRQgAAOwAAPwATP2QAO2MAQmQRQgAAOwAAPwBbO2QA
P2QARGQRRAAAPwAAOwB/PWMAQGMARGQRRAAAQAAAPQATPWMAQGQARGQRRAAAQAAAPQBbOmMAPWQA
QmQRQgAAPQAAOgATOmMAPWQAQmMRQgAAPQAAOgBbQmMAP2QAO2MROwAAPwAAQgATQmMAP2QAO2MR
OwAAPwAAQgATO2QAQmMAP2MRPwAAQgAAOwA3QmMAO2QAP2MRPwAAOwAAQgB/QGMARGQAO2QROwAA
RAAAQAATQGQARGQAO2MROwAARAAAQABbO2MAQWMARGQRRAAAQQAAOwB/P2QAO2QAQmQRQgAAOwAA
PwATP2MAO2QAQmQRQgAAOwAAPwBbO2QAP2QARGMRRAAAPwAAOwB/RGQAPWMAQGQRQAAAPQAARAAT
PWQAQGMARGQRRAAAQAAAPQBbQmMAOmMAPWQRPQAAOgAAQgATOmMAPWMAQmQRQgAAPQAAOgATP2QA
QmMAR2MRRwAAQgAAPwA3P2QAQmQAR2MRRwAAQgAAPwA3R2MAQmQAP2MRPwAAQgAARwAA/y8ATVRy
awAAAYQA/yEBAAD/AwlUdWJhIEJhc3MAwzoAswd4ALMKQACTKmNrKgABLGMjLAABLmMXLgAxLGMj
LAAlKmMXKgAxKGMjKAAlJ2QXJwAxJWQjJQAlI2RHIwBJHmNZHgA3I2NHIwBJHmRZHgA3I2NHIwAB
HmMjHgAlI2M1IwATJ2M1JwATKmNZKgA3JWNZJQA3HmRZHgA3JWNHJQBJHmRZHgA3JWRHJQBJHmQ1
HgATH2RHHwABIGMjIAAlImRHIgABI2QjIwAlImMjIgAlIGMjIAAlHmNHHgABI2MjIwBtHmNZHgA3
I2RHIwBJHmNZHgA3I2QjIwAlHmNHHgABI2QjIwAlJ2MjJwAlKGNHKABJI2RHIwBJHGNZHAA3HWNZ
HQA3HmRZHgA3IGRZIAA3JWRZJQA3HmRZHgA3I2MvIwAZImMvIgAZIGMvIAAZHmQvHgAZHGRZHAA3
HWRZHQA3HmRZHgA3IGNZIAA3JWNZJQA3HmRZHgA3I2QvIwAZHmQvHgAZI2MvIwAA/y8ATVRyawAA
AYYA/yEBAAD/AwtCYXNzIERvdWJsZQDEIgC0B24AtApAAJQqY2sqAAEsYyMsAAEuYxcuADEsZCMs
ACUqZBcqADEoYyMoACUnYxcnADElYyMlACUjZEcjAEkeZFkeADcjZEcjAEkeZFkeADcjZEcjAAEe
ZCMeACUjZDUjABMnZDUnABMqZFkqADclZFklADceY1keADclZEclAEkeY1keADclZEclAEkeYzUe
ABMfZEcfAAEgZCMgACUiZEciAAEjZCMjACUiYyMiACUgZCMgACUeY0ceAAEjZCMjAG0eY1keADcj
Y0cjAEkeZFkeADcjYyMjACUeY0ceAAEjZCMjACUnYyMnACUoZEcoAEkjZEcjAEkcY1kcADcdY1kd
ADceZFkeADcgY1kgADclY1klADceY1keADcjYy8jABkiZC8iABkgZC8gABkeYy8eABkcY1kcADcd
ZFkdADceZFkeADcgY1kgADclY1klADceZFkeADcjZC8jABkeYy8eABkjYy8jAAD/LwBNVHJrAAAD
PQD/IQEAAP8DBURydW1zALkHcQC5CkAAmTluACZ3ACRuASYAAyQAADkADCZYASYADyZVASYADyZU
ASYADyZSASYADiZPASYADiZNASYADSZ6BCYAICZ5ACRtBCQAACYAQyZ6BCYARSZ5ACRsBCQAACYA
QiZ+BCYAFyZ8BCYADSZ/BCYAGCZ6AiRnAiYAAiQAQiZ/BCYARiRvAjluAiQAAjkAQip3BCoAQyRl
BCQARSpoBCoAQyRmBCQARSpqBCoAQyRoBCQARSpsBCoAQyRoBCQARSprBCoAQyRkBCQARSpuBCoA
QyRjBCQARSpkBCoAQyRmBCQARSppBCoAQyRmBCQARSpxBCoARCRmBCQARCp6BCoARCRoBCQARCpy
BCoARCRlBCQARCp/BCoARSRpBCQAQyp6BCoARCRqBCQAQyp6BCoARSRqBCQARCp6BCoARCRpBCQA
RCp/BCoARSRrBCQAQyV6ACp1BCoAQyUAASRnBCQARCV7ACp7BCoAQyUAASRlBCQARCV7ACp9BCoA
QyUAASRoBCQARCV7ACp1BCoAQyUAASRrBCQARCV6ACp+BCoAQyUAASRpBCQAQyp3ASV7ACRoAyoA
ASQAQyUAASRnBCQARCV7ACp6BCoAICV6IyUAAiRpBCQAHiUAJSV6ACp5BCoAQyUAASRrBCQARCV6
ACp4BCoAQyUAASRwBCQARCV6ACp8BCoAQyUAASRrBCQAQyp6ASV6AyoARCUAASRmBCQARCV6ACp9
BCoAQyUAASRpBCQARCV7ACp3BCoAQyUAASRqBCQARCV7ACp0BCoAQyUAASRqBCQARCV6ACp6BCoA
ICV6IyUAASRlBCQAHyUAJCp6ASV7AyoARCUAADlhAiR/AjkAAiQAH7kHdBG5B3ETmSV6ACp4BCoA
QyUAASRuBCQARCV6ACpuBCoAQyUAACRwBCQARCp3ASV7AyoARCUAASRnBCQAQyp2ASV7AyoARCUA
ASRuBCQARCV7ACp6BCoAQyUAASRtBCQAQyp6ASV7AyoARCUAASV6ACRsBCQAQiZ/ASUAAyYAFyZ8
BCYADSZ/BCYAGCZ5Ajl6ACRoAiYAAiQAgQs5AAD/LwA=
'''

def play_music(music_file):
    """
    stream music with mixer.music module in blocking manner
    this will stream the sound from disk while playing
    """
    clock = pygame.time.Clock()
    try:
        pygame.mixer.music.load(music_file)
        print(f"Music file {music_file} loaded!")
    except pygame.error:
        print(f"File {music_file} not found! {pygame.get_error()}")
        return
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        # check if playback has finished
        clock.tick(30)

def play(music_file="take_five.mid"):
    freq = 44100  # audio CD quality
    bitsize = -16  # unsigned 16 bit
    channels = 2  # 1 is mono, 2 is stereo
    buffer = 1024  # number of samples
    pygame.mixer.init(freq, bitsize, channels, buffer)

    # optional volume 0 to 1.0
    pygame.mixer.music.set_volume(0.8)

    try:
        # use the midi file you just saved
        play_music(music_file)
    except KeyboardInterrupt:
        # if user hits Ctrl/C then exit
        # (works only in console mode)
        pygame.mixer.music.fadeout(1000)

        pygame.mixer.music.stop()
        raise SystemExit


def get_channels(music_file="take_five.mid"):
    tmp_file = "tmp.mid"
    mid = MidiFile(music_file, clip=True)
    music = mid.tracks[0]
    #music = track

    for msg in music:
        if msg.is_meta:
            music.remove(msg)
    j = 1
    ch_dict = {}
    ch_diff_grid = [[], []]
    while j < len(music):
        # Extracting message
        msg = music[j]

        # Checking is message has a channel
        if not hasattr(msg, 'channel'):
            j += 1
            continue

        if msg.channel not in ch_dict.keys():
            # If message's channel is not stored, store it. Init in the channel/time diff tracker lists
            ch_dict[msg.channel] = [msg]
            ch_diff_grid[0].append(msg.channel)
            ch_diff_grid[1].append(msg.time)
        else:
            # If message's channel is stored, add its time to all channel's diff tracker list
            ch_diff_grid[1] = [x + msg.time for x in ch_diff_grid[1]]

            # Get the index of the channel in the channel tracker list
            msg_ch_ind = np.where([x==msg.channel for x in ch_diff_grid[0]])[0][0]

            # Set the time of the message to the time in the channel's diff tracker list
            msg.time = ch_diff_grid[1][msg_ch_ind]

            # Append message to list of messages in the channel dict
            ch_dict[msg.channel].append(msg)

            # Reset the channel's diff tracker to 0
            ch_diff_grid[1][msg_ch_ind] = 0
        j += 1
    for ch, music in ch_dict.items():
        ch_dict[ch] = remove_delay(music)

    return ch_dict

def remove_delay(music):
    i = 0
    while i < len(music):
        msg = music[i]
        if msg.type == "note_on":
            msg.time = 0
            music[i] = msg
            return music
        i += 1
    return music

def get_line_plot(music):
    i = 0
    x = [0]
    xi = [0]
    y = [0]
    curr_note = None
    while i < len(music):
        msg = music[i]
        if msg.type == "note_on":
            if curr_note is None:
                x.append(msg.note)
                xi.append(msg.velocity)
                y.append(y[-1] + msg.time)
            else:
                x.append(x[-1])
                xi.append(xi[-1])
                y.append(y[-1] + msg.time - 1)
                x.append(msg.note)
                xi.append(msg.velocity)
                y.append(y[-1] + 1)
            curr_note = msg.note

        if msg.type == "note_off":
            if curr_note == msg.note:
                x.append(msg.note)
                xi.append(msg.velocity)
                y.append(y[-1] + msg.time)
            else:
                if i < len(music)-1:
                    next_msg = music[i+1]
                    next_msg.time = next_msg.time + msg.time
                    music[i+1] = next_msg
            curr_note = None

            #note_ind = np.where([v==msg.note for v in x])[0][-1]
           # y[note_ind] = y[note_ind] + msg.time
        i += 1
    x = np.array(x[1:])
    xi = np.array(xi[1:])
    y = np.array(y[1:])
    return x, xi, y


def play_channels(music_file="take_five.mid", ch=0):
    ch_dict = get_channels(music_file)
    tmp_file = "tmp.mid"
    mid = MidiFile(tmp_file, clip=True)
    music = ch_dict[ch]
    mid.tracks[0] = music
    mid.save(tmp_file)
    print(f"Playing channel {ch}")
    play(tmp_file)
    print("Done playing")




if __name__=="__main__":
    play_channels()
    play()

