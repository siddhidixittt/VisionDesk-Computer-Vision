import pandas as pd


def analyze_detections(
    detections,
    warning_limit=10,
    critical_limit=20
):
    """Calculate occupancy statistics and status."""

    count = len(detections)

    average_confidence = (
        sum(item["confidence"] for item in detections) / count
        if count
        else 0.0
    )

    if count >= critical_limit:
        status = "CRITICAL"
    elif count >= warning_limit:
        status = "WARNING"
    else:
        status = "NORMAL"

    return {
        "count": count,
        "avg_confidence": average_confidence,
        "status": status
    }


def make_report_dataframe(detections):
    """Convert detections into a Pandas report."""

    rows = []

    for person_id, detection in enumerate(detections, 1):
        x1, y1, x2, y2 = detection["bbox"]

        rows.append({
            "person_id": person_id,
            "x1": x1,
            "y1": y1,
            "x2": x2,
            "y2": y2,
            "confidence": round(
                detection["confidence"],
                3
            ),
            "class": detection["class"]
        })

    return pd.DataFrame(rows)
