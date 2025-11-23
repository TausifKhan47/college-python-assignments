import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt  
# initialise data of lists
data = {'Name':[ 'Mohe' , 'Karnal' , 'Yrik' , 'jack' ], 'Age':[ 30 , 21 , 29 , 28 ]}
df = pd.DataFrame( data ) 
sns.boxplot( data['Age'] )
plt.show()
