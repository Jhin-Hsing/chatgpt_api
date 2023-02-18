import openai

# 設定 API 金鑰
openai.api_key = "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"

# 定義 GPT-3 模型的名稱
model_engine = "text-davinci-002"

# 定義您要生成的文本
prompt = input("你好!，請輸入對話:")

# 呼叫 GPT-3 生成結果
completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

# 輸出生成的文本
message = completions.choices[0].text
print(message)