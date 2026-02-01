import ollama

prompt = "Analyse this image and tell me what is it. You must return a JSON object with the key 'description'."

def ai_analyse(img_name):
    image_path = f"./webpage_screenshots/{img_name}"
    
    response = ollama.chat(
        model='qwen3-vl:4b',
        messages=[{
            'role': 'user',
            'content': prompt,
            'images': [image_path]
        }]
    )
    
    result = response['message']['content']
    print(result)
    return result

def report(list_img): 
    list_desc = []
    for img in list_img:
        img_desc = ai_analyse(img)
        list_desc.append(img_desc)
    return list_desc