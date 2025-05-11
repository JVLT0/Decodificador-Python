from core.encryption.caesar import CaesarCipher
from core.validation import hybrid_validation
from core.correction import suggest_correction
from utils.visualization import generate_plots

history = []


def decrypt_caesar(text):
    cipher = CaesarCipher()
    best_score = -1
    best_decryption = ""
    best_shift = 0
    scores = []
    last_glc = last_bert = last_dict = 0

    for shift in range(1, 26):
        decrypted = cipher.decrypt(text, shift)
        score, glc, bert, dic = hybrid_validation(decrypted)
        scores.append((shift, score))
        if score > best_score:
            best_score = score
            best_decryption = decrypted
            best_shift = shift
            last_glc, last_bert, last_dict = glc, bert, dic

    history.append((text, best_shift, best_score))
    avg_score = sum(score for _, _, score in history) / len(history)
    total_attempts = len(history)

    corrected = suggest_correction(best_decryption)
    line_chart, pie_chart = generate_plots(scores, last_glc, last_bert, last_dict)

    result_text = (
        f"\U0001F513 Decodificado: {best_decryption}\n"
        f"\U0001F527 Sugestão: {corrected}\n\n"
        f"\U0001F510 Shift: {best_shift}\n"
        f"\U0001F4C8 Score: {best_score:.2f}\n\n"
        f"\U0001F4CA Tentativas: {total_attempts}\n"
        f"\U0001F4C9 Média Score: {avg_score:.2f}"
    )

    return result_text, line_chart, pie_chart