class ObjectDetector:
    def __init__(self, config=None):
        self.config = config
        self.last_detections = []

    def detect(self, frame):
        # Dummy implementation: always detect a single object in the center
        # Replace with real detection code (e.g., YOLO, SSD)
        h, w = frame.shape[:2]
        detection = {
            'bbox': [w//4, h//4, 3*w//4, 3*h//4],
            'confidence': 0.9,
            'label': 'object',
            'distance': 0.5
        }
        self.last_detections = [detection]
        return [detection]

    def get_last_detections(self):
        return self.last_detections

    def update_confidence_threshold(self, threshold):
        if self.config:
            self.config.CONFIDENCE_THRESHOLD = threshold
