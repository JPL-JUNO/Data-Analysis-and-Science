"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-11-19 21:29:24
@Description: 
"""
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.figure import Figure


def ts_plot(train, test,
            pred_label: str = 'pred',
            xticks_span: int = 5,
            xticks: list = None) -> Figure:
    train_length = len(train)
    test_length = len(test)
    total_sample = train_length + test_length
    if xticks is None:
        xticks = range(total_sample / xticks_span) + 1
    fig, ax = plt.subplots()
    for (data, shape, label) in zip([train, test], ['g-', 'b-'],
                                    ['train', 'test']):
        ax.plot(data['date'], data['data'], shape, label=label)
    ax.plot(test['date'], test[pred_label], 'r--', label='Predicted')
    ax.set_xlabel('Date')
    ax.set_ylabel('True Value vs Predicted Value')
    ax.axvspan(train_length, train_length + test_length -
               1, color='#808080', alpha=.2)
    ax.legend()
    fig.autofmt_xdate()
    plt.xticks(np.arange(0, total_sample, xticks_span), xticks)
    plt.tight_layout()
    return fig
