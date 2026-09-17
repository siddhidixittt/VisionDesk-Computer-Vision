import cv2
import os
import tempfile


def process_video(
    input_path,
    detector,
    confidence,
    warning_limit,
    critical_limit
):
    """Process video and return annotated output plus frame statistics."""

    capture = cv2.VideoCapture(input_path)

    if not capture.isOpened():
        raise ValueError("The uploaded video could not be opened.")

    fps = capture.get(cv2.CAP_PROP_FPS) or 20
    width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH) or 640)
    height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT) or 480)

    output_path = os.path.join(
        tempfile.gettempdir(),
        "visiondesk_annotated.mp4"
    )

    writer = cv2.VideoWriter(
        output_path,
        cv2.VideoWriter_fourcc(*"mp4v"),
        fps,
        (width, height)
    )

    rows = []
    frame_number = 0

    while True:
        success, frame = capture.read()

        if not success:
            break

        frame_number += 1

        # Analyse every second frame to reduce processing time.
        if frame_number % 2 == 0:
            detections = detector.detect(
                frame,
                confidence
            )

            count = len(detections)

            if count >= critical_limit:
                status = "CRITICAL"
            elif count >= warning_limit:
                status = "WARNING"
            else:
                status = "NORMAL"

            for detection in detections:
                x1, y1, x2, y2 = detection["bbox"]

                cv2.rectangle(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    (0, 255, 0),
                    2
                )

                cv2.putText(
                    frame,
                    f'person {detection["confidence"]:.2f}',
                    (x1, max(20, y1 - 5)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 255, 0),
                    1
                )

            cv2.putText(
                frame,
                f"People: {count} | Status: {status}",
                (15, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 0, 255) if status != "NORMAL"
                else (255, 255, 255),
                2
            )

            rows.append({
                "frame": frame_number,
                "people_count": count,
                "status": status
            })

        writer.write(frame)

    capture.release()
    writer.release()

    return output_path, rows
