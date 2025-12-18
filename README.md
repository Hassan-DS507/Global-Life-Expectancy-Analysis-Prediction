# Global Life Expectancy Analysis and Prediction

## Project Overview

This project implements a complete data science pipeline to analyze global life expectancy trends from 2000 to 2015 and build predictive models. The solution combines exploratory data analytics with machine learning to identify key socioeconomic and health determinants of life expectancy across 193 countries.

## Core Features

- **Predictive Modeling**: Random Forest model achieving 96.9% accuracy (R²=0.969) in predicting life expectancy
- **Comprehensive Analysis**: Power BI dashboard with interactive visualizations of global trends and disparities
- **Production-Ready Pipeline**: End-to-end data processing from raw WHO/UN data to actionable insights
- **Domain-Informed Features**: Five engineered features based on public health and economic principles

## Repository Structure

```
Global-Life-Expectancy-Analysis-Prediction/
├── data/                           # Data directories
│   ├── raw/                        # Original WHO dataset
│   └── processed/                  # Cleaned and processed datasets
├── notebooks/                      # Jupyter notebook pipeline
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_preprocessing.ipynb
│   └── 04_modeling.ipynb
├── EDA using Power BI/             # Dashboard and visualizations
├── Models/                         # Serialized machine learning models
├── src/                            # Python source modules
├── submission/                     # Project documentation
└── requirements.txt                # Python dependencies
```

## Installation and Setup

### Prerequisites

- Python 3.8 or higher
- Git

### Clone and Configure the Project

```bash
# Clone the repository
git clone https://github.com/Hassan-DS507/Global-Life-Expectancy-Analysis-Prediction.git

# Navigate to project directory
cd Global-Life-Expectancy-Analysis-Prediction

# Install required dependencies
pip install -r requirements.txt
```

### Data Access

The analysis uses the World Health Organization's Life Expectancy dataset, which is included in the repository under `data/raw/Life_Expectancy_Data.csv`. No external data downloads are required.

## Usage Instructions

### Option 1: Run the Complete Analysis Pipeline

Execute the Jupyter notebooks sequentially to reproduce the entire analysis:

```bash
# Launch the first notebook
jupyter notebook notebooks/01_data_understanding.ipynb
```

Follow this sequence:
1. **Data Understanding** - Initial exploration and issue identification
2. **Data Cleaning** - Handling missing values and data quality issues
3. **Preprocessing** - Feature engineering and preparation
4. **Modeling** - Training and evaluating predictive models

### Option 2: Use Pre-Trained Models for Predictions

Load the optimized Random Forest model for immediate predictions:

```python
import pickle
import pandas as pd

# Load the trained model
with open('Models/random_forest_best_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Prepare your data (ensure same format as training data)
# new_data = pd.DataFrame(...)

# Make predictions
predictions = model.predict(new_data)
```

### Option 3: Explore the Dashboard

For interactive visualization of the analysis results:

1. Install Microsoft Power BI Desktop (free version available)
2. Open `EDA using Power BI/Life_expectancy_Dashboard.pbix`
3. Explore global trends, country comparisons, and factor relationships

## Technical Implementation

### Data Processing

The pipeline addresses common real-world data challenges:
- Missing value imputation using group-wise and global median strategies
- Logarithmic transformation for highly skewed features (GDP, Population)
- Binary encoding for categorical variables (Developed/Developing status)

### Engineered Features

Five domain-specific features were created to improve model interpretability:
1. **Child Mortality Rate** - Combined infant and under-five deaths
2. **Immunization Average** - Average coverage of key vaccines
3. **Economic Strength** - Composite of GDP and income composition
4. **Education Index** - Combined schooling and income metrics
5. **Mortality Pressure** - Composite of adult mortality and HIV/AIDS prevalence

### Model Performance

| Model | MAE (Years) | RMSE (Years) | R² Score |
|-------|-------------|--------------|----------|
| Linear Regression (Baseline) | 2.706 | 3.542 | 0.855 |
| Random Forest (Initial) | 1.065 | 1.703 | 0.966 |
| **Random Forest (Optimized)** | **1.053** | **1.647** | **0.969** |

The optimized Random Forest model uses the following hyperparameters:
- `max_depth`: 20
- `max_features`: 'sqrt'
- `n_estimators`: 400

## Key Findings

### Global Trends (2000-2015)
- Average global life expectancy increased from approximately 67 to 71 years
- Developing countries (83% of dataset) showed consistent improvement but remain below developed nation averages
- Strong geographic patterns: Higher life expectancy in Europe, North America, and Australia; lower in Sub-Saharan Africa and South Asia

### Determinant Analysis
- Development status is the strongest single predictor of life expectancy
- Adult mortality shows the strongest negative correlation with life expectancy
- Economic indicators and education levels have synergistic positive effects
- Immunization coverage is widespread but consistency varies by region

## Business Applications

### For Policy Development
- **Targeted Interventions**: Model identifies highest-impact factors for specific regions
- **Resource Allocation**: Data-driven prioritization of healthcare investments
- **Progress Monitoring**: Framework for tracking intervention effectiveness

### For Research and Analysis
- **Scenario Modeling**: Predict impact of socioeconomic changes on population health
- **Comparative Analysis**: Benchmark country performance against regional peers
- **Trend Forecasting**: Project future life expectancy based on current trajectories

## Support and Maintenance

### Troubleshooting
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Verify Python version compatibility (3.8+ recommended)
- For Power BI dashboard issues, ensure you have the latest version of Power BI Desktop

### Extending the Project
The modular code structure allows for straightforward extensions:
- Add new data sources to `data/raw/`
- Implement additional models in `notebooks/04_modeling.ipynb`
- Create new dashboard visualizations in the Power BI file

