def decrypt_story():
    cipherText = CiphertextMessage(get_story_string())
    return cipherText.decrypt_message()
