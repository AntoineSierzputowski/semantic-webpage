import os
# return the img ['.jpg', '.jpeg', '.png'] in an array 
# the consumer of this function should handle logic based on the array

def read_local():
    array_img = []
    path = "./webpage_screenshots"
    
    if not os.path.exists(path):
        print(f"Directory '{path}' does not exist.")
        return array_img
    
    dir_list = os.listdir(path)
    for file in dir_list:
        extension = os.path.splitext(file)[1]
        if extension.lower() in ['.jpg', '.jpeg', '.png']:
            array_img.append(file)
    
    return array_img