import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp.settings')
import django

django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Delete all if necessary
# User.objects.all().delete()

try:
    User.objects.create_superuser('admin', 'nima_mahmoudi@live.com', 'pass')
except Exception:
    print("Admin already exists!")

from python_snippets import models
import pandas as pd

# Delete all if necessary
# models.PythonSnippet.objects.all().delete()

data_file_name = '../data/mytable.csv'
df = pd.read_csv(data_file_name, error_bad_lines=False, warn_bad_lines=False)
df = df.head(100)
df = df.where((pd.notnull(df)), None)


max_num_rows = min(100, df.shape[0])

for i in range(max_num_rows):
    row = df.iloc[i, :]
    ps = models.PythonSnippet()
    ps.original_id = row['Id']
    ps.post_id = row['PostId']
    ps.pred_post_block_version_id = row['PredPostBlockVersionId']
    ps.root_post_block_version_id = row['RootPostBlockVersionId']
    ps.length = row['Length']
    ps.line_count = row['LineCount']
    ps.tags = row['Tags']
    ps.content = row['Content']

    try:
        ps.save()
    except Exception:
        pass
