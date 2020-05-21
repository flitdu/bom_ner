from utils import load_model, extend_maps, prepocess_data_for_lstmcrf
from data import build_corpus
from evaluating import Metrics
from evaluate import ensemble_evaluate

HMM_MODEL_PATH = './ckpts/hmm.pkl'
CRF_MODEL_PATH = './ckpts/crf.pkl'
BiLSTM_MODEL_PATH = './ckpts/bilstm.pkl'
BiLSTMCRF_MODEL_PATH = './ckpts/bilstm_crf.pkl'

REMOVE_O = False  # 在评估的时候是否去除O标记


if __name__ == "__main__":
    print("读取数据...")
    train_word_lists, train_tag_lists, word2id, tag2id = \
        build_corpus("train")
    test_word_lists, test_tag_lists = build_corpus("test", make_vocab=False)
    print('@@@', test_word_lists, test_tag_lists)

    line = input('带预测行：')


    print("加载并评估bilstm+crf模型...")
    crf_word2id, crf_tag2id = extend_maps(word2id, tag2id, for_crf=True)
    # 加载模型
    bilstm_model = load_model(BiLSTMCRF_MODEL_PATH)
    bilstm_model.model.bilstm.bilstm.flatten_parameters()  # remove warning
    test_word_lists, test_tag_lists = prepocess_data_for_lstmcrf(
        test_word_lists, test_tag_lists, test=True
    )
    lstmcrf_pred, target_tag_list = bilstm_model.test(test_word_lists, test_tag_lists,
                                                      crf_word2id, crf_tag2id)
    print(f'预测实体: {lstmcrf_pred}')
    metrics = Metrics(target_tag_list, lstmcrf_pred, remove_O=REMOVE_O)
    metrics.report_scores()
    metrics.report_confusion_matrix()
