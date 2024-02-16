
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
cp /path/to/top100_product_indexs /path/to/your/project
cp /path/to/Product-details/path/to/your/project
cp /path/to/top10 Similar Products Index Matrix.pkl /path/to/your/project
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Usage

Run the recommendation system:

```python
from helper.recommender_system import recommender,matrix_display

```

Load the pickled files:

```python
import pickle

# Load pickled files
product_details = pkl.load(open('pickled/version2/Product-details.pkl','rb'))
similarity_metrix = pkl.load(open('pickled/version2/top10 Similar Products Index Matrix.pkl','rb'))
top_products_index = pkl.load(open('pickled/version2/top100_product_indexs.pkl','rb'))


# Create a recommender instance
recommended_ids = recommender(selected_product_index,similarity_metrix)

# Example usage
user_interests = 894  # nth - ( 894th product) Replace with actual user interests   
recommendations = recommender(user_interests,similar_products_matrix)
print(recommendations) # recommendations are in the index location format of those products.
```

This will provide recommendations based on a user's interests.

for more you can [see](https://www.kaggle.com/code/akeshkumarhp/amazon-electronics-product-recommender-system)
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

