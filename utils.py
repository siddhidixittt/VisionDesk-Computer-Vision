import cv2
import os
import tempfile


def draw_detections(frame, detections):
    """Draw bounding boxes and labels on an image."""

    for person_id, detection in enumerate(detections, 1):
        x1, y1, x2, y2 = detection["bbox"]

        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

        label = (
            f'P{person_id} '
            f'{detection["confidence"]:.2f}'
        )

        cv2.putText(
            frame,
            label,
            (x1, max(18, y1 - 7)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.55,
            (0, 255, 0),
            2
        )

    return frame


def save_uploaded_file(uploaded_file):
    """Save a Streamlit upload to a temporary file."""

    suffix = os.path.splitext(
        uploaded_file.name
    )[1]

    file_descriptor, path = tempfile.mkstemp(
        suffix=suffix
    )

    with os.fdopen(file_descriptor, "wb") as file:
        file.write(uploaded_file.getbuffer())

    return path
