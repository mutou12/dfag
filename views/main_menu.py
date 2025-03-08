import customtkinter as ctk
from views.text_to_speech_view import TextToSpeechFrame

class MainMenu(ctk.CTkFrame):
    def __init__(self, master, switch_frame):
        super().__init__(master)
        
        # 创建界面组件
        self.create_widgets(switch_frame)
    
    def create_widgets(self, switch_frame):
        # 标题
        title_label = ctk.CTkLabel(self, text="主菜单", font=("Microsoft YaHei", 24, "bold"))
        title_label.pack(pady=20)
        
        # 文本转语音按钮
        tts_button = ctk.CTkButton(self, text="文本转语音", font=("Microsoft YaHei", 14),
                                   command=lambda: switch_frame("TextToSpeechFrame"))
        tts_button.pack(pady=10)
        
        # 其他功能按钮（占位）
        other_button = ctk.CTkButton(self, text="其他功能", font=("Microsoft YaHei", 14),
                                     command=lambda: switch_frame(None))  # 这里可以替换为其他功能的 Frame
        other_button.pack(pady=10)