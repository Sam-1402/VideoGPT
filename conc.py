from moviepy.editor import*
vname = ['58142', '3654', '12060', '42420']
clip1 = VideoFileClip(vname[0]+".mp4")
clip2 = VideoFileClip(vname[1]+".mp4")
clip3 = VideoFileClip(vname[2]+".mp4")
clip4 = VideoFileClip(vname[3]+".mp4")
full_len_video = concatenate_videoclips([clip1, clip2, clip3, clip4])
final_video = full_len_video.subclip(1, 62)
audioclip = AudioFileClip("E://Python_pr/speech/speech.mp3")
final_clip = final_video.set_audio(audioclip)
final_clip.write_videofile("new.mp4", fps=60)