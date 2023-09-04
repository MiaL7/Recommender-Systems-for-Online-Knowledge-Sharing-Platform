# Recommender Systems for Online Knowledge Sharing Platform

## Files

```bash
.
├── Baseline-CF.ipynb
├── Baseline-Recbole.ipynb
├── README.md
├── RecBole
├── RecBole-GNN-main
├── Recbole-NGCF.ipynb
├── ZhihuRec-1M-Generator.ipynb
├── ZhihuRec-NetGen.ipynb
├── bole
├── data-visual-answer.ipynb
├── data-visual-question.ipynb
├── data-visual-user.ipynb
├── dataset-generator.ipynb
└── train-val-test-dataset-gen.ipynb
```

## How to run

All code are in Jupyter Notebooks.

```bash
jupyter nobook
```

We didn't include the whole ZhihuRec dataset here. Please download the original dataset [here](https://github.com/THUIR/ZhihuRec-Dataset) if interested.

- `ZhihuRec-1M-Generator.ipynb` is used to generate ZhihuRec1M dataset
- `ZhihuRec-NetGen.ipynb` is used to generate user graph data
- To split the train-validation-test set, please run `train-val-test-dataset-gen.ipynb`
- Feel free to check out the explorationary data analysis in `data-visual-answer.ipynb`, `data-visual-question.ipynb`, and `data-visual-user.ipynb`
- `Baseline-CF.ipynb` is the implementation of baseline methods using Surprise
- `Baseline-Recbole.ipynb` and `Recbole-NGCF.ipynb` is the implementation of our methods using RecBole
