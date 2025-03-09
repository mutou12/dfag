import asyncio
import edge_tts
import pygame
import os
import tempfile

# 初始化 Pygame
pygame.init()

# 初始化混音器
pygame.mixer.init()

# 创建临时文件夹用于存储音频文件
temp_dir = os.path.join(tempfile.gettempdir(), "dfag_audio")
os.makedirs(temp_dir, exist_ok=True)

async def speak_text_async(status_label, text, voice_name, speak_button):
    """
    异步函数，用于将文本转换为语音并播放
    """
    try:
        # 在临时目录中创建唯一的音频文件
        temp_file = os.path.join(temp_dir, "output.mp3")
        
        # 使用 edge_tts 将文本转换为语音
        communicate = edge_tts.Communicate(text, voice_name)
        await communicate.save(temp_file)
        
        # 播放生成的音频文件
        play_audio(temp_file, speak_button, status_label)
        
    except Exception as e:
        status_label.configure(text=f"播放失败: {str(e)}")
        speak_button.configure(state="normal")

def speak_text(status_label, text, voice_name, speak_button):
    """
    启动异步任务，将文本转换为语音并播放
    """
    # 更新状态栏
    status_label.configure(text="正在合成语音...")
    asyncio.run(speak_text_async(status_label, text, voice_name, speak_button))

def play_audio(file_path, speak_button, status_label):
    """
    使用 pygame 播放音频文件
    """
    try:
        # 禁用播放按钮
        speak_button.configure(state="disabled")
        
        # 更新状态栏
        status_label.configure(text="正在播放...")
        
        # 使用 pygame 播放音频
        audio = pygame.mixer.Sound(file_path)
        audio.play()
        
        # 等待音频播放完成
        while pygame.mixer.get_busy():
            pygame.time.Clock().tick(10)  # 防止 CPU 占用率过高
        
        # 播放完成后删除临时文件
        os.remove(file_path)
        status_label.configure(text="播放完成")
        speak_button.configure(state="normal")
        
    except Exception as e:
        status_label.configure(text=f"播放音频失败: {str(e)}")
        speak_button.configure(state="normal")

def stop_speaking(status_label, speak_button):
    """
    停止播放音频
    """
    try:
        # 停止播放音频
        pygame.mixer.stop()
        # 删除临时文件
        temp_file = os.path.join(temp_dir, "output.mp3")
        if os.path.exists(temp_file):
            os.remove(temp_file)
        status_label.configure(text="已停止播放")
        speak_button.configure(state="normal")
    except Exception as e:
        status_label.configure(text=f"停止失败: {str(e)}")
        speak_button.configure(state="normal")