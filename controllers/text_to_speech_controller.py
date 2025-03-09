import asyncio
import edge_tts
import pygame
import os

# 初始化 pygame 混音器
pygame.mixer.init()

async def speak_text_async(status_label, text, voice_name):
    try:
        # 更新状态栏
        status_label.configure(text="正在合成语音...")
        
        # 使用 edge_tts 将文本转换为语音
        communicate = edge_tts.Communicate(text, voice_name)
        await communicate.save("output.mp3")
        
        # 播放生成的音频文件
        play_audio("output.mp3")
        
        # 更新状态栏
        status_label.configure(text="播放完成")
    except Exception as e:
        status_label.configure(text=f"播放失败: {e}")

def speak_text(status_label, text, voice_name):
    asyncio.run(speak_text_async(status_label, text, voice_name))

def play_audio(file_path):
    # 使用 pygame 播放音频
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def stop_speaking(status_label):
    # 停止播放音频
    pygame.mixer.music.stop()
    status_label.configure(text="已停止播放")