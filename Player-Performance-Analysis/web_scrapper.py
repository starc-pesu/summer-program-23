import pandas as pd
from urllib.parse import urlparse, unquote
import re

url = "https://www.espncricinfo.com/cricketers/ab-de-villiers-44936/bowling-batting-stats"
parsed_url = urlparse(url)
path = parsed_url.path
player_name_with_id = path.split('/')[2]
player_name = unquote(player_name_with_id).replace("-", " ")
player_name = re.sub(r'\d+', '', player_name).strip()


tables = pd.read_html(url)

dfs = []
for table in tables:
    df = table.copy()
    dfs.append(df)

if dfs:
    combined_df = pd.concat(dfs)
    output_file = "{name}.csv".format(name=player_name)
    combined_df.to_csv(output_file, index=False)
    print("CSV file successfully generated.")
else:
    print("No tables found")
