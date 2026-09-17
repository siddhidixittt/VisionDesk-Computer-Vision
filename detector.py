import cv2


class PersonDetector:
    """
    Person detection component.

    Primary detector:
        YOLOv8n using Ultralytics.

    Fallback detector:
        OpenCV HOG pedestrian detector, when available.

    Only the 'person' class is detected because the project
    focuses on occupancy analysis.
    """

    def __init__(self):
        self.yolo = None
        self.hog = None

        # Try YOLO first.
        try:
            from ultralytics import YOLO
            self.yolo = YOLO("yolov8n.pt")
        except Exception:
            self.yolo = None

        # Only create HOG if YOLO is unavailable.
        if self.yolo is None and hasattr(cv2, "HOGDescriptor"):
            self.hog = cv2.HOGDescriptor()
            self.hog.setSVMDetector(
                cv2.HOGDescriptor_getDefaultPeopleDetector()
            )

    def detect(self, frame, confidence=0.4):
        detections = []

        # Use YOLO when available.
        if self.yolo is not None:
            results = self.yolo.predict(
                frame,
                conf=confidence,
                classes=[0],
                verbose=False
            )

            for result in results:
                if result.boxes is None:
                    continue

                for box in result.boxes:
                    coordinates = (
                        box.xyxy[0]
                        .cpu()
                        .numpy()
                        .astype(int)
                        .tolist()
                    )

                    score = float(
                        box.conf[0]
                        .cpu()
                        .numpy()
                    )

                    detections.append({
                        "bbox": coordinates,
                        "confidence": score,
                        "class": "person"
                    })

            return detections

        # Use HOG only if YOLO is unavailable.
        if self.hog is not None:
            boxes, weights = self.hog.detectMultiScale(
                frame,
                winStride=(8, 8),
                padding=(8, 8),
                scale=1.05
            )

            for (x, y, width, height), weight in zip(boxes, weights):
                score = float(weight)

                if score >= confidence:
                    detections.append({
                        "bbox": [
                            int(x),
                            int(y),
                            int(x + width),
                            int(y + height)
                        ],
                        "confidence": score,
                        "class": "person"
                    })

        return detections