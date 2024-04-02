import json
from dashboard.models import Incident

def load_data_from_json(json_file_path):
    with open(json_file_path) as f:
        data = json.load(f)
        for item in data:
            Incident.objects.create(
                intensity=item['intensity'],
                likelihood=item['likelihood'],
                relevance=item['relevance'],
                year=item['year'],
                country=item['country'],
                topics=item['topics'],
                region=item['region'],
                city=item['city']
            )

if __name__ == "__main__":
    json_file_path = "D:\Blackcoffer_Python_Task\VisualizationDashboard\jsondata.json"
    load_data_from_json(json_file_path)
