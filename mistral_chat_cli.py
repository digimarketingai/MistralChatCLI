# -*- coding: utf-8 -*-

# 匯入必要的函式庫
# Import necessary libraries
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

    # 優先從環境變數讀取 API 金鑰，如果不存在，則使用程式碼中定義的 API_KEY
    # Prioritize reading the API key from environment variables. If it doesn't exist, use the API_KEY defined in the code.
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

    # 建立一個列表來儲存整個對話的上下文
    # Create a list to store the context of the entire conversation
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

            # 將使用者的輸入作為一個 'user' 角色訊息加入到對話歷史中
            # Add the user's input as a 'user' role message to the conversation history
            messages.append(ChatMessage(role="user", content=user_input))

            print("\nAI: ", end="")

            # --- 4. 呼叫 API 並處理串流回應 (Call API and Handle Stream Response) ---

            # 使用 client.chat_stream 方法來啟用串流，這會立即返回一個生成器對象
            # Use the client.chat_stream method to enable streaming, which returns a generator object immediately
            stream_response = client.chat_stream(
                model=model,
                messages=messages,
            )

            # 建立一個空字串，用來收集完整的 AI 回應
            # Create an empty string to collect the full AI response
            ai_full_response = ""

            # 遍歷回應的每一個區塊 (chunk)
            # Iterate over each chunk of the response
            for chunk in stream_response:
                # 獲取區塊中的內容
                # Get the content from the chunk
                chunk_content = chunk.choices[0].delta.content
                if chunk_content is not None:
                    # 將內容即時印出到控制台
                    # Print the content to the console in real-time
                    print(chunk_content, end="")
                    # 強制刷新輸出緩衝區，確保內容立即顯示
                    # Force flush the output buffer to ensure immediate display
                    sys.stdout.flush()
                    # 將區塊內容附加到完整回應字串中
                    # Append the chunk content to the full response string
                    ai_full_response += chunk_content

            # 當串流結束後，將完整的 AI 回應作為 'assistant' 角色訊息加入到對話歷史中
            # After the stream ends, add the complete AI response as an 'assistant' role message to the history
            if ai_full_response:
                messages.append(ChatMessage(role="assistant", content=ai_full_response))

            # 在 AI 回應結束後換行並印出分隔線
            # Add a newline and print a separator after the AI's response is complete
            print("\n" + "-" * 30)

        except KeyboardInterrupt:
            # 允許使用者使用 Ctrl+C 來中斷程式
            # Allow the user to interrupt the program with Ctrl+C
            print("\n對話被中斷。(Conversation interrupted.)")
            break
        except Exception as e:
            # 捕捉並印出其他可能的錯誤
            # Catch and print any other potential errors
            print(f"\n發生錯誤 (An error occurred): {e}")
            break

# 程式執行的進入點
# Entry point of the script
if __name__ == "__main__":
    main()
