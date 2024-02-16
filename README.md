
# Electronics Recommendation System

## Overview

Welcome to the Electronics Recommendation System project! This system provides personalized recommendations for electronic products based on user preferences. It is built using a content-based filtering approach, leveraging a dataset from Kaggle.

## Features

- Content-based recommendation for electronic products.
- Utilizes machine learning techniques to understand user preferences.
- Easy-to-use Python script for obtaining personalized recommendations.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python (>=3.6)
- Required Python packages: Streamlit

### Installation

Clone the repository:

```bash
git clone https://github.com/your-username/electronics-recommendation-system.git
cd electronics-recommendation-system
```

Copy the `helper` folder and pickled files to your project directory:

```bash
cp -r /path/to/helper /path/to/your/project
cp /path/to/image_file.pkl /path/to/your/project
cp /path/to/product_link_file.pkl /path/to/your/project
cp /path/to/product_name.pkl /path/to/your/project
cp /path/to/top_10_Similar_Products_Index_Matrix.pkl /path/to/your/project
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Usage

Run the recommendation system:

```python
from helper.recommender_system import recommender
```

Load the pickled files:

```python
import pickle

# Load pickled files
image_file = pickle.load(open('image_file.pkl', 'rb'))
product_link_file = pickle.load(open('product_link_file.pkl', 'rb'))
product_name = pickle.load(open('product_name.pkl', 'rb'))
similar_products_matrix = pickle.load(open('top_10_Similar_Products_Index_Matrix.pkl', 'rb'))

# Create a recommender instance
recommendation_system = recommender(image_file, product_link_file, product_name, similar_products_matrix)

# Example usage
user_interests = 894  # nth - ( 894th product) Replace with actual user interests   
recommendations = recommender(user_interests,similar_products_matrix)
print(recommendations)
```

This will provide recommendations based on a user's interests.

for more you can [see](app.py).
## Dataset

The dataset used for training and testing the recommendation system is available on Kaggle. You can find it [here](https://www.kaggle.com/datasets/lokeshparab/amazon-products-dataset).

## Model

The recommendation system uses a content-based filtering approach, analyzing product features to suggest similar items. The model is trained on the provided dataset to understand user preferences and generate personalized recommendations.

## Contributing

If you'd like to contribute to this project, please follow the [Contributing Guidelines](CONTRIBUTING.md).

## Issues

If you encounter any issues or have suggestions, please [open an issue](https://github.com/your-username/electronics-recommendation-system/issues).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to Kaggle for providing the dataset.

