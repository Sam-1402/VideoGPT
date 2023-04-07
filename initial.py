import pyttsx3
import time
import os
import re
import openai
import requests
from moviepy.editor import*

#hello to git
openai.api_key = "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"
keyword = str(input("Enter the keyword you want to search for: "))
prompt1= "write a script for youtube video for explaining "+ keyword +" in 140 words"
response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt1,
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)


# with open('generated_text.txt', 'w') as f:
#     f.write(whole_paragraph)
# with open('generated_text.txt', 'r') as f:
#     text = f.read()
engine = pyttsx3.init()
engine.setProperty('rate', 140)
  # txt_clip = TextClip(para, fontsize = 15, color = 'red')
  # txt_clip = txt_clip.set_pos('center').set_duration(speech.duration)
  # fin_txt_clip = concatenate_videoclips([fin_txt_clip, txt_clip]) 

speak = response.choices[0].text
engine.save_to_file(speak, 'E://Python_pr/speech/speech.mp3')
engine.runAndWait()
speech = AudioFileClip("E://Python_pr/speech/speech.mp3")
length_sec = speech.duration

print(length_sec)


i=0
vname = []
url = f'https://pixabay.com/api/videos/?key=33228610-44ddd03b50b7504fcdd921acc&q={keyword}'
r = requests.get(url)
json_data = r.json()
# print(json_data)
for video in json_data['hits']:
  name = video['id']
  largevid = video['videos']['large']
  video_url = video['videos']['large']['url']
  if(video_url==""):
    continue
  duration = int(video['duration'])
  r = requests.get(video_url, stream=True)
  with open(str(name)+'.mp4', 'wb') as f:
    f.write(r.content)
    print(duration)
    vname.append(str(name))
    length_sec = length_sec-duration
    i=i+1
  if(length_sec<0):
    break


print(vname)
if(i==1):
  full_len_video = VideoFileClip(vname[0]+".mp4")
elif(i==2):
  clip1 = VideoFileClip(vname[0]+".mp4")
  clip2 = VideoFileClip(vname[1]+".mp4")
  full_len_video = concatenate_videoclips([clip1,clip2])
elif(i==3):
  clip1 = VideoFileClip(vname[0]+".mp4")
  clip2 = VideoFileClip(vname[1]+".mp4")
  clip3 = VideoFileClip(vname[2]+".mp4")
  full_len_video = concatenate_videoclips([clip1, clip2, clip3])
elif(i==4):
  clip1 = VideoFileClip(vname[0]+".mp4")
  clip2 = VideoFileClip(vname[1]+".mp4")
  clip3 = VideoFileClip(vname[2]+".mp4")
  clip4 = VideoFileClip(vname[3]+".mp4")
  full_len_video = concatenate_videoclips([clip1, clip2, clip3, clip4])
elif(i==5):
  clip1 = VideoFileClip(vname[0]+".mp4")
  clip2 = VideoFileClip(vname[1]+".mp4")
  clip3 = VideoFileClip(vname[2]+".mp4")
  clip4 = VideoFileClip(vname[3]+".mp4")
  clip5 = VideoFileClip(vname[4]+".mp4")
  full_len_video = concatenate_videoclips([clip1, clip2, clip3, clip4, clip5])

final_clip = full_len_video.subclip(1, length_sec+2)
final_clip_withaudio = final_clip.set_audio(speech)
final_clip_withaudio.write_videofile("new.mp4", fps=60)
