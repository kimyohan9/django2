# def count_word(Word):
#     count = 0
#     for i in Word:
#         count += len(i)
#     return count

def count_words_in_text(text):
    """텍스트에서 단어 개수를 세는 함수"""
    words = text.split()  # 공백을 기준으로 단어 분리
    return len(words)

def count_words_in_file(file_path):
    """파일에서 단어 개수를 세는 함수"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return count_words_in_text(text)  # 위에서 만든 함수 사용
    except FileNotFoundError:
        print(f"오류: '{file_path}' 파일을 찾을 수 없습니다.")
        return 0  # 파일이 없을 경우 0 반환