# Counterfactual Defense Against Adversarial Attacks in ML-Based IDS

[![GitHub last commit](https://img.shields.io/github/last-commit/s-m-sharjeel/counterfactual-ml-ids?style=flat-square)](https://github.com/s-m-sharjeel/counterfactual-ml-ids/commits/main)
[![Python Version](https://img.shields.io/badge/python-3.11-blue?style=flat-square)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)

[comment]: [![DOI](https://img.shields.io/badge/DOI-10.xxxx/yyyyy-blue?style=flat-square)](https://doi.org/10.xxxx/yyyyy)

## Overview

This repository implements a two-layer defense mechanism for Machine Learning-based Intrusion Detection Systems (IDS) that combines:
- Random Forest classification
- Counterfactual reasoning using DiCE (Diverse Counterfactual Explanations)

The system detects both conventional network intrusions and sophisticated adversarial attacks in real-time while providing interpretable explanations.

## Key Features

- **Dual-layer defense architecture**
- **Explainable AI integration** with counterfactual explanations
- **Real-time capable** with optimized computational overhead
- **97% classification accuracy** on CIC-IDS2018 dataset
- **100% adversarial detection rate** using counterfactual verification

## Research Paper

This implementation accompanies our research paper:

**"Counterfactual Defense Against Adversarial Attacks in ML-Based Intrusion Detection Systems Using DiCE"**  
*Shaikh Muhammad Sharjeel, Omar Ashraf Khan, Muhammad Jawad Maqsood*  
Institute of Business Administration, Karachi, Pakistan

[comment]: [Download Paper (PDF)](#) | [DOI Link](#)

## Quick Start

### Prerequisites

- Python 3.11 (recommended)
- Kaggle API for dataset download (can be done manually)
- Basic machine learning knowledge

### Installation

1. Clone the repository:
```bash
git clone https://github.com/s-m-sharjeel/counterfactual-ml-ids.git
cd counterfactual-ml-ids
```

2. Set up a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install dependencies:

```bash
pip install -r requirements.txt
Dataset Setup
The implementation uses the CIC-IDS2018 dataset (specifically the Friday traffic capture). To automatically download and prepare the dataset:
```

5. Configure Kaggle API (requires account):

```bash
mkdir ~/.kaggle
cp kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json
```

6. Run the dataset setup script:

```bash
python scripts/download_dataset.py
```

Alternatively, manually download from:

- [Kaggle Dataset](https://www.kaggle.com/datasets/solarmainframe/ids-intrusion-csv?select=03-02-2018.csv)
- Official CIC-IDS2018

Place the CSV file in ./data/ directory.

7. Running the Notebook

- Launch Jupyter and open the main notebook:

```bash
jupyter notebook cicids-ids-2018-using-randomforest.ipynb
```

## Methodology

### System Architecture

[comment]: ![System Architecture Diagram](docs/system_architecture.png)

#### First Layer - Random Forest Classifier
- **Training Data**: Balanced CIC-IDS2018 dataset
- **Model Configuration**:
  - 100 decision trees
  - Maximum depth of 3
  - Bootstrap sampling enabled
- **Performance**:
  - 97% test accuracy
  - 0.01 Mean Squared Error (MSE)
  - 0.97 R² Score

#### Second Layer - Counterfactual Verification
- **Framework**: DiCE (Diverse Counterfactual Explanations)
- **Key Features**:
  - Generates minimal perturbations to flip classifications
  - Focuses on 37 mutable network features
- **Dual-Threshold Mechanism**:
  - **Euclidean Distance**: 95th percentile threshold
  - **Feature Changes**: 95th percentile threshold
- **Adversarial Detection**: 95% accuracy

### Implementation Example

```python
# Counterfactual generation pipeline
d = dice_ml.Data(dataframe=dataset,
                continuous_features=['duration', 'flow_bytes_s', 'flow_pkts_s'],
                outcome_name='Label')

m = dice_ml.Model(model=rf_model, backend="sklearn")

exp = dice_ml.Dice(d, m)

# Generate 3 counterfactuals for each benign sample
counterfactuals = exp.generate_counterfactuals(
    query_instances=benign_samples,
    total_CFs=3,
    desired_class="opposite",
    proximity_weight=0.5,
    diversity_weight=1.0)
```

🛠️ Project Structure
counterfactual-ml-ids/
├── data/                   # Dataset directory
├── docs/                   # Documentation and visuals
├── scripts/                # Utility scripts
│   └── download_dataset.py # Dataset downloader
├── cicids-ids-2018-using-randomforest.ipynb  # Main notebook
├── requirements.txt        # Python dependencies
├── LICENSE
└── README.md

🤝 Contributing
We welcome contributions! Please follow these steps:

Fork the repository

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

📜 License
Distributed under the MIT License. See LICENSE for more information.

✉️ Contact
Shaikh Muhammad Sharjeel - s.muhammad.26932@khi.iba.edu.pk
Project Link: https://github.com/s-m-sharjeel/counterfactual-ml-ids