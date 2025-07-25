from mistralrs import Runner, Which, ChatCompletionRequest, VisionArchitecture

runner = Runner(
    which=Which.VisionPlain(
        model_id="microsoft/Phi-3.5-vision-instruct",
        arch=VisionArchitecture.Phi3V,
    ),
)

FILENAME = "picture.jpg"

res = runner.send_chat_completion_request(
    ChatCompletionRequest(
        model="default",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": FILENAME,
                        },
                    },
                    {
                        "type": "text",
                        "text": "<|image_1|>\nWhat is shown in this image? Write a detailed response analyzing the scene.",
                    },
                ],
            }
        ],
        max_tokens=256,
        presence_penalty=1.0,
        top_p=0.1,
        temperature=0.1,
    )
)
print(res.choices[0].message.content)
print(res.usage)
