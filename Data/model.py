from ultralytics import YOLO

# Initialize YOLO models
daModel = YOLO('AI_Models/ublDA_v1.pt')
qpdsModel = YOLO('AI_Models/ubl_QPDS_ST_v1.pt')
sosModel = YOLO('AI_Models/ublSOS_v1.pt')