class Hyperparams:
    """Hyperparameters"""

    # data
    source_train = "cut_cleaned_translation2019zh_txt/cut_cleaned_train.zh.txt"
    target_train = "cut_cleaned_translation2019zh_txt/cut_cleaned_train.en.txt"
    source_test = "cut_cleaned_translation2019zh_txt/cut_cleaned_valid.zh.txt"
    target_test = "cut_cleaned_translation2019zh_txt/cut_cleaned_valid.en.txt"

    # training
    batch_size = 48  # alias = N
    batch_size_valid = 32
    lr = (
        0.0001  # learning rate. In paper, learning rate is adjusted to the global step.
    )
    logdir = "logdir"  # log directory

    model_dir = "./models/"  # saving directory

    # model
    maxlen = 50  # Maximum number of words in a sentence. alias = T.
    min_cnt = 0  # words whose occurred less than min_cnt are encoded as <UNK>.
    hidden_units = 512  # alias = C
    num_blocks = 12  # number of encoder/decoder blocks
    num_epochs = 50
    num_heads = 8
    dropout_rate = 0.4
    sinusoid = False  # If True, use sinusoid. If false, positional embedding.
    eval_epoch = 1  # epoch of model for eval
    eval_script ="C:\\Users\\admin\\Desktop\\transformer\\attention is all you need\\scripts\\validate.sh"
    check_frequency = 10  # checkpoint frequency
