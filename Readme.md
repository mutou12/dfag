# 文本到语音程序

这是一个简单的文本到语音程序，使用 `customtkinter` 作为 GUI 框架。

## 项目结构
Project_Code\
 │ ├── dfag\
 │ ├── views # 用于存放UI相关的代码\
  │ │ ├── text_to_speech_view.py\
 │ │ └── init.py\
 │ ├── controllers # 用于存放事件处理相关的代码\
  │ │ ├── text_to_speech_controller.py\
   │ │ └── init.py\
    │ ├── main.py # 主程序入口\
     │ └── init.py\
      └── README.md
      
## 安装依赖

使用 `poetry` 来管理项目依赖。首先，确保你已经安装了 `poetry`，然后在项目根目录下运行以下命令来安赖：


## 运行程序
在项目根目录下运行以下命令来启动程序：

```sh
poetry run python dfag_code/main.py
```