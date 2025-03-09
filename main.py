import customtkinter as ctk
from views.main_menu import MainMenu
from views.text_to_speech_view import TextToSpeechFrame

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # 窗口设置
        self.title("主应用")
        self.geometry("700x500")
        self.resizable(False, False)
        
        # 创建容器框架
        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True)
        
        # 存储所有的页面
        self.frames = {}
        
        # 页面映射
        self.page_classes = {
            "MainMenu": MainMenu,
            "TextToSpeechFrame": TextToSpeechFrame
        }
        
        # 初始化页面
        self.show_frame("MainMenu")
    
    def show_frame(self, page_name):
        # 销毁当前页面
        for frame in self.frames.values():
            frame.pack_forget()
        
        # 如果页面不存在，则创建它
        if page_name not in self.frames:
            page_class = self.page_classes[page_name]
            frame = page_class(self.container, self.show_frame)
            self.frames[page_name] = frame
        else:
            frame = self.frames[page_name]
        
        # 显示页面
        frame.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = MainApp()
    app.protocol("WM_DELETE_WINDOW", app.destroy)
    app.mainloop()