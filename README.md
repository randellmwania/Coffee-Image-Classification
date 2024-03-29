# **COFFEE LEAF DISEASE IMAGE CLASSIFICATION**

Our project addresses the critical challenge of detecting coffee leaf diseases, including Rust, Cercospora, and Phoma, threatening Kenya's coffee farms. Leveraging cutting-edge technology and a dataset of Arabica coffee leaf images, our CNN models achieve remarkable accuracy, empowering farmers with early disease detection to safeguard their livelihoods.

### **Collaborators:**

- Crystal Wanjiru
- Randell Mwania
- Victorine Imbuhila
- Sadi Kiri
- Ian Kedeyie
- Simon Ng'ethe

## ![alt text](banner.jpeg)

# **Business Understanding**

Imagine the rolling hills of Kenya, vibrant with emerald coffee plantations. But a silent threat looms – Coffee rust, Cercospora, and Phoma, diseases capable of wiping out entire harvests and jeopardizing the livelihoods of thousands of small-scale farmers. This project rises to the challenge, wielding a powerful weapon: cutting-edge technology for early and accurate disease detection.

By empowering farmers with this knowledge, we equip them to act swiftly. Timely application of targeted fungicides becomes their shield, minimizing crop losses and protecting their precious income. It's more than just protecting profits; it's safeguarding a cultural cornerstone, preserving the deep-rooted tradition of Kenyan coffee and ensuring the sustainability of the prized Arabica bean.

This project is not just about numbers and yields; it's about people, communities, and the future of a cherished heritage. Join us in this fight to secure the verdant tapestry of Kenyan coffee farms, one healthy leaf at a time.

# **Data Understanding**

The dataset contains leaf images which were collected from Arabica coffee type and it shows three sets of Phoma, Rust and Cescospora images and one set of healthy images. The data was obtained from [Dataset on Mendeley](https://data.mendeley.com/datasets/t2r6rszp5c/1), [Dataset on Mendeley](https://data.mendeley.com/datasets/tgv3zb82nd/1) and web scrapping with the 'Download All images' extension from the chrome web store.

# **Data Preparation**

The data pre-processing involved noise filtering and contrast stretching.

To ensure uniformity, non-square images were cropped to obtain central square portions.

To mitigate overfitting and enhance smaller datasets, data augmentation techniques such as rotation and flipping were applied, expanding the collected field images into larger datasets.

# **Exploratory Data Analysis**

Visualising the data revealed the presence of four classes with balanced distribution in the train and test sets.

Image statistics like mean and standard deviation(std) for each color channel were calculated and analysed.

![alt text](image-1.png)

## Image statistics:

### Pixel intesity for each color channel (Red, Green,Blue)

| Type        | Red Mean  | Green Mean | Blue Mean |
| ----------- | --------- | ---------- | --------- |
| Leafrust    | 146.73724 | 160.34663  | 143.0774  |
| Cerscospora | 121.76627 | 136.07367  | 76.1142   |
| Phoma       | 137.64172 | 145.31422  | 103.19717 |
| Healthy     | 101.7592  | 177.86247  | 113.43119 |

| Type        | Red Std   | Green Std | Blue Std  |
| ----------- | --------- | --------- | --------- |
| Leafrust    | 43.12189  | 30.854395 | 32.087067 |
| Cerscospora | 34.370064 | 29.52207  | 34.861458 |
| Phoma       | 46.71672  | 39.924957 | 44.30027  |
| Healthy     | 44.20804  | 27.321201 | 46.579483 |

# **Modeling**

Four CNN models were developed and evaluated:

- Baseline Model: A simple CNN with flatten and dense layers.
- Model 2: Deeper CNN with additional convolution layers and max pooling.
- Model 3: CNN with increased complexity in convoution layers and dense layers.
- Model 4: Most complex CNN with additional convolution layer and increased units in dense layers.

![alt text](image.png)

# **Results**

- **Model Performance:** Each model iteration showed significant improvement in accuracy, indicating the effectiveness of incorporating more sophisticated architectures.

- **Feature Extraction:** Convolutional layers proved crucial in capturing hierarchical and intricate features within leaf images, resulting in higher classification accuracy.

- **Optimization Techniques:** Utilizing the Adam optimizer contributed to model convergence and enhanced performance across different architectures.

# **Next Steps**

**Monitoring and Improvement:**

- Continuous monitoring: Track the model's performance in real-world settings to ensure accuracy and effectiveness.
  Retraining: Regularly update the model with new data and evolving disease patterns to maintain performance.

**Knowledge Sharing and Community Engagement:**

- Education campaigns: Empower farmers with knowledge on disease prevention, early detection, and sustainable practices.
- User feedback: Collect feedback from farmers to inform future improvements and iterations of the model.

**Sustainability and Expansion:**

- Long-term planning: Develop a sustainable plan for resource allocation, community involvement, and future scaling.
- Testing phase: Thoroughly test the model in real-world settings with the help of farmers and experts.
