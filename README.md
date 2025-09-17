# MistralChatCLI

This document is available in English and Traditional Chinese.
本文件提供英文及繁體中文版本。

---

`MistralChatCLI` is a simple, interactive command-line interface (CLI) chatbot powered by the [Mistral AI API](https://docs.mistral.ai/). It supports continuous conversation with streaming responses for a smooth, real-time interactive experience.

**MistralChatCLI** 是一個簡單、互動式的命令列介面 (CLI) 聊天機器人，由 [Mistral AI API](https://docs.mistral.ai/) 驅動。它支援持續對話，並能以串流方式即時顯示 AI 的回應，提供流暢的互動體驗。

## ✨ Features / 功能

*   **Interactive Chat:** Engage in a conversation with Mistral AI directly in your terminal.
*   **Conversation History:** The script remembers the current conversation context, allowing for more coherent responses from the AI.
*   **Streaming Responses:** AI responses are displayed in real-time as they are generated, so you don't have to wait for the full response.
*   **Easy Setup:** Get started by simply configuring your API key.
*   **Cross-Platform:** Runs on Windows, macOS, and Linux.

---

*   **互動式對話:** 在您的終端機中直接與 Mistral AI 進行對話。
*   **支援對話歷史:** 程式會記住當前的對話上下文，讓 AI 的回應更連貫。
*   **串流回應:** AI 的回應會以串流方式即時顯示，無需等待完整回應生成。
*   **簡易設定:** 只需設定您的 API 金鑰即可開始使用。
*   **跨平台:** 可在 Windows, macOS, 和 Linux 上運行。

## 📋 Requirements / 環境需求

*   Python 3.6 or higher
*   `pip` (Python package installer)

---

*   Python 3.6 或更高版本
*   `pip` (Python 套件安裝程式)

## 🚀 Installation and Setup / 安裝與設定

#### 1. Clone or Download the Repository / 複製或下載儲存庫

Clone the repository using git:
```bash
git clone https://github.com/your-username/MistralChatCLI.git
cd MistralChatCLI
```
Alternatively, you can download the `mistral_chat_cli.py` file directly.

(或者，您也可以直接下載 `mistral_chat_cli.py` 檔案。)

#### 2. Install Required Packages / 安裝必要的套件

This project depends on the `mistralai` Python client. Install it using pip:
(本專案依賴 `mistralai` Python 客戶端。使用 pip 進行安裝：)
```bash
pip install mistralai
```

#### 3. Configure Your Mistral API Key / 設定您的 Mistral API 金鑰

Before running the script, you need to set your Mistral API key. There are two ways to do this:
(在執行程式之前，您需要設定您的 Mistral API 金鑰。有兩種方法：)

**Method 1: Environment Variable (Recommended) / 方法一：環境變數 (建議)**
Set an environment variable named `MISTRAL_API_KEY`. This is the more secure method as it avoids hardcoding your key in the source code.
(設定一個名為 `MISTRAL_API_KEY` 的環境變數。這是更安全的方法，因為您不會將金鑰硬編碼在程式碼中。)

*   **On macOS/Linux:**
    ```bash
    export MISTRAL_API_KEY="your_api_key_here"
    ```
*   **On Windows (Command Prompt):**
    ```bash
    set MISTRAL_API_KEY="your_api_key_here"
    ```
*   **On Windows (PowerShell):**
    ```bash
    $env:MISTRAL_API_KEY="your_api_key_here"
    ```

**Method 2: Edit the Source Code / 方法二：直接在程式碼中修改**
Open the `mistral_chat_cli.py` file and replace `"XXXX"` with your API key.
(打開 `mistral_chat_cli.py` 檔案，找到下面這行並將 `"XXXX"` 替換為您的 API 金鑰。)

```python
# Please replace "XXXX" with your Mistral API key
API_KEY = "XXXX"
```

> **Warning:** Hardcoding API keys is not recommended, especially if your code will be pushed to a public repository.
> (**警告：** 不建議將 API 金鑰直接寫在程式碼中，特別是如果您的程式碼會被上傳到公開的儲存庫。)

## 🏃‍♂️ How to Use / 如何使用

Once the setup is complete, simply run the Python script to start the conversation:
(完成設定後，只需執行 Python 腳本即可開始對話：)

```bash
python mistral_chat_cli.py
```

After the script starts, you will see the `You (您):` prompt. Type your message and press Enter.
(程式啟動後，您會看到提示符 `您 (You):`。直接輸入您的問題或訊息，然後按 Enter。)

To end the session, type `exit`, `quit`, or `退出`.
(若要結束對話，請輸入 `exit`, `quit`, 或 `退出`。)

**Example Conversation / 範例對話:**
```
Start chatting with Mistral AI. Type 'exit', 'quit', or '退出' to end the session.
與 Mistral AI 開始對話。輸入 'exit', 'quit', 或 '退出' 來結束對話。
------------------------------
您 (You): Hello, please introduce yourself in Traditional Chinese.
AI: 你好！我是一個由 Mistral AI 開發的大型語言模型。我可以回答你的問題、提供資訊、進行翻譯、撰寫文章，以及完成各種語言相關的任務。有什麼可以幫助你的嗎？
------------------------------
您 (You): exit
對話結束。(Conversation ended.)
```

## 📄 Full Code / 完整程式碼

The complete code is contained in the `mistral_chat_cli.py` file, with detailed bilingual comments.
(完整的程式碼包含在 `mistral_chat_cli.py` 檔案中，並附有詳細的雙語註解。)

```python
# -*- coding: utf-8 -*-

import os
import sys
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

def main():
    """
    主函數，啟動一個與 Mistral AI 的可持續對話。
    The main function to start a continuous conversation with Mistral AI.
    """
    # --- 1. 初始化設定 (Initialization) ---
    # 請將 "XXXX" 替換為您的 Mistral API 金鑰
    # Please replace "XXXX" with your Mistral API key
    API_KEY = "XXXX"

    # 優先從環境變數讀取 API 金鑰
    # Prioritize reading the API key from environment variables
    api_key = os.getenv("MISTRAL_API_KEY", API_KEY)
    if not api_key or api_key == "XXXX":
        print("錯誤：請設定您的 MISTRAL_API_KEY 環境變數或在程式碼中填寫 API_KEY。")
        print("Error: Please set your MISTRAL_API_KEY environment variable or fill in the API_KEY in the code.")
        return

    # 設定要使用的模型
    # Set the model to be used
    model = "mistral-large-latest"

    try:
        # 初始化 Mistral 客戶端
        # Initialize the Mistral client
        client = MistralClient(api_key=api_key)
    except Exception as e:
        print(f"初始化 MistralClient 時發生錯誤 (Error initializing MistralClient): {e}")
        return

    # --- 2. 對話歷史紀錄 (Conversation History) ---
    # 儲存整個對話的上下文
    # Stores the context of the entire conversation
    messages = []

    print("與 Mistral AI 開始對話。輸入 'exit', 'quit', 或 '退出' 來結束對話。")
    print("Start chatting with Mistral AI. Type 'exit', 'quit', or '退出' to end the session.")
    print("-" * 30)

    # --- 3. 對話迴圈 (Conversation Loop) ---
    while True:
        try:
            # 獲取使用者輸入
            # Get user input
            user_input = input("您 (You): ")

            # 檢查退出指令
            # Check for exit commands
            if user_input.lower() in ["exit", "quit", "退出"]:
                print("對話結束。(Conversation ended.)")
                break

            # 將使用者的輸入加入到對話歷史中
            # Add the user's input to the conversation history
            messages.append(ChatMessage(role="user", content=user_input))

            print("\nAI: ", end="")

            # --- 4. 呼叫 API 並處理串流回應 (Call API and Handle Stream Response) ---
            # 使用 client.chat_stream 方法來啟用串流
            # Use the client.chat_stream method to enable streaming
            stream_response = client.chat_stream(
                model=model,
                messages=messages,
            )

            # 用來收集完整的 AI 回應
            # Used to collect the full AI response
            ai_full_response = ""

            # 遍歷回應的每一個區塊 (chunk)
            # Iterate over each chunk of the response
            for chunk in stream_response:
                chunk_content = chunk.choices.delta.content
                if chunk_content is not None:
                    # 將內容即時印出
                    # Print the content in real-time
                    print(chunk_content, end="")
                    sys.stdout.flush()
                    # 收集回應內容
                    # Collect the response content
                    ai_full_response += chunk_content

            # 將完整的 AI 回應加入到對話歷史中
            # Add the complete AI response to the conversation history
            if ai_full_response:
                messages.append(ChatMessage(role="assistant", content=ai_full_response))

            # 在 AI 回應結束後換行
            # Add a newline after the AI's response is complete
            print("\n" + "-" * 30)

        except KeyboardInterrupt:
            # 允許使用 Ctrl+C 來中斷程式
            # Allow interruption with Ctrl+C
            print("\n對話被中斷。(Conversation interrupted.)")
            break
        except Exception as e:
            print(f"\n發生錯誤 (An error occurred): {e}")
            break

if __name__ == "__main__":
    main()

```

## 📄 License / 授權

This project is licensed under the [MIT License](LICENSE).
(本專案採用 [MIT 授權條款](LICENSE)。)
