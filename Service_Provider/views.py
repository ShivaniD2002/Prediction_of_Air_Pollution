from django.shortcuts import render, redirect
from django.db.models import Avg, Q
from django.http import HttpResponse
import pandas as pd
import xlwt

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from Remote_User.models import (
    ClientRegister_Model,
    air_quality_type,
    air_quality_type_ratio,
    detection_accuracy
)

# ================================
# SERVICE PROVIDER LOGIN
# ================================
def serviceproviderlogin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == "Admin" and password == "Admin":
            return redirect("View_Remote_Users")

    return render(request, "SProvider/serviceproviderlogin.html")


# ================================
# DASHBOARD
# ================================
def View_Remote_Users(request):
    users = ClientRegister_Model.objects.all()
    return render(request, "SProvider/View_Remote_Users.html", {"objects": users})


# ================================
# TRAIN & TEST DATASETS
# ================================
def Train_Test_Datasets(request):

    detection_accuracy.objects.all().delete()

    df = pd.read_csv("Air_Pollution_Datasets.csv", encoding="latin-1")

    def label_map(x):
        mapping = {
            "Poor": 0,
            "Very Poor": 1,
            "Severe": 2,
            "Moderate": 3,
            "Satisfactory": 4,
            "Good": 5,
        }
        return mapping.get(x, 0)

    df["label"] = df["AQI_Bucket"].apply(label_map)

    X = df["MID"]
    y = df["label"]

    cv = CountVectorizer()
    X_vec = cv.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_vec, y, test_size=0.2, random_state=42
    )

    # ---- SVM ----
    svm = LinearSVC()
    svm.fit(X_train, y_train)
    svm_acc = accuracy_score(y_test, svm.predict(X_test)) * 100
    detection_accuracy.objects.create(names="SVM", ratio=svm_acc)

    # ---- Logistic Regression ----
    lr = LogisticRegression(max_iter=1000)
    lr.fit(X_train, y_train)
    lr_acc = accuracy_score(y_test, lr.predict(X_test)) * 100
    detection_accuracy.objects.create(names="Logistic Regression", ratio=lr_acc)

    # ---- Decision Tree ----
    dt = DecisionTreeClassifier()
    dt.fit(X_train, y_train)
    dt_acc = accuracy_score(y_test, dt.predict(X_test)) * 100
    detection_accuracy.objects.create(names="Decision Tree", ratio=dt_acc)

    # ---- KNN ----
    knn = KNeighborsClassifier()
    knn.fit(X_train, y_train)
    knn_acc = accuracy_score(y_test, knn.predict(X_test)) * 100
    detection_accuracy.objects.create(names="KNN", ratio=knn_acc)

    results = detection_accuracy.objects.all()
    return render(request, "SProvider/Train_Test_Datasets.html", {"objs": results})


# ================================
# CHARTS (ACCURACY)
# ================================
def charts(request, chart_type):
    data = detection_accuracy.objects.values("names").annotate(
        dcount=Avg("ratio")
    )

    return render(
        request,
        "SProvider/charts.html",
        {"form": data, "chart_type": chart_type},
    )


# ================================
# PREDICTION DETAILS
# ================================
def View_Air_Pollution_Predicted_Details(request):
    data = air_quality_type.objects.all()
    return render(
        request,
        "SProvider/View_Air_Pollution_Predicted_Details.html",
        {"objs": data},
    )


# ================================
# RATIO CALCULATION
# ================================
def Find_Air_Pollution_Predicted_Ratio(request):

    air_quality_type_ratio.objects.all().delete()

    total = air_quality_type.objects.count()
    if total == 0:
        return render(
            request,
            "SProvider/Find_Air_Pollution_Predicted_Ratio.html",
            {"objs": []},
        )

    categories = ["Poor", "Very Poor", "Severe", "Moderate", "Satisfactory", "Good"]

    for cat in categories:
        count = air_quality_type.objects.filter(Prediction=cat).count()
        ratio = (count / total) * 100
        air_quality_type_ratio.objects.create(names=cat, ratio=ratio)

    objs = air_quality_type_ratio.objects.all()
    return render(
        request,
        "SProvider/Find_Air_Pollution_Predicted_Ratio.html",
        {"objs": objs},
    )


# ================================
# LIKE CHART (RATIO)
# ================================
def likeschart(request, chart_type):
    data = air_quality_type_ratio.objects.values("names").annotate(
        dcount=Avg("ratio")
    )

    return render(
        request,
        "SProvider/likeschart.html",
        {"form": data, "chart_type": chart_type},
    )


# ================================
# DOWNLOAD DATA
# ================================
def Download_Trained_DataSets(request):

    response = HttpResponse(content_type="application/ms-excel")
    response["Content-Disposition"] = 'attachment; filename="PredictedData.xls"'

    wb = xlwt.Workbook(encoding="utf-8")
    ws = wb.add_sheet("Predictions")

    headers = [
        "City", "Date", "PM2.5", "PM10", "NO", "NO2", "NOx",
        "NH3", "CO", "SO2", "O3", "Benzene", "Toluene",
        "Xylene", "AQI", "Prediction"
    ]

    for col, header in enumerate(headers):
        ws.write(0, col, header)

    rows = air_quality_type.objects.all()
    for row_idx, obj in enumerate(rows, start=1):
        ws.write(row_idx, 0, obj.City)
        ws.write(row_idx, 1, obj.Date)
        ws.write(row_idx, 2, obj.PM2andhalf)
        ws.write(row_idx, 3, obj.PM10)
        ws.write(row_idx, 4, obj.NO)
        ws.write(row_idx, 5, obj.NO2)
        ws.write(row_idx, 6, obj.Nox)
        ws.write(row_idx, 7, obj.NH3)
        ws.write(row_idx, 8, obj.CO)
        ws.write(row_idx, 9, obj.SO2)
        ws.write(row_idx, 10, obj.O3)
        ws.write(row_idx, 11, obj.Benzene)
        ws.write(row_idx, 12, obj.Toluene)
        ws.write(row_idx, 13, obj.Xylene)
        ws.write(row_idx, 14, obj.AQI)
        ws.write(row_idx, 15, obj.Prediction)

    wb.save(response)
    return response
