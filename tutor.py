import ollama

import time

import os



# Файл, который мы будем проверять

FILE_TO_WATCH = "check_me.py"



def get_file_content():

    with open(FILE_TO_WATCH, "r", encoding="utf-8") as f:

        return f.read()



def ask_llama(code):

    # Тот самый "промпт" для учителя

    prompt = f"""

    Проверь этот код на Python:

    {code}



    Если в коде есть ошибка:

    1. Напиши: "ОШИБКА НАЙДЕНА"

    2. Объясни очень просто, что не так.

    3. Напиши, как исправить.
    

    Если в коде есть комментарии со знаками вопроса (например, # как мне сделать...), ОТВЕТЬ на них максимально просто

    Если код идеален и в нем нет синтаксических ошибок, напиши просто одно слово: "КРАСАВА".

    """



    response = ollama.chat(model='llama3', messages=[

        {'role': 'user', 'content': prompt},

    ])

    return response['message']['content']


def main():

    print(f"👀 Учитель заступил на дежурство. Слежу за файлом {FILE_TO_WATCH}...")

    

    last_content = ""



    while True:

        # Читаем код из файла

        current_content = get_file_content()



        # Если содержимое изменилось (ты нажал Сохранить)

        if current_content != last_content:

            if current_content.strip(): # Проверяем, что файл не пустой

                print("\n🔍 Вижу изменения! Проверяю...")

                

                result = ask_llama(current_content)

                

                if "КРАСАВА" in result:

                    print("✅ Ошибок нет, ты молодец!")

                else:

                    print("\n⚠️  СОВЕТ УЧИТЕЛЯ:")

                    print(result)

            

            last_content = current_content

        

        # Ждем 2 секунды перед следующей проверкой, чтобы не перегреть комп

        time.sleep(2)



if __name__ == "__main__":

    main()