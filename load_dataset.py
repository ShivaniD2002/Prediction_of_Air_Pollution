import pandas as pd
from Remote_User.models import air_quality_type

def run():
    air_quality_type.objects.all().delete()

    df = pd.read_csv("Air_Pollution_Datasets.csv", encoding="latin-1")

    for _, row in df.iterrows():
        air_quality_type.objects.create(
            aid=row.get("MID", ""),
            City=row.get("City", ""),
            Date=row.get("Date", ""),
            PM2andhalf=row.get("PM2.5", ""),
            PM10=row.get("PM10", ""),
            NO=row.get("NO", ""),
            NO2=row.get("NO2", ""),
            Nox=row.get("NOx", ""),
            NH3=row.get("NH3", ""),
            CO=row.get("CO", ""),
            SO2=row.get("SO2", ""),
            O3=row.get("O3", ""),
            Benzene=row.get("Benzene", ""),
            Toluene=row.get("Toluene", ""),
            Xylene=row.get("Xylene", ""),
            AQI=row.get("AQI", ""),
            Prediction=row.get("AQI_Bucket", "")
        )

    print("✅ Dataset loaded successfully")
