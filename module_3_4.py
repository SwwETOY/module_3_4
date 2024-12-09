def single_root_words(root_word, *other_words):
    same_words = []
    root_word_lower = root_word.lower()  # в нижний регистр

    for word in other_words:
        word_lower = word.lower()  # в нижний регистр
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)

    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)


# 1) Объявите функцию single_root_words и напишите в ней параметры root_word и *other_words.
# 2) Создайте внутри функции пустой список same_words, который пополнится нужными словами.
# 3) При помощи цикла for переберите предполагаемо подходящие слова.
# 4) Пропишите корректное относительно задачи условие, при котором добавляются слова в результирующий список same_words.
# 5) После цикла верните образованный функцией список same_words.
# 6) Вызовите функцию single_root_words и выведете на экран(консоль) возвращённое ей значение.

# вывод в консоль
# ['richiest', 'orichalcum', 'richies']
# ['Able', 'Disable']

# Примечания:
# 1) При проверке наличия одного слова в составе другого стоит учесть, что регистр символов не должен влиять ни на что.
# ('Disablement' - 'Able') ('Able', 'able', 'AbLe' - все подходят)
# 2) В этой задаче вам могут понадобиться следующие методы строк/ключевые слова:
# а. Оператор in или count()
# b. lower()/upper().


