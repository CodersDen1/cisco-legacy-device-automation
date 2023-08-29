import pandas as pd
import json
data_frame={}

def toExcelFile(getData,name):
    item_keys=set()
    output=json.loads(getData)
    for item in output:
        item_keys.update(item.keys())

    data=[]
    for item in output:
        proccessed_item={key: item.get(key , '') for key in item_keys}
        data.append(proccessed_item)

    data_frame = pd.DataFrame(data)

    file_name=f"csv_output/{name}.csv"
     
    data_frame.to_csv(file_name,index=False )
    print(f"\n ******************************\nFile saved as {file_name}")

