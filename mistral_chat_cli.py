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
