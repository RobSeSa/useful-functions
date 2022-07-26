


def f1_score(precision, recall):
    print(f"Computing F1 score using precision {precision} and recall {recall}")
    F1 = 2 * (precision * recall) / (precision + recall)
    print("F1:", F1)
    return F1
