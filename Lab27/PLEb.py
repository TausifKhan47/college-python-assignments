import pandas as pd
import seaborn as sns # initialise data of lists
import matplotlib.pyplot as plt 
data = {'Name':[ 'Mohe' , 'Karnal' , 'Yrik' , 'jack' ], 'Age':[ 30 , 21 , 29 , 28 ]}
df = pd.DataFrame( data ) 
sns.violinplot(data['Age'])
plt.show()
