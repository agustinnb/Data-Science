# Customer Segmentation Clustering

# Import libraries
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

# Read CSV
customer_df= pd.read_csv('segmentation_data.csv')


# Drop Id column
customer_df.drop('ID',axis='columns',inplace=True)


# Kmeans with 3 clusters, we will divide our customers in three different segments.
kmeans=KMeans(n_clusters = 3, init = 'k-means++', max_iter=600, random_state=0)
kmeans.fit(customer_df)

# Now that we have defined our model and fit our customers
customer_df['Clusters']=kmeans.labels_

# Making the logic to plot a graph 
customers_data=customer_df.to_numpy()
pca = PCA(2)
pca_res = pca.fit_transform(customers_data)
customer_df['X'] = pca_res[:,0]
customer_df['Y'] = pca_res[:,1]


cluster_0 = customer_df[customer_df['Clusters'] == 0]
cluster_1 = customer_df[customer_df['Clusters'] == 1]
cluster_2 = customer_df[customer_df['Clusters'] == 2]

plt.scatter(cluster_0['X'], cluster_0['Y'], label='Cluster 0')
plt.scatter(cluster_1['X'], cluster_1['Y'], label='Cluster 1')
plt.scatter(cluster_2['X'], cluster_2['Y'], label='Cluster 2')

plt.legend()
plt.title('Clustering customers visualization')
plt.xlabel('X')
plt.ylabel('Y')

# Visual of our clustering
plt.show()
