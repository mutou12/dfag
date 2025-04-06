import customtkinter as ctk
import threading
import asyncio
import multiprocessing

class ProcessVisualizationFrame(ctk.CTkFrame):
    def __init__(self, master, switch_frame, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        # 创建界面组件
        self.create_widgets(switch_frame)
    
    def create_widgets(self, switch_frame):
        # 标题
        title_label = ctk.CTkLabel(self, text="进程/协程/线程可视化", font=("Microsoft YaHei", 24, "bold"))
        title_label.pack(pady=20)
        
        # 显示线程信息
        process_button = ctk.CTkButton(self, text="进程信息", font=("Microsoft YaHei", 14),
                                      command=self.show_thread_info)
        process_button.pack(pady=10)

        # 显示线程信息
        thread_button = ctk.CTkButton(self, text="显示线程信息", font=("Microsoft YaHei", 14),
                                      command=self.show_thread_info)
        thread_button.pack(pady=10)
        
        
        # 显示协程信息
        coroutine_button = ctk.CTkButton(self, text="显示协程信息", font=("Microsoft YaHei", 14),
                                         command=self.show_coroutine_info)
        coroutine_button.pack(pady=10)
        
        # 返回主菜单按钮
        back_button = ctk.CTkButton(self, text="返回主菜单", font=("Microsoft YaHei", 14),
                                    command=lambda: switch_frame("MainMenu"))
        back_button.pack(pady=10)
        
        # 状态显示
        self.status_label = ctk.CTkLabel(self, text="状态: 就绪", font=("Microsoft YaHei", 12))
        self.status_label.pack(pady=10)
    
    def show_thread_info(self):
        # 获取当前线程信息
        current_thread = threading.current_thread()
        self.status_label.configure(text=f"当前线程: {current_thread.name}")
    
    def show_coroutine_info(self):
        # 模拟协程信息
        loop = asyncio.get_event_loop()
        self.status_label.configure(text=f"事件循环: {loop}")

    
    def show_process(self):
        # 举一个进程的例子
        # 创建一个进程
        process = multiprocessing.Process(target=self.process_task)
        process.start()
        process.join()

    def process_task(self):
        # 进程任务
        print("进程任务开始")
        # 模拟一些工作
        time.sleep(2)
        print("进程任务结束")