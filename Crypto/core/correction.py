import re
import difflib
from core.validation import tokenizer, model, DICTIONARY
import torch

def suggest_correction(sentence):
    words = sentence.split()
    corrected = words.copy()

    for i, word in enumerate(words):
        clean_word = re.sub(r'[^\w\s]', '', word.lower())

        if clean_word in DICTIONARY:
            continue

        close_matches = difflib.get_close_matches(clean_word, DICTIONARY, n=1, cutoff=0.8)
        if close_matches:
            corrected[i] = close_matches[0]
            continue

        masked = words.copy()
        masked[i] = '[MASK]'
        masked_sentence = ' '.join(masked)

        inputs = tokenizer(masked_sentence, return_tensors="pt")
        with torch.no_grad():
            outputs = model(**inputs)
            predictions = outputs.logits

        mask_token_index = (inputs.input_ids == tokenizer.mask_token_id).nonzero(as_tuple=True)[1]
        predicted_token_ids = torch.topk(predictions[0, mask_token_index, :], k=5, dim=-1).indices[0]

        for token_id in predicted_token_ids:
            suggestion = tokenizer.decode([token_id]).strip().lower()
            suggestion = re.sub(r"[^\w\s]", "", suggestion)
            if suggestion in DICTIONARY:
                corrected[i] = suggestion
                break
        else:
            corrected[i] = tokenizer.decode([predicted_token_ids[0]]).strip()

    return ' '.join(corrected)