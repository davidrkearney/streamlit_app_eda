import streamlit as st
import pandas as pd

#import python pages
from modules.home_page import run_home
from modules.pandas_page import run_pandas
from modules.graphs_page import run_graphs

#Set app name and emoji displayed in browser tab
st.set_page_config(page_title="Fiscal Data", page_icon="bar_chart")

#title of my app and brief description
st.title("Fiscal Data")
st.subheader("Let's take a look at some Fiscal Data! :face_with_monocle:")

#set up the side bar for page options
page = st.sidebar.radio("Pick a Page:", ["Home", "Pandas Profile", "Basic Graphs", "Audio Page"])

import streamlit as st
import plotly.graph_objs as go
import numpy as np

st.title("Plotly examples")

st.header("Chart with two lines")

trace0 = go.Scatter(x=[1, 2, 3, 4], y=[10, 15, 13, 17])
trace1 = go.Scatter(x=[1, 2, 3, 4], y=[16, 5, 11, 9])
data = [trace0, trace1]
st.write(data)



# Copyright 2018-2021 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import io
import streamlit as st
import numpy as np
import wave
from scipy.io import wavfile

st.title("Audio test")

st.header("Local file")

# These are the formats supported in Streamlit right now.
AUDIO_EXTENSIONS = ["wav", "flac", "mp3", "aac", "ogg", "oga", "m4a", "opus", "wma"]

# For samples of sounds in different formats, see
# https://docs.espressif.com/projects/esp-adf/en/latest/design-guide/audio-samples.html


def get_audio_files_in_dir(directory):
    out = []
    for item in os.listdir(directory):
        try:
            name, ext = item.split(".")
        except:
            continue
        if name and ext:
            if ext in AUDIO_EXTENSIONS:
                out.append(item)
    return out


avdir = os.path.expanduser("~")
audiofiles = get_audio_files_in_dir(avdir)

if len(audiofiles) == 0:
    st.write(
        "Put some audio files in your home directory (%s) to activate this player."
        % avdir
    )

else:
    filename = st.selectbox(
        "Select an audio file from your home directory (%s) to play" % avdir,
        audiofiles,
        0,
    )
    audiopath = os.path.join(avdir, filename)
    st.audio(audiopath)


st.header("Generated audio (440Hz sine wave)")


def note(freq, length, amp, rate):
    t = np.linspace(0, length, length * rate)
    data = np.sin(2 * np.pi * freq * t) * amp
    return data.astype(np.int16)


frequency = 440  # hertz
nchannels = 1
sampwidth = 2
sampling_rate = 44100
duration = 89  # Max size, given the bitrate and sample width
comptype = "NONE"
compname = "not compressed"
amplitude = 10000
nframes = duration * sampling_rate

x = st.text("Making wave...")
sine_wave = note(frequency, duration, amplitude, sampling_rate)

fh = wave.open("sound.wav", "w")
fh.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))

x.text("Converting wave...")
fh.writeframes(sine_wave)

fh.close()

with io.open("sound.wav", "rb") as f:
    x.text("Sending wave...")
    x.audio(f)

st.header("Audio from a Remote URL")


def shorten_audio_option(opt):
    return opt.split("/")[-1]


song = st.selectbox(
    "Pick an MP3 to play",
    (
        "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
        "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3",
        "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3",
    ),
    0,
    shorten_audio_option,
)

st.audio(song)

st.title("Streaming audio from a URL")

st.write("[MP3: Mutiny Radio](http://nthmost.net:8000/mutiny-studio)")

st.audio("http://nthmost.net:8000/mutiny-studio")

st.write("[OGG: Radio Loki](http://nthmost.net:8000/loki.ogg)")

st.audio("http://nthmost.net:8000/loki.ogg")

#load data
#url = 'https://raw.githubusercontent.com/davidrkearney/Kearney_Data_Science/master/_notebooks/df_panel_fix.csv'
#url = 'https://raw.githubusercontent.com/davidrkearney/colab-notebooks/main/datasets/depression_data.csv'
url='https://raw.githubusercontent.com/davidrkearney/colab-notebooks/main/datasets/diabetes.csv'



train_set = pd.read_csv(url, error_bad_lines=False)

if page == "Home":
    run_home(train_set)

elif page == "Pandas Profile":
    run_pandas(train_set)

elif page == "Audio Page":
    run_audio()

else:
    run_graphs(train_set)
