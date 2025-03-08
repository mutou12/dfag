import customtkinter as ctk
from controllers import text_to_speech_controller

class TextToSpeechFrame(ctk.CTkFrame):
    def __init__(self, master, switch_frame, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        # 创建界面组件
        self.create_widgets(switch_frame)
    
    def create_widgets(self, switch_frame):
        # 标题
        title_label = ctk.CTkLabel(self, text="文本转语音", font=("Microsoft YaHei", 24, "bold"))
        title_label.pack(pady=20)
        
        # 文本输入框
        input_frame = ctk.CTkFrame(self)
        input_frame.pack(fill="x", padx=20, pady=10)
        
        input_label = ctk.CTkLabel(input_frame, text="输入文本:", font=("Microsoft YaHei", 12))
        input_label.pack(anchor="w", padx=10, pady=5)
        
        self.text_input = ctk.CTkTextbox(input_frame, height=150, font=("Microsoft YaHei", 12))
        self.text_input.pack(fill="x", padx=10, pady=5)
        
        # 语音选择下拉菜单
        voice_frame = ctk.CTkFrame(self)
        voice_frame.pack(fill="x", padx=20, pady=10)
        
        voice_label = ctk.CTkLabel(voice_frame, text="选择语音:", font=("Microsoft YaHei", 12))
        voice_label.pack(side="left", padx=10, pady=5)
        
        # 硬编码语音名称列表
        voice_names = ["zh-CN-XiaoxiaoNeural", "en-US-JennyNeural"]
        self.voice_var = ctk.StringVar(value=voice_names[0])
        voice_option = ctk.CTkOptionMenu(voice_frame, values=voice_names, 
                                         variable=self.voice_var, font=("Microsoft YaHei", 12))
        voice_option.pack(side="left", fill="x", expand=True, padx=10, pady=5)
        
        # 播放按钮
        button_frame = ctk.CTkFrame(self)
        button_frame.pack(fill="x", padx=20, pady=20)
        
        self.speak_button = ctk.CTkButton(button_frame, text="播放语音", font=("Microsoft YaHei", 14),
                                         command=self.speak_text)
        self.speak_button.pack(side="left", fill="x", expand=True, padx=10)
        
        self.stop_button = ctk.CTkButton(button_frame, text="停止", font=("Microsoft YaHei", 14),
                                        command=self.stop_speaking)
        self.stop_button.pack(side="left", fill="x", expand=True, padx=10)
        
        # 返回主菜单按钮
        back_button = ctk.CTkButton(button_frame, text="返回主菜单", font=("Microsoft YaHei", 14),
                                    command=lambda: switch_frame("MainMenu"))
        back_button.pack(side="left", fill="x", expand=True, padx=10)
        
        # 状态栏
        self.status_label = ctk.CTkLabel(self, text="就绪", font=("Microsoft YaHei", 10))
        self.status_label.pack(side="bottom", fill="x", padx=20, pady=10)
    
    def speak_text(self):
        # 调用 text_to_speech_controller.py 中的 speak_text 函数
        text_to_speech_controller.speak_text(self.status_label)
    
    def stop_speaking(self):
        # 调用 text_to_speech_controller.py 中的 stop_speaking 函数
        text_to_speech_controller.stop_speaking(self.status_label)